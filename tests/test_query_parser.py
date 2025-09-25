"""
Tests for scripts/query_parser.py
Validates Boolean grammar (AND/OR/NOT, precedence, parentheses),
quoted phrases, and wildcard handling.
"""

import sys
from pathlib import Path
import pytest

# Add scripts dir to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from query_parser import parse_query, pretty_print, TermNode, AndNode, OrNode, NotNode, QuerySyntaxError  # type: ignore


class TestQueryParser:
    def test_simple_and(self):
        node = parse_query("A AND B")
        assert isinstance(node, AndNode)
        assert all(isinstance(c, TermNode) for c in node.children)

    def test_simple_or(self):
        node = parse_query("A OR B")
        assert isinstance(node, OrNode)
        assert all(isinstance(c, TermNode) for c in node.children)

    def test_simple_not(self):
        node = parse_query("NOT A")
        assert isinstance(node, NotNode)
        assert isinstance(node.child, TermNode)

    def test_nested_expression(self):
        node = parse_query("A AND (B OR C)")
        assert isinstance(node, AndNode)
        assert isinstance(node.children[1], OrNode)

    def test_operator_precedence(self):
        n1 = parse_query("NOT A OR B")
        # Should be (NOT A) OR B
        assert isinstance(n1, OrNode)
        assert isinstance(n1.children[0], NotNode)

        n2 = parse_query("A AND B OR C")
        # Should be (A AND B) OR C
        assert isinstance(n2, OrNode)
        assert isinstance(n2.children[0], AndNode)

    def test_phrase(self):
        node = parse_query('"hello world"')
        assert isinstance(node, TermNode)
        assert node.is_phrase is True
        assert "hello\\s+world" in node.pattern

    def test_wildcard(self):
        node = parse_query('forest*')
        assert isinstance(node, TermNode)
        assert node.is_phrase is False
        assert node.pattern.endswith(r"\w*")

    def test_phrase_with_wildcard(self):
        node = parse_query('"ecosystem service*"')
        assert isinstance(node, TermNode)
        assert node.is_phrase is True
        assert node.pattern.endswith(r"\w*")

    def test_empty_query_raises(self):
        with pytest.raises(QuerySyntaxError):
            parse_query("")

    def test_mismatched_parentheses(self):
        with pytest.raises(QuerySyntaxError):
            parse_query("(A AND B")
"""
Tests for query_parser.py module.
"""

import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from query_parser import parse_query, pretty_print, QuerySyntaxError


def test_parses_simple_and():
    node = parse_query("A AND B")
    s = pretty_print(node)
    assert "AND" in s and '"A"' in s and '"B"' in s


def test_parses_simple_or():
    node = parse_query("A OR B")
    s = pretty_print(node)
    assert "OR" in s and '"A"' in s and '"B"' in s


def test_parses_simple_not():
    node = parse_query("NOT A")
    s = pretty_print(node)
    assert "NOT" in s and '"A"' in s


def test_parses_quoted_phrase_and_wildcard():
    node = parse_query('"hello world*" AND test*')
    s = pretty_print(node)
    assert "hello world" in s and "test" in s


def test_parses_nested_expression():
    node = parse_query("A AND (B OR C)")
    s = pretty_print(node)
    assert "AND" in s and "OR" in s


def test_operator_precedence():
    # NOT has highest precedence, then AND, then OR
    node = parse_query("NOT A OR B")
    s = pretty_print(node)
    # Expect OR at top, NOT applied to A
    assert s.splitlines()[0].strip() == "OR"


def test_invalid_operator_raises():
    with pytest.raises(QuerySyntaxError):
        parse_query("A NAND B")


def test_mismatched_parentheses_raises():
    with pytest.raises(QuerySyntaxError):
        parse_query("(A AND B")


def test_empty_query_raises():
    with pytest.raises(QuerySyntaxError):
        parse_query("")
