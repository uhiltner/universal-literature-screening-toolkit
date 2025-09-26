# ULST Architectural Plan — Pivot to Raw Search String Engine

Date: 2025-09-25
Owner: Architectural Leader (Python)
Status: Planning complete; ready for implementation and test generation

## Executive Summary

We will deprecate the BLOCK-based search model and introduce a Raw Search String Engine. Users provide one database-style Boolean query (e.g., ((forest* OR wood*) AND (management OR planning)) AND ("ecosystem service*" OR biodiversity) AND NOT (economics)). Internally, we parse this string into an AST and evaluate it against document text. This aligns with researcher workflows and simplifies the CLI.


## 1) Deconstruction of the Current System

Target: remove BLOCK parsing and combination logic while preserving PDF extraction, reporting, and CLI ergonomics.

- scripts/search_parser.py
  - Current: parses BLOCKS from search_terms.txt and compiles regex per block.
  - Plan: deprecate fully. Replace with scripts/query_parser.py.
  - Transition: keep a thin compatibility shim for one release cycle that reads search_terms.txt, emits a deprecation warning, and converts BLOCKS into an equivalent raw query string (best-effort OR/AND join) to feed the new engine. If conversion is ambiguous, fail with guidance.

- scripts/validator.py
  - Current: evaluates per-block matches based on config-driven AND/OR logic and combinations.
  - Plan: refactor to evaluate an AST produced by query_parser (no reliance on BLOCKS or block_combinations).

- run_screening.py (CLI)
  - Current: --search-terms points to search_terms.txt; relies on BLOCKS + config.validation_logic.
  - Plan: add --query-file (path to .txt containing the raw query). For one release: support both; precedence to --query-file with a deprecation warning when --search-terms is used. In a subsequent release, remove --search-terms.

- config.json
  - Current: validation_logic (default_operator, block_combinations) influences BLOCK evaluation.
  - Plan: mark validation_logic as deprecated; it is ignored when using --query-file. In the next major version, remove it. Keep text_processing and output_settings as-is.

- scripts/report_generator.py
  - Current: shows blocks and term matches.
  - Plan: show the raw query used; optionally show a normalized/pretty-printed version. Continue showing matched evidence snippets.

- Documentation and examples
  - Deprecate search_terms.txt format in README/QUICK_START/USER_GUIDE and examples/.
  - Add examples/query.txt and guidance for writing Boolean queries.


## 2) Design of the New Query Engine

Two components: a Parser (query_parser.py) and an Evaluator (validator.py).

### 2.1 Parsing Component (query_parser.py)

- Library choice: pyparsing
  - Rationale: small, mature, expressive for infix boolean grammars with precedence and grouping; easy error reporting with location.
  - Alternative: lark (suitable and robust; heavier footprint). Only choose if we later add more complex grammars.

- Supported syntax
  - Operators: AND, OR, NOT (case-insensitive). Optional synonyms: &&, ||, ! (v2).
  - Parentheses: ( ... ) for grouping; nested allowed.
  - Terms:
    - Single tokens: letters/digits/underscore/hyphen allowed inside terms.
    - Wildcards: trailing * only (e.g., forest*, ecosys*). Mid-word * supported in v2 if needed.
    - Quoted phrases: "..." may include spaces and wildcard *. E.g., "ecosystem service*".
  - Whitespace: insignificant between tokens; required between terms unless quoted.

- Operator precedence
  - NOT > AND > OR, with parentheses overriding precedence.

- Output data structure (AST)
  - Use small immutable dataclasses (or typed dicts) representing nodes:
    - AndNode(children: list[Node])
    - OrNode(children: list[Node])
    - NotNode(child: Node)
    - TermNode(original: str, is_phrase: bool, pattern: str)  // pattern is a compiled-friendly regex string
  - Node protocol (duck-typed): .kind in {and, or, not, term}; and/or have .children; not has .child; term has .pattern and .original.

- Regex strategy (built at parse-time)
  - Case-insensitive matching by default (configurable via text_processing.case_sensitive if retained).
  - Term without quotes:
    - forest -> word-boundary: \bforest\b
    - forest* -> \bforest\w* (prefer \w* over .* to avoid spanning punctuation; review with multilingual texts)
  - Quoted phrase:
    - "ecosystem service" -> \becosystem\s+service\b
    - "ecosystem service*" -> \becosystem\s+service\w*
  - Escape regex metacharacters in user terms except wildcard * which we translate.

