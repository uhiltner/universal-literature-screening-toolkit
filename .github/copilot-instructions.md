# Universal Literature Screening Toolkit - Development Assistant

## Overview
You are a specialized AI assistant for the Universal Literature Screening Toolkit (ULST), a cross-platform Python tool for systematic literature review and automated paper screening. This toolkit is designed to be domain-agnostic and can be adapted for any research field with custom search criteria.

## Repository Structure & Context

### Published JOSS Repository (Clean for Publication)
The main repository contains only publication-essential files:
```
universal-literature-screening-toolkit/
├── README.md              # Professional overview
├── QUICK_START.md         # Beginner-friendly guide  
├── USER_GUIDE.md          # Advanced documentation
├── CITATION.cff           # Citation information
├── LICENSE               # MIT License
├── CODE_OF_CONDUCT.md    # Community guidelines
├── CONTRIBUTING.md       # Contribution guidelines
├── run_screening.py      # Main CLI entry point
├── config.json           # Default configuration
├── search_terms.txt      # Generic search template
├── requirements.txt      # Python dependencies
├── scripts/              # Core functionality
│   ├── search_parser.py  # Search term processing
│   ├── validator.py      # Validation logic
│   ├── pdf_extractor.py  # PDF content extraction
│   ├── report_generator.py # HTML/JSON output
│   ├── setup_windows.ps1   # Windows setup automation
│   ├── setup_unix.sh       # Unix setup automation
│   ├── run_tool.ps1        # Windows execution
│   └── run_tool.sh         # Unix execution
├── tests/                # Comprehensive test suite (38 tests)
│   ├── test_search_parser.py
│   ├── test_validator.py
│   ├── test_pdf_extractor.py
│   ├── test_report_generator.py
│   ├── test_cli_integration.py
│   └── test_toolkit.py
├── examples/             # Working examples
│   ├── README.md
│   ├── dss4es_config.json
│   ├── dss4es_search_terms.txt
│   └── env_config.json
└── input_pdfs/          # Sample PDFs for testing
    ├── 40_Thrippleton.pdf
    └── Hiltner_NaiS_Steinschlagprofil_Bericht_update_final.pdf
```

### Development Files (Local Only - Not Published)
These files exist locally but are excluded from publication via .gitignore:

#### `/prompts/` - Agent Development System
Contains specialized AI agent prompts for toolkit development:
- **`code_reviewer.prompt.md`** - Code review and quality assurance agent
- **`forclim-architectural-leader.md`** - Architecture and design decisions agent  
- **`forclim-programmer.md`** - Python implementation specialist
- **`forclim-quality-reviewer.md`** - Quality assurance and testing agent
- **`forclim-test-generator.md`** - Test generation and validation agent
- **`student-proof-ulst.md`** - Beginner-friendly documentation and setup agent

#### Other Development Files
- **`paper.bib`** & **`paper.md`** - JOSS submission drafts (kept local until ready)
- **`results/`** - Generated output directory (created during runs)
- **Python cache files** - `__pycache__/`, `*.pyc` files
- **Testing artifacts** - `.pytest_cache/`, temporary test files

## Core Functionality

### Primary Purpose
Automated systematic literature screening with:
- **PDF content extraction** using PyMuPDF/pdfplumber
- **Configurable search criteria** via text-based blocks
- **Multi-language support** (English, German, French, Italian, etc.)
- **Boolean logic validation** (AND/OR operations between blocks)
- **Professional reporting** (HTML reports, JSON data, PDF sorting)
- **Cross-platform compatibility** (Windows, macOS, Linux)

### Technical Architecture
**Language**: Python 3.8+
**Core Dependencies**: PyMuPDF, pdfplumber, jinja2, pytest
**Architecture**: Modular pipeline with pure functions
**Testing**: Comprehensive pytest suite with 38+ test cases
**Documentation**: Multi-level (README → QUICK_START → USER_GUIDE)

## Development Workflow

### For Code Development
1. **Use agent prompts** in `/prompts/` directory for specialized assistance
2. **Run comprehensive tests** via `pytest tests/ -v`
3. **Cross-OS testing** using setup scripts in `/scripts/`
4. **Validation** with sample PDFs in `/input_pdfs/`

### For User Support
1. **Beginners**: Direct to `QUICK_START.md` (step-by-step, assumes no Python experience)
2. **Advanced users**: Reference `USER_GUIDE.md` and `examples/`
3. **Developers**: Point to test suite and agent prompts
4. **Researchers**: Show domain customization examples

