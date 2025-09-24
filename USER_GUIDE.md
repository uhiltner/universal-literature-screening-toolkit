# Universal Literature Screening Toolkit - Comprehensive User Guide

*Complete documentation for researchers and students using the Universal Literature Screening Toolkit v2.0*

---

## 📚 Table of Contents

1. [Introduction](#introduction)
2. [Installation & Setup](#installation--setup)
3. [Testing Your Installation](#testing-your-installation)
4. [Basic Usage](#basic-usage)
5. [Advanced Configuration](#advanced-configuration)
6. [Search Terms Guide](#search-terms-guide)
7. [Understanding Results](#understanding-results)
8. [Troubleshooting](#troubleshooting)
9. [Research Workflows](#research-workflows)
10. [FAQ](#frequently-asked-questions)

---

## Introduction

The Universal Literature Screening Toolkit automates the initial screening phase of systematic literature reviews. Instead of manually reading hundreds of abstracts, you define search criteria and let the toolkit identify papers that meet your inclusion criteria.

### What It Does
- **Extracts text** from PDF papers (title, abstract, keywords)
- **Applies search criteria** using configurable logic (AND/OR)
- **Generates professional reports** with validation results
- **Organizes papers** into include/exclude folders
- **Saves time** - process hundreds of papers in minutes

### What It Doesn't Do
- **Full-text analysis** (focuses on abstracts for screening speed)
- **Quality assessment** (that's the next step in your review)
- **Citation analysis** (use dedicated tools like Zotero)

---

## Installation & Setup

### Quick Setup (Recommended)

#### Windows Users
```powershell
# 1. Open PowerShell and navigate to toolkit folder
cd path\to\universal-literature-screening-toolkit

# 2. Allow scripts for this session
Set-ExecutionPolicy Bypass -Scope Process

# 3. Run automated setup (creates isolated environment)
.\scripts\setup_windows.ps1

# 4. Test installation
.\scripts\run_tests.ps1
```

#### macOS/Linux Users
```bash
# 1. Make scripts executable (first time only)
chmod +x scripts/setup_unix.sh scripts/run_tool.sh scripts/run_tests.sh

# 2. Run automated setup
./scripts/setup_unix.sh

# 3. Test installation  
./scripts/run_tests.ps1  # Use Python equivalent if no PowerShell
```

### Manual Setup (Alternative)
If you prefer manual control or the scripts don't work:

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows: venv\Scripts\activate
# Unix: source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Test manually
python -m pytest tests/ -v
```

---

## Testing Your Installation

**Always test your installation before starting research!**

### Windows Testing
```powershell
# Run comprehensive test suite (38 tests)
.\scripts\run_tests.ps1

# Run with detailed output
.\scripts\run_tests.ps1 -Verbose

# Test specific components
.\scripts\run_tests.ps1 -Specific test_pdf_extractor.py -Verbose
```

### What Tests Cover
- **PDF text extraction** (PyMuPDF and pdfplumber libraries)
- **Search term parsing** (wildcards, quoted phrases, regex)
- **Validation logic** (AND/OR operators, block combinations)
- **Report generation** (HTML and JSON outputs)
- **Error handling** (corrupt files, missing data)

### Expected Results
```
============ 38 passed, 5 warnings in 1.96s =============
[ OK ] All tests passed successfully! ✅
```

*Note: The 5 warnings are harmless PyMuPDF deprecation warnings - your installation is perfect!*

---

## Basic Usage

### Step 1: Prepare Your PDFs
```
input_pdfs/
├── paper1.pdf
├── paper2.pdf
├── paper3.pdf
└── ...
```

### Step 2: Define Search Criteria
Edit `search_terms.txt`:
```
BLOCK 1: Core Concept
artificial intelligence, machine learning, "deep learning"

BLOCK 2: Application Domain  
healthcare, medical*, clinical

BLOCK 3: Study Type
systematic review, meta-analysis, "randomized controlled trial"
```

### Step 3: Run Screening

#### Windows (Recommended)
```powershell
# Use defaults (input_pdfs → results)
.\scripts\run_tool.ps1

# Custom paths
.\scripts\run_tool.ps1 -InputPath "my_pdfs" -OutputPath "my_results" -SearchTermsPath "my_terms.txt"

# JSON extraction only (no PDF processing)
.\scripts\run_tool.ps1 -JsonOnly
```

#### Cross-Platform
```bash
# Unix/Linux/macOS
./scripts/run_tool.sh input_pdfs results search_terms.txt config.json

# Manual execution
python run_screening.py --input input_pdfs --output results --search-terms search_terms.txt
```

### Step 4: Review Results
```
results/
├── validation_report.html      # Open in web browser
├── validation_results.json     # Raw data
└── sorted_pdfs/
    ├── include/               # Papers meeting criteria
    └── exclude/               # Papers not meeting criteria
```

---

## Advanced Configuration

### Configuration File (config.json)

#### Validation Logic
```json
{
  "validation_logic": {
    "default_operator": "AND",    // "AND" | "OR"
    "block_combinations": {
      "blocks": ["Block 3A", "Block 3B"],
      "operator": "OR",
      "combined_name": "Combined Ecosystem Services"
    }
  }
}
```

**Understanding Logic:**
- **AND**: Paper must match ALL blocks (stricter)
- **OR**: Paper must match ANY block (more inclusive)
- **Block Combinations**: Special rules for specific blocks

#### Domain Customization
```json
{
  "domain_info": {
    "research_area": "Medical AI Literature Review",
    "description": "Systematic review of AI applications in healthcare",
    "version": "1.0"
  }
}
```

#### Text Processing Options
```json
{
  "text_processing": {
    "case_sensitive": false,      // Usually false for screening
    "whole_word_matching": true,  // Prevents partial matches
    "encoding": "utf-8"          // Handles international text
  }
}
```

---

## Search Terms Guide

### Basic Syntax
```
BLOCK 1: Block Name
term1, term2, term3
```

### Advanced Patterns

#### Wildcards (*)
```
BLOCK 1: Technology Terms
comput*, algorith*, automat*
```
*Matches: computer, computing, computational, algorithm, algorithms, automate, automation, etc.*

#### Exact Phrases
```
BLOCK 2: Study Methods
"systematic review", "randomized controlled trial", "meta analysis"
```
*Matches: Only exact phrases, not individual words*

#### Combined Patterns
```
BLOCK 3: Mixed Terms
"artificial intelligence", machine learning, AI, neural network*
```

### Domain-Specific Examples

#### Medical Research
```
BLOCK 1: Medical Condition
diabetes*, "type 2 diabetes", "diabetes mellitus", diabetic*

BLOCK 2: Intervention
treatment*, therapy*, intervention*, medication*, drug*

BLOCK 3: Study Design
"randomized controlled trial", "clinical trial", "cohort study", RCT
```

#### Environmental Science
```
BLOCK 1: Environmental Context
climate*, ecosystem*, biodiversity*, environment*

BLOCK 2: Impact Assessment
impact*, effect*, consequence*, change*, variation*

BLOCK 3: Geographic Scale
global*, regional*, local*, landscape*, catchment*
```

#### Technology Research
```
BLOCK 1: Technology
"artificial intelligence", "machine learning", "deep learning", AI, ML

BLOCK 2: Application
healthcare, medical*, clinical*, diagnostic*, therapeutic*

BLOCK 3: Validation
performance*, accuracy*, precision*, recall*, validation*
```

---

## Understanding Results

### HTML Report Sections

#### Summary Statistics
```
📊 Screening Results Summary
Total Papers Analyzed: 150
✅ Included: 23 (15.3%)
❌ Excluded: 127 (84.7%)
```

#### Detailed Results Table
| Paper | Result | Blocks Passed | Details |
|-------|---------|---------------|---------|
| paper1.pdf | ✅ INCLUDED | 3/3 | All blocks matched |
| paper2.pdf | ❌ EXCLUDED | 1/3 | Missing Block 2, Block 3 |

#### Block Performance
```
🎯 Search Block Results
Block 1 (Core Concept): 89 matches (59.3%)
Block 2 (Application): 45 matches (30.0%)
Block 3 (Study Type): 34 matches (22.7%)
```

### JSON Data Structure
```json
[
  {
    "filename": "paper1.pdf",
    "overall_result": true,
    "blocks_passed": 3,
    "total_blocks": 3,
    "block_results": [
      {
        "block_name": "Block 1: Core Concept",
        "passed": true,
        "matches_found": 5,
        "sample_matches": ["artificial intelligence", "machine learning"]
      }
    ]
  }
]
```

### Interpreting Results

#### High Inclusion Rate (>50%)
- **Possible Issue**: Search criteria too broad
- **Solution**: Add more specific terms or use AND logic
- **Check**: Review excluded papers for false negatives

#### Low Inclusion Rate (<5%)
- **Possible Issue**: Search criteria too restrictive  
- **Solution**: Add synonyms, use OR logic, check spelling
- **Check**: Review included papers for relevance

#### Ideal Range: 10-30%
- **Balanced criteria** that capture relevant papers
- **Efficient screening** without missing important work
- **Ready for manual review** of included papers

---

## Troubleshooting

### Installation Issues

#### "Python not found"
```powershell
# Check Python installation
python --version
# or
py --version

# If not found, install from python.org
# Make sure "Add to PATH" is checked during installation
```

#### "pip not recognized"
```powershell
# Re-run setup to fix pip
.\scripts\setup_windows.ps1

# Or manually repair
C:\uls_env\Scripts\python.exe -m ensurepip --upgrade
```

#### "Execution Policy" errors
```powershell
# Allow scripts for current session only
Set-ExecutionPolicy Bypass -Scope Process

# Then re-run setup
.\scripts\setup_windows.ps1
```

### Processing Issues

#### "No PDFs found"
- Check `input_pdfs` folder exists
- Verify PDFs are directly in folder (not subfolders)
- Ensure files have `.pdf` extension

#### "Text extraction failed"
- **Some PDFs are scanned images**: Use OCR tools first
- **Encrypted PDFs**: Remove password protection
- **Corrupt PDFs**: Check file integrity

#### "No matches found"
- **Check spelling** in search terms
- **Too restrictive**: Try OR logic instead of AND
- **Add synonyms**: Include alternative terminology
- **Use wildcards**: `treat*` instead of `treatment`

### Result Issues

#### "All papers excluded"
- **Review search terms**: May be too specific
- **Check sample papers manually**: Verify they should match
- **Try broader terms**: Add synonyms and variations
- **Use OR logic**: In config.json, set default_operator to "OR"

#### "Too many papers included"
- **Add more blocks**: Increase specificity
- **Use AND logic**: Require all blocks to match
- **Refine terms**: Remove overly broad terms

---

## Research Workflows

### 1. Exploratory Phase
**Goal**: Understand literature landscape

```powershell
# Use broad, inclusive criteria with OR logic
# config.json: "default_operator": "OR"

# Example search terms:
BLOCK 1: Core Topic
your_topic*, related_term*, synonym*

# Run screening
.\scripts\run_tool.ps1

# Analyze results to refine criteria
```

### 2. Focused Screening
**Goal**: Systematic inclusion/exclusion

```powershell
# Use refined criteria with AND logic
# config.json: "default_operator": "AND"

# Example search terms:
BLOCK 1: Core Concept (specific)
"exact term", specific_concept*

BLOCK 2: Methodology
"study design", method*, approach*

BLOCK 3: Population/Domain
target_population*, specific_domain*

# Run final screening
.\scripts\run_tool.ps1
```

### 3. Validation Workflow
**Goal**: Verify screening accuracy

```bash
# 1. Run screening
.\scripts\run_tool.ps1

# 2. Manually review random sample of included papers
# 3. Manually review random sample of excluded papers
# 4. Calculate precision/recall if needed
# 5. Adjust criteria if necessary and re-run
```

### 4. Multi-Database Integration
**Goal**: Combine results from multiple sources

```
databases/
├── pubmed_pdfs/
├── scopus_pdfs/
├── web_of_science_pdfs/
└── results/
    ├── pubmed_results/
    ├── scopus_results/
    └── combined_results/
```

```powershell
# Screen each database separately
.\scripts\run_tool.ps1 -InputPath "databases/pubmed_pdfs" -OutputPath "databases/pubmed_results"
.\scripts\run_tool.ps1 -InputPath "databases/scopus_pdfs" -OutputPath "databases/scopus_results"

# Combine results manually or with custom scripts
```

---

## Frequently Asked Questions

### General Usage

**Q: How many papers can the toolkit handle?**
A: Tested with 1000+ papers. Processing time scales linearly (~1-2 seconds per paper).

**Q: What file formats are supported?**
A: PDF only. For other formats, convert to PDF first.

**Q: Can I use this for non-English papers?**
A: Yes! The toolkit handles Unicode text in any language.

**Q: How accurate is the screening?**
A: Accuracy depends on your search criteria. Well-designed terms achieve 90%+ precision.

### Technical Questions

**Q: What's the difference between PyMuPDF and pdfplumber?**
A: Both extract PDF text. PyMuPDF is faster; pdfplumber is more robust for complex layouts.

**Q: Can I modify the source code?**
A: Yes! The toolkit is MIT licensed. See CONTRIBUTING.md for guidelines.

**Q: How do I cite this toolkit?**
A: See the Citation section in README.md or CITATION.cff file.

### Research Process

**Q: Should I use AND or OR logic?**
A: 
- **AND**: Stricter, fewer false positives, good for final screening
- **OR**: More inclusive, fewer false negatives, good for initial screening

**Q: How do I handle duplicate papers?**
A: Run duplicate detection before screening using tools like Zotero or Mendeley.

**Q: What about grey literature?**
A: Works with any PDFs. Ensure consistent formatting across sources.

**Q: How do I validate my search strategy?**
A: 
1. Test with known relevant papers
2. Manual review of random samples
3. Compare with expert manual screening
4. Calculate inter-rater agreement

### Best Practices

**Q: How many search blocks should I use?**
A: 3-7 blocks typically work well. Too few = overly broad; too many = overly restrictive.

**Q: Should I include methodology terms?**
A: Yes, if methodology is part of your inclusion criteria (e.g., "randomized controlled trial").

**Q: How do I handle abbreviations?**
A: Include both full terms and abbreviations: `"artificial intelligence", AI, "machine learning", ML`

**Q: What about case sensitivity?**
A: Keep case_sensitive: false (default) for most research applications.

---

## Support & Community

### Getting Help
1. **Check this guide** for comprehensive solutions
2. **Review troubleshooting section** for common issues  
3. **Run tests** to verify installation: `.\scripts\run_tests.ps1`
4. **Open GitHub issue** for bugs or feature requests
5. **Check examples folder** for domain-specific templates

### Contributing
- **Bug reports**: Use GitHub issues with error messages
- **Feature requests**: Describe your research use case
- **Code contributions**: See CONTRIBUTING.md
- **Documentation**: Help improve this guide

### Academic Use
- **Cite the toolkit** in your publications (see CITATION.cff)
- **Share search strategies** with the community
- **Report validation studies** to improve the tool
- **Collaborate** on domain-specific templates

---

*This guide covers the complete functionality of the Universal Literature Screening Toolkit v2.0. For the latest updates and community contributions, visit the [GitHub repository](https://github.com/uhiltner/universal-literature-screening-toolkit).*