- Public API
  - parse_query(query: str) -> Node  // raises QuerySyntaxError with (message, loc, line, col, context)
  - pretty_print(node: Node) -> str   // for logging/report aesthetics

### 2.2 Evaluation Component (validator.py)

- Core contract
  - evaluate_ast(node: Node, text: str) -> tuple[bool, list[MatchEvidence]]
    - Returns (boolean verdict, evidence snippets list). Evidence for operators is the union of child evidences that contributed to True; for NOT, evidence is empty unless we record the negated term’s absence (not needed).

- Algorithm
  - Preprocess text once per document (lowercasing if not case-sensitive, unicode normalization NFKC, collapse whitespace).
  - For TermNode: compile regex once (re.compile(..., flags)) and search in text. Capture 1-2 short context windows as evidence.
  - For AndNode: short-circuit false; evaluate children left-to-right; collect evidence from True children.
  - For OrNode: short-circuit true; collect evidence from the child that satisfied the OR (configurable to collect all).
  - For NotNode: evaluate child; result = not child_result; evidence: empty.

- Efficiency
  - Compile all term regexes once and cache by pattern string (LRU dict) per run.
  - Use finditer only when evidence is requested; otherwise use search for speed.
  - Consider optional field-scoped evaluation (title/abstract/keywords) in a follow-up; initial version uses whole extracted text blob to preserve current behavior.

- Field weighting (non-goal for v1)
  - We do not score; we only boolean-match. Future extension could allow field scoping e.g., title:forest*.


## 3) Error Handling and Validation

- Parser errors
  - Types: mismatched parentheses; unexpected token; dangling operator; unknown operator; empty query.
  - Exception: QuerySyntaxError(message, loc, line, col, near=token)
  - UX: Render the line with a caret under the error position and an actionable fix hint.

- Runtime errors
  - Term compilation errors (after escaping): report which term failed and why.
  - Empty document text: treat as no matches, result False (with a note in results.error if desired).

- CLI behavior
  - Fail fast: parse at startup; on error, exit with code != 0 and a succinct message.
  - Deprecation warnings when using --search-terms or validation_logic in config.


## 4) Impact on Existing Contracts

- New/updated interfaces
  - scripts/query_parser.py
    - parse_query(query: str) -> Node
    - pretty_print(node: Node) -> str
  - scripts/validator.py
    - evaluate_ast(node: Node, text: str) -> tuple[bool, list[MatchEvidence]]
    - validate_papers(json_dir: str, query_node: Node, config: dict) -> list[Result]
  - scripts/report_generator.py
    - generate_html_report(results: list[Result], query_string: str, output_dir: str) -> Path
  - run_screening.py
    - Add CLI arg --query-file PATH; read query string; call parse_query; pass node downstream.
    - Continue to accept --search-terms for one release; emit deprecation and internally convert to a raw query best-effort or exit with guidance.

- Data shapes (contract sketch)
  - MatchEvidence: { term: str, span: [start, end], snippet: str }
  - Result: { filename: str, include: bool, evidence: list[MatchEvidence], error: str | null }

- Removed/ignored inputs
  - config.validation_logic no longer used in query mode.


## 5) Phased Implementation Plan

- Phase 0: Guardrails
  - Add deprecation warnings and feature flag plumbing; ensure tests continue to pass using legacy path while we build the new path behind a test-only switch.

- Phase 1: Parser
  - Add pyparsing to requirements.txt.
  - Implement parse_query with precedence and grouping; translate terms to regex patterns; robust error messages.
  - Unit tests: parser success and failure cases (see §6).

- Phase 2: Evaluator
  - Implement evaluate_ast with short-circuiting and evidence collection; caching of compiled regex.
  - Unit tests: evaluator truth tables and evidence snippets.

- Phase 3: CLI integration
  - Update run_screening.py to accept --query-file; wire parser->evaluator; keep legacy path with deprecation.
  - Update report generation to show raw query; ensure validation_results.json schema remains stable (add query_string field).

- Phase 4: Documentation & Examples
  - Update README, QUICK_START, USER_GUIDE.
  - Add examples/query.txt and refresh examples/README.md.

