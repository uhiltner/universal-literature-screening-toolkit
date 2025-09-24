---
mode: agent
role: programmer
priority: high
context: Universal Literature Screening Toolkit (ULST) – Python 3.8+, cross-platform (Windows/macOS/Linux)
---

# ULST Programmer Task List (from Quality Reviewer)

This is a precise, LLM-optimized backlog to fix correctness, documentation, and UX risks before release. Follow the acceptance criteria and produce evidence for each task.

## Goals
- Correctness first: enforce config invariants, Boolean logic, and stable outputs
- Documentation/CLI parity: README/QUICK_START must match actual behavior
- Robustness: friendly errors, safe PDF handling, cross-OS paths
- Performance: compile regex once; avoid repeated work

## P0 – Critical User-Facing Fixes (blockers)

1) Rebuild README.md (corruption fix + parity)
- Files: `README.md`, `QUICK_START.md`, `USER_GUIDE.md`
- Do: Reconstruct `README.md` (no duplicated headers/badges), verify examples match CLI flags and output filenames/paths. Cross-link QUICK_START and USER_GUIDE.
- Acceptance:
   - README renders cleanly on GitHub (one H1, valid badges)
   - CLI usage snippet aligns with `run_screening.py -h`
   - Example run produces `results/validation_results.json` and `results/validation_report.html` as documented
- Evidence:
   - Paste `run_screening.py -h` output excerpt in PR description
   - Screenshot or link to rendered README preview

2) Windows PowerShell script variable safety
- File: `scripts/run_tool.ps1`
- Do: Replace any ambiguous `$Input` usages with `$InputPath` (or unique names). Ensure parameters have `[Parameter(Mandatory=$true)]` where needed. Avoid names colliding with PowerShell automatic variables.
- Acceptance:
   - Running the script with `-InputPath` works and does not shadow `$Input`
   - Script returns non-zero exit code on failure
- Evidence:
   - Show a successful script invocation and one failure case with exit codes

3) Config invariants and validation gate
- Files: `run_screening.py`, `scripts/validator.py`, `config.json`
- Do: Add a `validate_config(config)` step early (before processing):
   - Enforce `default_operator` ∈ {"AND","OR"} (case-insensitive)
   - Validate `block_combinations` structure (if present): list of lists of ints within range
   - Provide defaults if missing, with warnings
- Acceptance:
   - Invalid config raises a clear, actionable error; valid config logs normalized values
- Evidence:
   - Unit tests for valid/invalid cases; CLI run with invalid config shows friendly error

## P1 – Correctness and Performance

4) Pre-compile and cache regex patterns
- File: `scripts/search_parser.py`
- Do: Convert all generated regex strings to compiled patterns once per run; ensure flags `re.IGNORECASE|re.UNICODE` are set; support wildcards (`term*`) and exact phrases (`"term phrase"`).
- Acceptance:
   - Patterns compiled once; reused by validator
   - Unit tests covering: wildcard, exact phrase, multi-language accents
- Evidence:
   - Test names (examples): `test_regex_wildcards_case_insensitive`, `test_exact_phrase_multilang`

5) Boolean logic correctness in validator
- File: `scripts/validator.py`
- Do: Honor `default_operator` across blocks; if `block_combinations` is provided, evaluate combos precisely; ensure evaluation on lowercase/normalized text; document tie-breaking and empty block policies.
- Acceptance:
   - Tests prove AND/OR behavior and `block_combinations` precedence
   - Empty or malformed blocks handled deterministically with explicit errors/warnings
- Evidence:
   - Tests: `test_validator_and_or`, `test_validator_block_combinations`, `test_validator_empty_blocks`

6) Path normalization and deterministic outputs
- Files: `run_screening.py`, `scripts/report_generator.py`, `scripts/pdf_extractor.py`
- Do: Normalize all input/output paths via `os.path.abspath` + `os.path.normpath`; never embed absolute paths in outputs. Ensure outputs are written under `results/` with stable filenames.
- Acceptance:
   - Windows and Unix paths behave identically; no absolute paths in JSON/HTML
- Evidence:
   - Cross-OS path unit test for join/norm

7) PDF extraction safety and scope
- File: `scripts/pdf_extractor.py`
- Do: Extract ONLY title, abstract, keywords per design; ensure PyMuPDF primary with pdfplumber fallback; always close documents; normalize Unicode; handle empty/malformed PDFs gracefully.
- Acceptance:
   - Unit tests: extraction limited to pure elements; fallback path covered; resource cleanup confirmed (no warnings/exceptions)
- Evidence:
   - Tests: `test_pdf_extractor_title_abstract_keywords_only`, `test_pdf_extractor_fallback_plumber`

## P1 – Reporting and UX

8) Report generation correctness
- File: `scripts/report_generator.py`
- Do: Guarantee creation of `results/sorted_pdfs/{include,exclude}` and consistent `validation_results.json`/`validation_report.html`. JSON schema includes: filename, verdict, evidence snippets, error (nullable).
- Acceptance:
   - Tests assert directories created and files sorted deterministically
   - JSON schema validated by test; HTML contains count summary
