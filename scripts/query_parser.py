"""
Boolean Query Parser for ULST

Parses a raw Boolean query string into an AST and prepares regex patterns
for efficient evaluation by the validator. Supports:
  - Operators: AND, OR, NOT (case-insensitive)
  - Parentheses for grouping
  - Terms with trailing wildcard *
  - Quoted phrases, optionally with trailing * on the last token

Public API:
  parse_query(query: str) -> Node
  pretty_print(node: Node) -> str

Error handling:
  Raises QuerySyntaxError with message and location info on invalid input.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union
import re

from pyparsing import (
    CaselessKeyword,
    Forward,
    Group,
    Literal,
    ParseBaseException,
    ParserElement,
    QuotedString,
    StringEnd,
    Word,
    alphanums,
    Suppress,
    infixNotation,
    opAssoc,
)


class QuerySyntaxError(Exception):
    """Raised when the query string cannot be parsed."""

    def __init__(self, message: str, loc: int | None = None, line: str | None = None, col: int | None = None):
        super().__init__(message)
        self.loc = loc
        self.line = line
        self.col = col


@dataclass(frozen=True)
class TermNode:
    kind: str
    original: str
    is_phrase: bool
    pattern: str


@dataclass(frozen=True)
class AndNode:
    kind: str
    children: List["Node"]


@dataclass(frozen=True)
class OrNode:
    kind: str
    children: List["Node"]


@dataclass(frozen=True)
class NotNode:
    kind: str
    child: "Node"


Node = Union[TermNode, AndNode, OrNode, NotNode]


def _escape_term_to_regex(term: str, is_phrase: bool) -> str:
    """Translate a term to a regex pattern string with word boundaries and wildcard support.

    Rules:
    - Unquoted: word-boundary on both sides; trailing * -> \w*
      e.g., forest -> \bforest\b, forest* -> \bforest\w*
    - Quoted: treat spaces as \s+; add word-boundaries at start and end; last token may have * suffix
      e.g., "ecosystem service" -> \becosystem\s+service\b
            "ecosystem service*" -> \becosystem\s+service\w*
    """
    if not is_phrase:
        if term.endswith("*"):
            stem = term[:-1]
            return r"\b" + re.escape(stem) + r"\w*"
        return r"\b" + re.escape(term) + r"\b"

    # phrase case
    inner = term
    # If trailing wildcard present on last token in phrase
    trailing_wild = inner.endswith("*")
    if trailing_wild:
        inner = inner[:-1]

    # Split on whitespace and join with \s+
    tokens = inner.strip().split()
    if not tokens:
        return r""

    escaped = [re.escape(tok) for tok in tokens]
    body = r"\s+".join(escaped)
    if trailing_wild:
        # Allow suffix on last token
        if len(tokens) == 1:
            body = escaped[0] + r"\w*"
        else:
            body = r"\s+".join(escaped[:-1] + [escaped[-1] + r"\w*"])
        # For trailing wildcard phrases, omit the trailing word boundary to allow extended suffixes
        return r"\b" + body

    return r"\b" + body + r"\b"


def parse_query(query: str) -> Node:
    """Parse the Boolean query into an AST.

    Raises QuerySyntaxError with basic location information on invalid input.
    """
    if query is None or query.strip() == "":
        raise QuerySyntaxError("Empty query string")

    ParserElement.set_default_whitespace_chars(" \t\r\n")

    LPAREN, RPAREN = map(Suppress, (Literal("("), Literal(")")))
    AND = CaselessKeyword("AND")
    OR = CaselessKeyword("OR")
    NOT = CaselessKeyword("NOT")

    # Terms: unquoted words with allowed chars, or quoted strings
    # Allow '*' to be part of word so trailing wildcard stays with the token
    word = Word(alphanums + "_-.*")
    phrase = QuotedString('"', escChar='\\', unquoteResults=True)

    def make_term(original: str, is_phrase: bool) -> TermNode:
        return TermNode(kind="term", original=original, is_phrase=is_phrase, pattern=_escape_term_to_regex(original, is_phrase))

    # Use set_parse_action with context to mark phrase vs word
    word.set_parse_action(lambda s, l, t: make_term(t[0], False))
    phrase.set_parse_action(lambda s, l, t: make_term(t[0], True))

    operand = Forward()
    # Parentheses should just yield the inner operand (no extra grouping)
    atom = (phrase | word | (LPAREN + operand + RPAREN))

    def and_action(tokens):
        nodes: List[Node] = [tok for tok in tokens[0][::2]]
        flat: List[Node] = []
        for n in nodes:
            if isinstance(n, AndNode):
                flat.extend(n.children)
            else:
                flat.append(n)
        return AndNode(kind="and", children=flat)

    def or_action(tokens):
        nodes: List[Node] = [tok for tok in tokens[0][::2]]
        flat: List[Node] = []
        for n in nodes:
            if isinstance(n, OrNode):
                flat.extend(n.children)
            else:
                flat.append(n)
        return OrNode(kind="or", children=flat)

    def not_action(tokens):
        node = tokens[0][1]
        return NotNode(kind="not", child=node)

    expr = infixNotation(
        atom,
        [
            (NOT, 1, opAssoc.RIGHT, not_action),
            (AND, 2, opAssoc.LEFT, and_action),
            (OR, 2, opAssoc.LEFT, or_action),
        ],
    )

    operand <<= expr

    try:
        parsed = (expr + StringEnd()).parse_string(query, parse_all=True)
        return parsed[0]
    except ParseBaseException as e:
        msg = f"Query syntax error at col {e.column}: {e.msg}"
        raise QuerySyntaxError(msg, loc=e.loc, line=e.line, col=e.column)


def pretty_print(node: Node, indent: int = 0) -> str:
    pad = "".rjust(indent)
    if isinstance(node, TermNode):
        return f"{pad}TERM(\"{node.original}\" -> {node.pattern})"
    if isinstance(node, AndNode):
        lines = [f"{pad}AND"]
        for c in node.children:
            lines.append(pretty_print(c, indent + 2))
        return "\n".join(lines)
    if isinstance(node, OrNode):
        lines = [f"{pad}OR"]
        for c in node.children:
            lines.append(pretty_print(c, indent + 2))
        return "\n".join(lines)
    if isinstance(node, NotNode):
        lines = [f"{pad}NOT"]
        lines.append(pretty_print(node.child, indent + 2))
        return "\n".join(lines)
    return f"{pad}<unknown>"