- Phase 5: Remove legacy
  - In next minor/major, remove --search-terms, search_parser.py, and config.validation_logic.


## 6) Comprehensive Testing Strategy

- Parser unit tests (new: tests/test_query_parser.py)
  - test_parses_simple_and: A AND B
  - test_parses_simple_or: A OR B
  - test_parses_simple_not: NOT A
  - test_parses_quoted_phrase: "hello world"
  - test_parses_wildcard: test*
  - test_parses_nested_expression: A AND (B OR C)
  - test_parses_complex_expression: (A OR B) AND NOT ("C D" OR E*)
  - test_handles_case_insensitivity: a aNd b
  - test_operator_precedence: NOT A OR B == (NOT A) OR B; A AND B OR C == (A AND B) OR C

- Parser failure tests
  - test_fails_on_mismatched_parentheses: (A AND B
  - test_fails_on_invalid_operator: A NAND B
  - test_fails_on_dangling_operator: A AND
  - test_fails_on_empty_query: ""

- Evaluator unit tests (update tests/test_validator.py or add new)
  - test_evaluator_simple_and_true/false
  - test_evaluator_nested_or
  - test_evaluator_not_clause
  - test_evaluator_wildcard_match (testing -> test*)
  - test_evaluator_phrase_match (contains "hello world")
  - test_short_circuiting_behavior (ensure no unnecessary term evals)

- Integration tests (tests/test_cli_integration.py)
  - Provide a sample query.txt and 2–3 PDFs (use existing input_pdfs/ if suitable).
  - Run run_screening.py end-to-end; assert validation_results.json includes correct include/exclude per the query.
  - Assert HTML report includes the raw query string.

- Regression tests
  - Ensure legacy path still works during transition; then remove once legacy removed.


## 7) Migration & Backward Compatibility

- CLI
  - Introduce --query-file; keep --search-terms with deprecation warning in this release.
  - If both are provided, prefer --query-file and warn.

- Config
  - Ignore validation_logic when using --query-file; warn once.

- User comms
  - Add migration notes to README/USER_GUIDE: how to translate typical BLOCKS into a raw query with examples.


## 8) Risks and Mitigations

- Parsing complexity
  - Mitigation: small grammar with clear precedence; extensive parser tests; helpful errors.

- Performance for large texts
  - Mitigation: compile regex once; case-insensitive; short-circuiting; optional evidence throttling.

- International text and token boundaries
  - Mitigation: use \b and \w conservatively; add integration tests with non-English texts; allow configuration to relax word boundaries if needed in a follow-up.

- Dependency footprint
  - Mitigation: pyparsing is lightweight; no heavy runtime deps added.


## 9) Deliverables and Ownership

- Code: query_parser.py; updated validator.py; CLI changes; report updates.
- Tests: test_query_parser.py; updates to test_validator.py and test_cli_integration.py.
- Docs: README, QUICK_START, USER_GUIDE; examples/query.txt.
- Ops: Deprecation warnings and removal plan documented in CHANGELOG (if present).


## 10) Success Criteria

- Functional: All new tests pass; integration test validates correct include/exclude with a sample query.
- Usability: Users can provide a single Boolean query file; clear errors on invalid queries.
- Maintainability: Contracts are simple; code remains modular and documented.
- Back-compat: Legacy path works with warnings during the transition release; removed on schedule.


## Appendix A — Example Query and AST

Query:

((forest* OR wood*) AND (management OR planning)) AND ("ecosystem service*" OR biodiversity) AND NOT (economics)

Simplified AST shape (pretty print):

AND
├─ AND
│  ├─ OR
│  │  ├─ TERM("\\bforest\\w*")
│  │  └─ TERM("\\bwood\\w*")
│  └─ OR
│     ├─ TERM("\\bmanagement\\b")
│     └─ TERM("\\bplanning\\b")
├─ OR
│  ├─ TERM("\\becosystem\\s+service\\w*")
│  └─ TERM("\\bbiodiversity\\b")
└─ NOT
   └─ TERM("\\beconomics\\b")


## Appendix B — Minimal Node Protocol (sketch)

- Node.kind in {and, or, not, term}
- And/Or: Node.children: list[Node]
- Not: Node.child: Node
- Term: Node.pattern: str; Node.original: str; Node.is_phrase: bool