- Evidence:
   - Tests: `test_report_sorted_paths`, `test_report_json_schema`, `test_report_html_summary`

9) Friendly error messages and logging
- Files: `run_screening.py`, `scripts/*`
- Do: Wrap top-level CLI with try/except that prints user-friendly messages and exits with non-zero code; use logging with INFO/ERROR levels and clear context per file.
- Acceptance:
   - Intentional failure (bad path/bad config) prints actionable message, not raw traceback
- Evidence:
   - CLI run screenshot/logs; unit test capturing stderr

## P2 – Documentation, Scripts, and Tests

10) CLI-docs parity sweep
- Files: `run_screening.py`, `README.md`, `QUICK_START.md`
- Do: Ensure all CLI options documented; examples use correct flags and file names; QUICK_START matches Windows/macOS/Linux flows.
- Acceptance:
   - `run_screening.py -h` and README options list are consistent
- Evidence:
   - Diff or table mapping flags → docs

11) Test suite hardening and BDD-style names
- Files: `tests/`
- Do: Add tests for the new validations and edge cases; prefer readable, behavior-driven names; keep fixtures minimal.
- Acceptance:
   - All tests pass locally; failure modes covered (invalid config, unreadable PDF)
- Evidence:
   - `pytest -q` summary; added tests listed in PR

12) Cross-OS scripts polish
- Files: `scripts/run_tool.ps1`, `scripts/run_tool.sh`, `scripts/run_tests.ps1`, `scripts/run_tests.sh`, `scripts/setup_windows.ps1`, `scripts/setup_unix.sh`
- Do: Ensure scripts return proper exit codes; print clear usage; avoid shell-specific pitfalls; Windows launcher examples included in docs.
- Acceptance:
   - Manual runs show correct exit codes and usage help
- Evidence:
   - Log excerpts of success + intentional failure

## Evidence Requirements (per PR)
- Terminal output:
   - `pytest -q` passing summary
   - One small CLI run on sample PDFs that generates artifacts
- Artifacts:
   - `results/validation_results.json`
   - `results/validation_report.html`
   - `results/sorted_pdfs/include/…`, `results/sorted_pdfs/exclude/…`
- Snippets:
   - `run_screening.py -h` excerpt to prove CLI-docs parity
   - JSON schema example (one entry) showing required fields

## Suggested Test Additions (names only)
- `test_config_validation_invalid_operator_raises`
- `test_config_validation_block_combinations_schema`
- `test_regex_wildcards_and_exact_phrase_multilang`
- `test_validator_and_or`
- `test_validator_block_combinations`
- `test_pdf_extractor_title_abstract_keywords_only`
- `test_pdf_extractor_fallback_plumber`
- `test_cli_smoke_generates_expected_artifacts`
- `test_report_json_schema`
- `test_report_sorted_paths`

## Definition of Done
- All acceptance criteria above satisfied
- All unit/integration tests pass locally
- Readme/Quick Start match actual CLI and outputs
- No hard-coded absolute paths; paths normalized
- Patterns compiled once; validator honors config

## Quick Commands (Windows PowerShell)
```powershell
# Run tests
pytest -q

# Show CLI help
python run_screening.py -h

# Smoke run (adjust paths as needed)
python run_screening.py --config config.json --search-terms search_terms.txt --input-dir .\input_pdfs --output-dir .\results
```

Deliver this file back to the Quality Reviewer with links to evidence in the PR.

---
mode: agent
role: code_reviewer
priority: high
context: Universal Literature Screening Toolkit (ULST) - Python 3.8+ cross-platform application
---

# ULST Code Review Request

## Project Overview
You are reviewing the **Universal Literature Screening Toolkit v2.0**, a production-ready Python application for systematic literature review and automated PDF screening. This is a cross-platform, domain-agnostic tool designed for researchers and students.

## Current Application State
- **Functionality**: ✅ WORKING - Successfully processes PDFs, extracts text, validates against search criteria, generates professional reports
- **Architecture**: ✅ SOLID - Modular design with clear separation of concerns
- **Testing**: ✅ COMPREHENSIVE - 38 test cases across 6 test files
- **Documentation**: ✅ MULTI-LEVEL - README, QUICK_START, USER_GUIDE for different user types
- **Cross-Platform**: ✅ SUPPORTED - Windows PowerShell & Unix shell scripts

## Core Components to Review

### 1. Entry Point & CLI
- **File**: `run_screening.py` (270 lines)
- **Purpose**: Main CLI interface with argparse
- **Key Features**: Input validation, configuration loading, pipeline orchestration
- **Focus Areas**: Error handling, user experience, argument validation

### 2. PDF Processing Pipeline
- **File**: `scripts/pdf_extractor.py` (200 lines)
- **Purpose**: PDF text extraction with PyMuPDF/pdfplumber fallback
- **Key Features**: Multi-library support, robust error handling, text cleaning
- **Focus Areas**: Unicode handling, extraction reliability, performance

