"""
Tests for AST-based evaluation in validator.py using the query parser.
Skips cleanly if pyparsing (parser dependency) is not installed.
"""

import sys
from pathlib import Path
import pytest

try:
    import pyparsing  # noqa: F401
except Exception:  # pragma: no cover - environment without deps
    pytest.skip("pyparsing not installed; skipping query-evaluator tests", allow_module_level=True)

# Add scripts dir to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from query_parser import parse_query  # type: ignore
from validator import evaluate_ast, validate_single_paper_query  # type: ignore


def test_evaluate_ast_and_or_not():
    text = "This paper covers forest management and planning, with ecosystem services."
    node = parse_query('forest AND management')
    verdict, evidence = evaluate_ast(node, text)
    assert verdict is True
    assert evidence and any('forest' in e['snippet'].lower() for e in evidence)

    node2 = parse_query('forest OR ocean')
    v2, _ = evaluate_ast(node2, text)
    assert v2 is True

    node3 = parse_query('forest AND NOT urban')
    v3, _ = evaluate_ast(node3, text)
    assert v3 is True

    node4 = parse_query('forest AND NOT planning')
    v4, _ = evaluate_ast(node4, text)
    assert v4 is False


def test_evaluate_ast_phrase_and_wildcard():
    text = "The study covers ecosystem services and forested landscapes in detail."
    node = parse_query('"ecosystem service*" AND forest*')
    verdict, evidence = evaluate_ast(node, text)
    assert verdict is True
    # Evidence may be limited; ensure structure
    assert isinstance(evidence, list)


def test_validate_single_paper_query_structure():
    paper = {
        "filename": "sample.pdf",
        "full_text": "Decision support systems for forest management and optimization of ecosystem services."
    }
    cfg = {"text_processing": {"case_sensitive": False}}
    node = parse_query('decision AND forest AND optimization')
    res = validate_single_paper_query(paper, node, cfg)
    assert res["filename"].endswith("sample.pdf")
    assert res["overall_result"] is True
    assert "block_results" in res and isinstance(res["block_results"], list)
    assert res["total_blocks"] == 1
    assert res["blocks_passed"] in (0, 1)