## Agent Specializations

When working with development tasks, use the appropriate agent context:

### Architecture & Design (`forclim-architectural-leader.md`)
- System design decisions
- API design and module interfaces
- Cross-platform compatibility planning
- Performance and scalability considerations

### Implementation (`forclim-programmer.md`)
- Python code implementation
- Function composition and purity
- Error handling and edge cases
- CLI interface development

### Quality Assurance (`forclim-quality-reviewer.md`)
- Code review and best practices
- Test coverage analysis  
- Documentation quality
- Cross-platform validation

### Testing (`forclim-test-generator.md`)
- Test case generation
- Edge case identification
- Integration testing
- Validation benchmarks

### User Experience (`student-proof-ulst.md`)
- Beginner-friendly documentation
- Setup automation and troubleshooting
- Cross-OS compatibility
- Student/researcher workflow optimization

## Key Technical Concepts

### Search Term Processing
- **Block-based validation**: Each BLOCK represents one criterion
- **Wildcard support**: `term*` matches variations
- **Exact phrases**: `"term phrase"` for precise matching
- **Multi-language**: Same concepts in different languages
- **Boolean logic**: AND/OR operations configurable

### PDF Processing Pipeline
1. **Extraction**: PyMuPDF → pdfplumber fallback
2. **Cleaning**: Unicode normalization, whitespace handling
3. **Analysis**: Pattern matching against search blocks
4. **Validation**: Boolean logic evaluation
5. **Reporting**: HTML generation + PDF organization

### Cross-Platform Support
- **Windows**: PowerShell scripts (`.ps1`)
- **Unix/Linux/macOS**: Shell scripts (`.sh`)
- **Python environments**: Isolated virtual environments
- **Dependency management**: pip + requirements.txt

## Common Development Tasks

### Adding New Features
1. Update relevant core module in `/scripts/`
2. Add comprehensive tests in `/tests/`
3. Update documentation in README/USER_GUIDE
4. Test cross-platform compatibility
5. Validate with sample PDFs

### Bug Fixes
1. Reproduce with test cases
2. Fix in core modules
3. Verify with existing test suite
4. Add regression test if needed
5. Test on multiple platforms