### 3. Search Term Processing  
- **File**: `scripts/search_parser.py` (108 lines)
- **Purpose**: Parse user-defined search blocks into regex patterns
- **Key Features**: Block-based validation, wildcard support, multi-language
- **Focus Areas**: Regex pattern generation, validation logic, edge cases

### 4. Validation Engine
- **File**: `scripts/validator.py` (estimated ~200 lines)
- **Purpose**: Core validation logic with Boolean operations
- **Key Features**: AND/OR logic, configurable validation, paper scoring
- **Focus Areas**: Logic correctness, performance, configurability

### 5. Report Generation
- **File**: `scripts/report_generator.py` (estimated ~150 lines)
- **Purpose**: HTML report generation and PDF file organization
- **Key Features**: Professional HTML output, file sorting, JSON export
- **Focus Areas**: Template quality, data presentation, file handling

## Known Issues to Address

### CRITICAL Issues
1. **README.md Corruption**
   - **Problem**: Duplicated headers, broken badge formatting, text corruption
   - **Impact**: Major user-facing issue, first impression problem
   - **Action**: Complete README reconstruction needed

### MEDIUM Issues  
2. **PowerShell Variable Conflict**
   - **File**: `scripts/run_tool.ps1:17`
   - **Problem**: `$Input` variable conflicts with PowerShell automatic variable
   - **Impact**: Potential unexpected behavior on Windows
   - **Action**: Rename to `$InputPath` or similar

### LOW Issues
3. **Testing Environment Setup**
   - **Problem**: Tests require proper Python environment activation
   - **Impact**: CI/CD and development workflow
   - **Action**: Verify virtual environment configuration

## Review Focus Areas

### Code Quality Priorities
1. **Error Handling**: Robust exception handling throughout pipeline
2. **Unicode/Encoding**: Proper UTF-8 handling for international content
3. **Performance**: Efficient processing for large PDF collections
4. **Memory Management**: Proper resource cleanup in PDF processing
5. **Configuration Validation**: Input validation and default handling

### Architecture Review
1. **Modularity**: Clean separation between parsing, validation, and reporting
2. **Extensibility**: How easy is it to add new output formats or validation logic?
3. **Testing**: Coverage of edge cases, integration test quality
4. **Documentation**: Code comments, docstrings, type hints

### User Experience
1. **Error Messages**: Clear, actionable error messages for users
2. **Progress Feedback**: Appropriate logging and progress indication  
3. **Configuration**: Intuitive configuration file structure
4. **Cross-Platform**: Consistent behavior across Windows/Mac/Linux

## Success Criteria for Review

### Must Pass
- [ ] Core functionality works end-to-end
- [ ] No critical bugs or security issues
- [ ] README.md properly formatted and informative
- [ ] PowerShell variable conflict resolved
- [ ] Error handling covers common failure modes

### Should Pass
- [ ] Code follows Python best practices (PEP 8, typing)
- [ ] Test coverage is comprehensive for critical paths
- [ ] Documentation is clear and complete
- [ ] Performance is acceptable for typical use cases
- [ ] Configuration system is intuitive

### Nice to Have
- [ ] Code is highly modular and extensible
- [ ] Advanced error recovery mechanisms
- [ ] Performance optimizations for large datasets
- [ ] Additional output formats beyond HTML/JSON

## Validation Commands

### Test Application Functionality
```bash
# Basic functionality test
powershell -NoProfile -ExecutionPolicy Bypass -File "scripts\run_tool.ps1" -InputPath "input_pdfs" -OutputPath "results" -SearchTermsPath "examples\search_terms_dss4es.txt"

# Expected: 2 PDFs processed, HTML report generated, files sorted correctly
```

### Test Suite Execution
```bash  
# Full test suite (when Python environment configured)
pytest tests/ -v

# Expected: All 38 tests pass
```

### Documentation Validation
- [ ] README.md renders correctly on GitHub
- [ ] QUICK_START.md provides clear beginner path
- [ ] Examples work out of the box

## Review Deliverables Requested

1. **Priority Issues List**: Critical, Medium, Low priority issues with specific fixes
2. **Code Quality Assessment**: Overall code quality score and improvement recommendations
3. **Architecture Feedback**: Strengths and suggested architectural improvements
4. **User Experience Review**: Usability issues and enhancement suggestions
5. **Test Coverage Analysis**: Missing test cases and edge case identification
6. **Documentation Review**: Clarity, completeness, and accuracy assessment

## Context Notes
- **Target Users**: Researchers, students, literature review specialists
- **Deployment**: Cross-platform desktop application, not web service
- **Scale**: Designed for 10s-100s of PDFs, not enterprise-scale processing  
- **Maintenance**: Should be maintainable by academic researchers, not just developers

**Timeline**: This is ready for final polish before JOSS publication submission. Focus on production-readiness and user experience quality.

---

**Review this application as if it were going into production use by researchers worldwide. Be thorough but practical - focus on issues that would impact real users.**