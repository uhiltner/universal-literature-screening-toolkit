---
mode: agent
role: architectural-leader
priority: high
context: Universal Literature Screening Toolkit (ULST) – Strategic Pivot
---

**Subject: Strategic Pivot: Evolving from `BLOCK` System to a "Raw Search String" Engine**

**Team,**

After a thorough review of the ULST's core value proposition and its limitations, we are making a strategic architectural decision. To achieve our goal of creating a truly universal, domain-agnostic screening tool, we will be deprecating the current `BLOCK`-based search system in favor of a more powerful and flexible "Raw Search String" engine.

**The Vision (Solution 4):**

The user experience will be simplified and empowered. Instead of translating their logic into our `BLOCK` system, researchers will provide a single text file (e.g., `query.txt`) containing one complete, database-style Boolean search string.

**Example `query.txt`:**
```
((forest* OR wood*) AND (management OR planning)) AND ("ecosystem service*" OR biodiversity) AND NOT (economics)
```

This aligns the ULST directly with the established workflows of researchers and the capabilities of professional academic search platforms.

**Architectural Mandate:**

As the Architectural Leader, your primary task is to design the transition to this new architecture. I need a comprehensive plan that addresses the following key areas. This plan will serve as the blueprint for the Programmer and Test Generator agents.

**1. Deconstruction of the Current System:**
    *   Outline the plan for phasing out the `BLOCK` system.
    *   Identify which modules will be deprecated or completely refactored (e.g., `search_parser.py`).

**2. Design of the New "Query Engine":**
    *   **Parsing Component:** Propose a robust strategy for parsing the raw search string.
        *   Specify the recommended Python library (e.g., `pyparsing`, `lark`, or another suitable alternative) for handling keywords, quoted phrases, wildcards, parentheses, and operators (`AND`, `OR`, `NOT`).
        *   Define the data structure that the parser will output (e.g., an Abstract Syntax Tree or another form of logic tree).
    *   **Evaluation Component:** Design the new `validator.py` logic.
        *   It must be able to recursively traverse the logic tree produced by the parser.
        *   It must efficiently apply this logic to the extracted text of each document.

**3. Error Handling and Validation:**
    *   A critical part of this design is user-friendly error handling. The plan must include a strategy for detecting and reporting syntax errors in the user's search string (e.g., mismatched parentheses, invalid operators). The tool must fail gracefully with actionable feedback.

**4. Impact on Existing Contracts:**
    *   Update the core contracts (`search_parser.py` will no longer return blocks, `validator.py` will take a logic tree instead of blocks).
    *   Define the new function signatures and data flows.

**5. A Phased Implementation Plan:**
    *   Break down the implementation into logical, testable steps for the Programmer agent.
        *   *Suggestion:* Start with the parser, then the evaluator, then integrate it into the main `run_screening.py` workflow.

**6. A Comprehensive Testing Strategy:**
    *   Provide a plan for the Test Generator agent. This must include:
        *   **Unit Tests** for the new parser (e.g., `test_parses_simple_expression`, `test_parses_nested_expression`, `test_handles_wildcards_and_phrases`).
        *   **Unit Tests** for the new evaluator (e.g., `test_evaluator_simple_and`, `test_evaluator_nested_or`, `test_evaluator_not_clause`).
        *   **Integration Tests** that run the full pipeline with a sample `query.txt` and a few PDFs, asserting the correct `include`/`exclude` outcome.
        *   **Failure Tests** that prove the system provides clear errors for invalid search strings.

**Deliverable:**

A detailed architectural plan in markdown format that addresses all the points above. This document will be the single source of truth for the development team to execute this pivot.

**Justification:**

This is a significant but necessary evolution. It elevates the ULST from a useful utility to an essential piece of research infrastructure, directly addressing a key limitation and ensuring its long-term relevance and defensibility in a peer-review context.
