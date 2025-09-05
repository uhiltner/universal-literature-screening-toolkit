"""
Generic Validation Module

Applies configurable search criteria to extracted paper content.
Supports any research domain with customizable validation logic.
"""

import json
import re
from pathlib import Path
from search_parser import compile_regex_patterns
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

def validate_papers(json_dir, search_blocks, config_path="config.json"):
    """Validate papers against search criteria using configurable logic."""
    
    # Load configuration
    config = load_config(config_path)
    
    # Load paper content
    papers = load_json_content(json_dir)

    if not papers:
        raise ValueError(f"No papers found in {json_dir}")

    # Compile search patterns
    compiled_blocks = compile_regex_patterns(search_blocks)

    validation_results = []

    for paper in papers:
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
