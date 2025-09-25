"""
Generic Validation Module

Applies configurable search criteria to extracted paper content.
Supports both legacy BLOCK-based validation and new AST-based Boolean query evaluation.
"""

import json
import re
from pathlib import Path
from search_parser import compile_regex_patterns
from typing import List, Tuple, Dict, Any

# Query AST types (imported lazily to avoid tight coupling during legacy runs)
try:
    from query_parser import TermNode, AndNode, OrNode, NotNode, pretty_print
except Exception:
    TermNode = AndNode = OrNode = NotNode = None  # type: ignore
    pretty_print = None  # type: ignore
from pdf_extractor import load_json_content, get_paper_filename

def load_config(config_path="config.json"):
    """Load configuration settings."""
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        # Default configuration if file not found
        return {
            "validation_logic": {"default_operator": "AND"},
            "text_processing": {"case_sensitive": False, "encoding": "utf-8"}
        }

def validate_papers(json_dir, search_blocks, config_path="config.json", *, query_node=None):
    """Validate papers against search criteria using configurable logic.

    Modes:
    - Legacy mode (search_blocks provided, query_node is None):
        Evaluate per-block regexes with config-driven AND/OR and combinations.
    - Query mode (query_node provided):
        Evaluate a Boolean AST against document text; config.validation_logic is ignored.
    """

    # Load configuration
    config = load_config(config_path)

    # Load paper content
    papers = load_json_content(json_dir)

    if not papers:
        raise ValueError(f"No papers found in {json_dir}")

    # Prepare compiled patterns (legacy) or regex cache (query)
    compiled_blocks = None
    if query_node is None:
        compiled_blocks = compile_regex_patterns(search_blocks)

    validation_results = []

    for paper in papers:
        if query_node is not None:
            result = validate_single_paper_query(paper, query_node, config)
        else:
            result = validate_single_paper(paper, compiled_blocks, config)
        validation_results.append(result)

    return validation_results

def validate_single_paper(paper, compiled_blocks, config):
    """Validate a single paper against all search blocks with configurable logic."""

    # Extract filename - handle both JSON filename and PDF filename
    json_filename = paper.get("filename", "unknown")
    pdf_filename = get_paper_filename(json_filename)

    full_text = paper.get("full_text", "")

    if not full_text:
        return create_validation_result(pdf_filename, [], False, "No text content")
                                                                               
    block_results = []

    # Check each validation block
    for block in compiled_blocks:
        matches = block["regex"].findall(full_text)
        block_passed = len(matches) > 0

        block_result = {
            "block_name": block["name"],
            "passed": block_passed,
            "matches_found": len(matches),
            "sample_matches": matches[:5] if matches else []
        }

        block_results.append(block_result)

    # Apply validation logic from configuration
    validation_logic = config.get("validation_logic", {})
    default_operator = validation_logic.get("default_operator", "AND")
    
    # Check for special block combinations
    block_combinations = validation_logic.get("block_combinations", {})
    if "blocks" in block_combinations and "operator" in block_combinations:
        # Handle special combinations (like DSS4ES BES blocks)
        special_blocks = block_combinations["blocks"]
        combined_name = block_combinations.get("combined_name", "Combined Block")
        
        # Find special blocks
        special_results = [b for b in block_results if any(sb in b["block_name"] for sb in special_blocks)]
        regular_results = [b for b in block_results if not any(sb in b["block_name"] for sb in special_blocks)]
        
        if special_results:
            # Combine special blocks
            if block_combinations["operator"] == "AND":
                combined_passed = all(b["passed"] for b in special_results)
            else:  # OR
                combined_passed = any(b["passed"] for b in special_results)
            
            combined_block = {
                "block_name": combined_name,
                "passed": combined_passed,
                "matches_found": -1,  # Combined result
                "sample_matches": [f"Combined result from {len(special_results)} blocks"]
            }
            
            final_blocks = regular_results + [combined_block]
        else:
            final_blocks = block_results
    else:
        final_blocks = block_results

    # Overall result based on default operator
    if default_operator == "AND":
        overall_passed = all(block["passed"] for block in final_blocks)
    else:  # OR
        overall_passed = any(block["passed"] for block in final_blocks)

    return create_validation_result(pdf_filename, final_blocks, overall_passed)