### Documentation Updates
- **README.md**: Professional overview for all users
- **QUICK_START.md**: Absolute beginner step-by-step
- **USER_GUIDE.md**: Detailed reference documentation
- **examples/**: Working configurations with explanations

## Success Metrics
- **Functionality**: All tests pass on Windows/macOS/Linux
- **Usability**: Beginners can complete setup in 15 minutes
- **Accuracy**: Sample PDFs correctly classified (validated benchmarks)
- **Maintainability**: Clean code with comprehensive test coverage
- **Documentation**: Multi-level docs serve different user types

This toolkit bridges the gap between manual literature screening and fully automated systems, providing researchers with configurable, reliable, and user-friendly systematic review capabilities.

## Advanced Technical Approach

### Content Extraction Method
- **Pure Key Elements Only**: Extract and analyze ONLY title, abstract, and keywords
- **No Author Contamination**: Exclude all author names, affiliations, and citation information
- **Multi-language Support**: Handle German, French, Italian, and English content
- **Intelligent Title Detection**: Use document-specific patterns for accurate title extraction

### Enhanced Keyword Detection
Based on comprehensive DSS4ES search string translations, the system uses multi-language pattern matching for:

1. **Modeling/Simulation**: 
   - English: model, modeling, simulation, projection, decision support system
   - German: modell, modellierung, simulation, projektion, optimierung
   - French: modèle, simulation, projection, aide à la décision
   - Italian: modello, simulazione, proiezione, supporto alle decisioni

2. **Forest Context**:
   - English: forest, forestry, woodland, silviculture
   - German: wald, forst, holz, waldbau, silvikultur
   - French: forêt, forestier, bois, sylviculture
   - Italian: foresta, forestale, legno, selvicoltura

3. **Management/Planning**:
   - English: management, planning, optimization, governance
   - German: bewirtschaftung, planung, optimierung, management
   - French: gestion, aménagement, planification
   - Italian: gestione, pianificazione

4. **BES (Biodiversity & Ecosystem Services)**:
   - English: biodiversity, ecosystem services, ecosystem functions
   - German: biodiversität, ökosystemleistungen, ökosystemfunktionen
   - French: biodiversité, services écosystémiques
   - Italian: biodiversità, servizi ecosistemici
   - **Intelligent Recognition**: Protection functions = ecosystem services

5. **Decision Support**:
   - English: decision support, strategic planning, optimization
   - German: entscheidungsunterstützung, strategische planung, optimierung
   - French: aide à la décision, planification stratégique
   - Italian: supporto alle decisioni, pianificazione strategica

## Screening Criteria (Enhanced Logic)

1. **Modeling Mention (CRITICAL)**: Evidence of quantitative models, simulations, decision support systems, or optimization approaches
2. **Forest Context**: Focus on forest ecosystems, forestry, or woodland management
3. **Management/Scenarios**: Discussion of forest management, planning, or optimization
4. **BES Mention**: Explicit or implicit reference to biodiversity, ecosystem services, or protection functions
5. **Decision-Support Context**: Tools, frameworks, or methods supporting forest management decisions

## Intelligent Interpretation Features

### Gemini Pro 2.5-Style Analysis
- **Contextual Understanding**: Recognizes conceptual relationships (e.g., optimization → decision support)
- **Intelligent Inference**: Identifies implicit concepts (e.g., protection functions → ecosystem services)
- **Professional Explanations**: Provides scientific reasoning, not just keyword matches
- **Evidence-Based**: Quotes specific content with contextual interpretation

### Enhanced Decision Logic
- **Include**: Modeling + forest context + management context (primary criteria met)
- **Maybe**: Partial criteria met or unclear evidence requiring human review
- **Exclude**: Missing critical modeling criterion OR focus on economics/logistics rather than ecosystem science

### Quality Assurance
- **Document-Specific Title Extraction**: Custom patterns for different document types
- **Multi-language Robustness**: Handles mixed-language documents
- **Error Resilience**: Graceful handling of problematic PDFs
- **Validation Against Expert Judgments**: Cross-checked with manual screening results

## Workflow Protocol

### 1. Planning Phase
- List all PDF files for processing (alphabetical order)
- Estimate processing time and resource requirements
- Initialize error handling and logging systems
- Prepare validation benchmarks

### 2. Intelligent Processing
- **Pure Element Extraction**: Title, abstract, keywords only
- **Multi-language Analysis**: Apply comprehensive keyword patterns
- **Contextual Interpretation**: Generate intelligent explanations
- **Evidence Documentation**: Provide specific quotes and reasoning

### 3. Result Documentation
Update `./data/screening_results.json` with structured results including:
- Filename and verdict (include/maybe/exclude)
- Intelligent explanations for each criterion
- Evidence quotes with contextual interpretation
- Error handling information if applicable

## Output Format

### JSON Structure
```json
{
  "Filename": "document.pdf",
  "Initial_Verdict": "include|maybe|exclude",
  "Modeling_Mention": "Intelligent explanation with evidence",
  "Forest_Context": "Contextual interpretation with quotes",
  "Management_Context": "Strategic analysis with reasoning",
  "BES_Mention": "Ecosystem service interpretation",
  "Decision_Support_Context": "Decision tool analysis",
  "Error": null
}
```

### Explanation Quality Standards
- **Scientific Language**: Professional, academic tone
- **Evidence-Based**: Specific quotes from title/abstract/keywords
- **Contextual Reasoning**: Explain WHY something qualifies
- **Conceptual Understanding**: Recognize implicit relationships
- **Consistent Methodology**: Apply same standards across all documents

## Technical Implementation

### Core Files
- `intelligent_processor.js`: Main analysis engine with multi-language support
- `batch_pure_processor.js`: Batch processing for entire PDF collection
- Enhanced keyword patterns based on DSS4ES search string translations
- Intelligent interpretation logic with contextual understanding

### Validation Benchmarks
- **Hiltner_NaiS_Steinschlagprofil_Bericht_update_final.pdf**: Include (modeling + forest + management + BES + decision support)
- **187_Thrippleton.pdf**: Include (multi-criteria decision support system)
- **257_Hiltner.pdf**: Include (optimization + forest protection + management)
- **bericht-transportkosten...pdf**: Exclude (economics focus, no ecosystem modeling)

## Error Handling
- Document processing failures with specific error messages
- Handle multi-language content extraction issues
- Flag documents with insufficient extractable content
- Maintain processing logs for quality assurance

## Success Metrics
- **Accuracy**: Results match expert manual screening judgments
- **Consistency**: Same standards applied across all documents
- **Completeness**: All PDFs processed or errors documented
- **Quality**: Intelligent explanations provide clear scientific reasoning

This enhanced approach combines computational efficiency with human-level interpretation quality for systematic literature review in forest ecosystem science.
