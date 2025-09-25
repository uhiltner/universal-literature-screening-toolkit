# Universal Literature Screening Toolkit — Comprehensive User Guide

Complete documentation for researchers and students using the Universal Literature Screening Toolkit v2.1 (query-first workflow).

---

## 📚 Table of Contents

1. [Introduction](#introduction)
2. Installation & Setup
3. Testing Your Installation
4. Basic Usage (query.txt)
5. Boolean Query Syntax and Tips
6. Advanced Configuration
7. Understanding Results
8. Troubleshooting
9. Research Workflows
10. FAQ

---

## Introduction

The Universal Literature Screening Toolkit automates the initial screening phase of systematic literature reviews. Instead of manually reading hundreds of abstracts, you write one Boolean query and let the toolkit identify papers that meet your inclusion criteria.

### What It Does
- **Extracts text** from PDF papers (title, abstract, keywords)
- **Applies search criteria** via a Boolean query (AND/OR/NOT, parentheses, phrases, wildcards)
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
python -m pytest tests -q
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
# Run comprehensive test suite
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
[ OK ] All tests passed successfully!
[ OK ] All tests passed successfully! ✅
```

*Note: The 5 warnings are harmless PyMuPDF deprecation warnings - your installation is perfect!*

---

## Basic Usage (query-first)

### Step 1: Prepare Your PDFs
```
input_pdfs/
├── paper1.pdf
├── paper2.pdf
├── paper3.pdf
└── ...
```

### Step 2: Define Search Criteria as a Boolean query
Create a file named `query.txt` with one Boolean expression (lines starting with `#` are comments and ignored):

```
# Example: AI in clinical context; include study designs; exclude purely economic papers
("artificial intelligence" OR "machine learning" OR "deep learning")
AND (healthcare OR medical* OR clinical)
AND ("systematic review" OR "randomized controlled trial" OR meta-analysis)
AND NOT (economics OR cost*)
```

### Step 3: Run Screening

#### Windows (PowerShell)
```powershell
# Use defaults (input_pdfs → results) with query file
.\scripts\run_tool.ps1 -QueryFile "query.txt"

# Custom paths
.\scripts\run_tool.ps1 -InputPath "my_pdfs" -OutputPath "my_results" -QueryFile "my_query.txt"
```

#### Cross-Platform (macOS/Linux)
```bash
# Unix/Linux/macOS
./scripts/run_tool.sh --input input_pdfs --output results --query-file query.txt

# Manual execution
python run_screening.py --input input_pdfs --output results --query-file query.txt
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

## Boolean Query Syntax and Tips

- Operators: NOT > AND > OR
- Parentheses group sub-expressions: (A OR B) AND C
- Phrases: use double quotes, e.g., "ecosystem services"
- Wildcards: trailing asterisk expands variations, e.g., model* matches model, models, modeling, modelling
- Comments: lines starting with # are ignored in query files

Examples:

- Core + context: (forest* OR woodland*) AND (management OR planning)
- Include BES concept, exclude economics: ("ecosystem service*" OR biodiversity) AND NOT economics

Deprecation note: The legacy block-based --search-terms mode is still available for one transition release but will be removed. When using --query-file, validation_logic in config.json is ignored.

## Advanced Configuration

### Configuration File (config.json)

#### Validation Logic (legacy)

If you use --query-file, this section does not apply. For legacy --search-terms users only, see prior versions of the guide.

#### Domain Customization
```json
{
  "domain_info": {
    "research_area": "Medical AI Literature Review",
    "description": "Systematic review of AI applications in healthcare",
    "version": "0.90.0"
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

## Search Terms Guide (legacy)

This section described the legacy block-based format and is retained only for transition. New users should prefer Boolean queries with --query-file.

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
| Paper | Result | Matched | Details |
|-------|--------|---------|---------|
| paper1.pdf | ✅ INCLUDED | forest*, management | Evidence snippet in abstract |
| paper2.pdf | ❌ EXCLUDED | — | — |

#### Query Summary
When running in query mode, the report shows your original query string and a compact AST view for traceability.

### JSON Data Structure
```json
[
  {
    "filename": "paper1.pdf",
    "included": true,
    "evidence": {
      "forest": ["…forest management…"],
      "ecosystem service*": ["…ecosystem services…"]
    }
  }
]
```

### Interpreting Results

#### High Inclusion Rate (>50%)
- **Possible Issue**: Search criteria too broad
- **Solution**: Add more specific terms or use AND logic
- **Check**: Review excluded papers for false negatives

#### Low Inclusion Rate (<5%)
- **Possible Issue**: Query too restrictive  
- **Solution**: Add OR synonyms, use wildcards, remove NOT terms
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
- **Tighten query**: Add AND conditions, remove very broad terms
- **Use phrases**: Quote multi-word concepts

---

## Research Workflows

### 1. Exploratory Phase
**Goal**: Understand literature landscape

```powershell
# Start broad, inclusive query with OR logic
# Example:
(your_topic* OR related_term* OR synonym*)

# Run screening
.\scripts\run_tool.ps1

# Analyze results to refine criteria
```

### 2. Focused Screening
**Goal**: Systematic inclusion/exclusion

```powershell
# Refine with AND logic
# Example:
("exact term" OR specific_concept*) AND ("study design" OR method* OR approach*) AND (target_population* OR specific_domain*)

# Run final screening
.\scripts\run_tool.ps1
```

### 3. Validation Workflow
**Goal**: Verify screening accuracy

```bash
# 1. Run screening (Windows example)
.\scripts\run_tool.ps1 -QueryFile query.txt

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
A: Tested with 100+ papers. Processing time scales linearly (~1-2 seconds per paper).

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

*This guide covers the complete functionality of the Universal Literature Screening Toolkit v0.90.0. For the latest updates and community contributions, visit the [GitHub repository](https://github.com/uhiltner/universal-literature-screening-toolkit).*