# ------------------ Query-mode evaluation ------------------

_REGEX_CACHE: Dict[str, Any] = {}


def _compile_regex(pattern: str, case_sensitive: bool) -> Any:
    flags = 0 if case_sensitive else re.IGNORECASE
    key = (pattern, flags)
    if key in _REGEX_CACHE:
        return _REGEX_CACHE[key]
    try:
        rx = re.compile(pattern, flags)
    except re.error as e:
        raise ValueError(f"Invalid term regex pattern '{pattern}': {e}")
    _REGEX_CACHE[key] = rx
    return rx


def _prep_text(text: str, case_sensitive: bool) -> str:
    if not text:
        return ""
    # Normalize whitespace; case handled by regex flags
    return re.sub(r"\s+", " ", text).strip()


def _evidence_from_matches(rx, text: str, term: str, context: int = 30) -> List[Dict[str, Any]]:
    ev: List[Dict[str, Any]] = []
    for m in rx.finditer(text):
        start, end = m.span()
        s = max(0, start - context)
        e = min(len(text), end + context)
        snippet = text[s:e]
        ev.append({"term": term, "span": [start, end], "snippet": snippet})
        if len(ev) >= 3:
            break
    return ev


def evaluate_ast(node, text: str, *, case_sensitive: bool = False) -> Tuple[bool, List[Dict[str, Any]]]:
    """Evaluate the Boolean AST over the text and collect match evidence.

    Returns (verdict, evidence_list).
    """
    text2 = _prep_text(text, case_sensitive)

    def eval_node(n) -> Tuple[bool, List[Dict[str, Any]]]:
        # Term
        if hasattr(n, "kind") and getattr(n, "kind") == "term":
            rx = _compile_regex(n.pattern, case_sensitive)
            m = rx.search(text2)
            if m:
                return True, _evidence_from_matches(rx, text2, n.original)
            return False, []

        # NOT
        if hasattr(n, "kind") and getattr(n, "kind") == "not":
            res, _ev = eval_node(n.child)
            return (not res), []

        # AND
        if hasattr(n, "kind") and getattr(n, "kind") == "and":
            all_ev: List[Dict[str, Any]] = []
            for c in n.children:
                ok, ev = eval_node(c)
                if not ok:
                    return False, []
                all_ev.extend(ev)
            return True, all_ev

        # OR
        if hasattr(n, "kind") and getattr(n, "kind") == "or":
            first_ev: List[Dict[str, Any]] = []
            any_true = False
            for c in n.children:
                ok, ev = eval_node(c)
                if ok and not any_true:
                    any_true = True
                    first_ev = ev
            return any_true, (first_ev if any_true else [])

        # Unknown node
        return False, []

    return eval_node(node)


def validate_single_paper_query(paper, query_node, config):
    """Validate a single paper using AST-based Boolean evaluation."""
    json_filename = paper.get("filename", "unknown")
    pdf_filename = get_paper_filename(json_filename)
    full_text = paper.get("full_text", "")

    if not full_text:
        # Keep schema similar, but block_results becomes evidence list for query mode
        return {
            "filename": pdf_filename,
            "overall_result": False,
            "block_results": [],
            "error": "No text content",
            "total_blocks": 0,
            "blocks_passed": 0,
            "validation_date": "2025-09-05",
        }

    case_sensitive = config.get("text_processing", {}).get("case_sensitive", False)
    verdict, evidence = evaluate_ast(query_node, full_text, case_sensitive=case_sensitive)
    # Represent evidence in block_results for backward-compatible report consumption
    block_results = [{
        "block_name": "Query",
        "passed": verdict,
        "matches_found": len(evidence),
        "sample_matches": [e.get("snippet", "") for e in evidence]
    }]

    return create_validation_result(pdf_filename, block_results, verdict)

def create_validation_result(filename, block_results, overall_passed, error=None):
    """Create standardized validation result."""

    return {
        "filename": filename,
        "overall_result": overall_passed,
        "block_results": block_results,
        "error": error,
        "total_blocks": len(block_results),
        "blocks_passed": sum(1 for b in block_results if b["passed"]),
        "validation_date": "2025-09-05"
    }

def save_validation_results(results, output_path):
    """Save validation results to JSON file."""

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
