# Universal Literature Screening Toolkit — Comprehensive User Guide

**Welcome to the complete guide!** This documentation is designed for researchers at all skill levels, from complete beginners to advanced users.

**Version:** 1.0.2  
**Last Updated:** October 2025

---

## 📚 Table of Contents

**Getting Started** (For Beginners)
1. [Introduction](#introduction) - What this toolkit does and why you need it
2. [Installation & Setup](#installation--setup) - Get the toolkit running on your computer
3. [Testing Your Installation](#testing-your-installation) - Make sure everything works
4. [Basic Usage](#basic-usage-query-first) - Screen your first batch of papers

**Core Features** (For All Users)
5. [Boolean Query Syntax and Tips](#boolean-query-syntax-and-tips) - Master search queries
6. [Refining Search Strings](#refining-search-strings) - Fix common problems with your searches
7. [Understanding Results](#understanding-results) - Interpret your screening reports

**Advanced Topics**
8. [Advanced Configuration](#advanced-configuration) - Customize the toolkit
9. [Research Workflows](#research-workflows) - Real-world screening strategies
10. [Troubleshooting](#troubleshooting) - Solve technical problems
11. [FAQ](#frequently-asked-questions) - Quick answers to common questions

---

## Introduction

### What Does This Toolkit Do?

The Universal Literature Screening Toolkit **automates the tedious first step of systematic literature reviews**. Instead of manually reading hundreds or thousands of research paper abstracts one by one, you:

1. **Write a search query once** (like "show me papers about forests AND climate change")
2. **Run the toolkit** (it reads all your PDFs automatically)
3. **Get organized results** (papers sorted into include/exclude folders with a detailed report)

**In plain English:** This toolkit is like having a research assistant who can read 100 papers in 2 minutes and tell you which ones match your criteria.

### What It DOES Do ✅

1. **Extracts text from PDFs**
   - Reads the title, abstract, and keywords from each research paper
   - Works with most standard PDF files
   
2. **Applies your search criteria**
   - Uses Boolean logic (AND/OR/NOT) like advanced database searches
   - Supports wildcards (`forest*`), exact phrases (`"climate change"`), and complex combinations
   
3. **Creates clear reports**
   - Shows you exactly which papers matched and why
   - Provides evidence snippets from each paper
   - Generates both HTML (easy to read) and JSON (for data analysis)
   
4. **Organizes your papers**
   - Automatically sorts PDFs into "include" and "exclude" folders
   - Keeps your original files safe and unchanged
   
5. **Saves massive amounts of time**
   - Process 100 papers in 2-3 minutes instead of several hours
   - Consistent, objective application of your criteria

### What It DOESN'T Do ❌

1. **Full-text deep analysis**
   - Focuses on abstracts and key sections for speed
   - Not designed to read entire 50-page papers
   
2. **Quality assessment of research**
   - Doesn't judge if a study is "good" or "bad"
   - You still need to critically evaluate included papers
   
3. **Citation network analysis**
   - Use dedicated tools like Zotero, Mendeley, or Covidence for reference management
   
4. **Replace human judgment**
   - Automated screening is the first step, not the final decision
   - Always manually review your included papers

---

## Installation & Setup

**Good news:** Installation is straightforward and only takes about 5 minutes. We've created automated scripts that do most of the work for you.

**What you'll need:**
- A computer (Windows, macOS, or Linux)
- Internet connection (for downloading software)
- About 500 MB of free disk space

### Quick Setup (Recommended for Beginners)

#### Windows Users

**Follow these steps exactly:**

```powershell
# Step 1: Open PowerShell
#   Press Windows Key + X, then select "Windows PowerShell"

# Step 2: Navigate to toolkit folder (replace YourName with your username)
cd C:\Users\YourName\Downloads\universal-literature-screening-toolkit

# Step 3: Allow the script to run (this is safe - only affects this window)
Set-ExecutionPolicy Bypass -Scope Process

# Step 4: Run automated setup (installs Python environment and all needed software)
.\scripts\setup_windows.ps1

# Step 5: Test that everything works
.\scripts\run_tests.ps1
```

**What happens during setup:**
- Creates an isolated Python environment (won't affect other programs)
- Installs PDF processing libraries
- Sets up the testing framework
- Takes 2-3 minutes total

**Success looks like:**
You'll see `✅ All tests passed successfully!` at the end.

#### macOS/Linux Users

**Follow these steps exactly:**

```bash
# Step 1: Open Terminal
#   macOS: Press Cmd+Space, type "Terminal", press Enter
#   Linux: Press Ctrl+Alt+T

# Step 2: Navigate to toolkit folder
cd ~/Downloads/universal-literature-screening-toolkit

# Step 3: Make scripts executable (first time only)
chmod +x scripts/setup_unix.sh scripts/run_tool.sh scripts/run_tests.sh

# Step 4: Run automated setup
./scripts/setup_unix.sh

# Step 5: Test installation  
python3 -m pytest tests -q
```

**What happens during setup:**
- Creates an isolated Python environment
- Installs PDF processing libraries  
- Sets up the testing framework
- Takes 2-3 minutes total

**Success looks like:**
You'll see test results with no errors.

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

**Why test?** Testing ensures everything is installed correctly before you start working with your actual research papers. It only takes 30 seconds!

### Running Tests

**Windows Testing:**
```powershell
# Basic test (recommended for beginners)
.\scripts\run_tests.ps1

# Detailed output (if you want to see everything)
.\scripts\run_tests.ps1 -Verbose
```

**macOS/Linux Testing:**
```bash
# Basic test
python3 -m pytest tests -q

# Detailed output
python3 -m pytest tests -v
```

### What Gets Tested

The test suite checks that all major components work correctly:

1. **PDF Text Extraction**
   - Tests the ability to read text from PDF files
   - Checks both primary (PyMuPDF) and backup (pdfplumber) methods
   
2. **Search Query Processing**
   - Verifies wildcards work (`forest*` matching `forest`, `forests`, etc.)
   - Tests exact phrases (`"climate change"`)
   - Checks Boolean operators (AND, OR, NOT)
   
3. **Validation Logic**
   - Ensures papers are correctly classified as include/exclude
   - Tests complex query combinations
   
4. **Report Generation**
   - Confirms HTML and JSON files are created properly
   - Checks that evidence snippets appear correctly
   
5. **Error Handling**
   - Tests behavior with corrupted files
   - Checks handling of missing or incomplete data

### What Success Looks Like

**Windows:**
```
✅ All tests passed successfully!
```

**macOS/Linux:**
```
===================== test session starts ======================
collected 25 items

tests/test_pdf_extractor.py .....                        [ 20%]
tests/test_validator.py .........                         [ 56%]
tests/test_report_generator.py .....                     [ 76%]
tests/test_toolkit.py ......                             [100%]

===================== 25 passed in 3.2s ======================
```

**Don't worry about warnings!** You might see 5-10 warnings about PyMuPDF deprecation. These are harmless - the toolkit still works perfectly. Warnings are not errors.

**If tests fail:** See the [Troubleshooting](#troubleshooting) section below.

---

## Basic Usage (Query-First)

**This is the heart of the toolkit!** Follow these 4 simple steps to screen your papers.

### Step 1: Prepare Your PDFs

**Create the input folder:**

Create a folder called `input_pdfs` in the same location as `run_screening.py`:

**Windows:**
```powershell
New-Item -ItemType Directory -Name "input_pdfs" -Force
```

**macOS/Linux:**
```bash
mkdir -p input_pdfs
```

**Add your PDF files:**

Copy all your research paper PDFs into this folder. The structure should look like:

```
input_pdfs/
├── paper1.pdf
├── paper2.pdf
├── paper3.pdf
└── ...
```

**Important:**
- ✅ Files can have any names
- ✅ Put all PDFs directly in `input_pdfs` (no subfolders)
- ✅ Works with any number of PDFs (tested with 100+)

### Step 2: Write Your Search Query

**Create a file named `query.txt` in the toolkit folder** (same place as `run_screening.py`).

**What is a query?** Think of it like a Google search, but more powerful. You're telling the toolkit exactly what to look for in each paper.

**Simple example:**
```
forest* AND climate*
```
This finds papers that mention both "forest" (or forests, forestry, etc.) AND "climate" (or climatic, etc.)

**Real-world example for a systematic review:**
```
# My systematic review on forest ecosystem services
# Lines starting with # are comments and are ignored

(forest* OR woodland* OR silvicultur*) 
AND 
("ecosystem service*" OR biodiversity OR "natural capital") 
AND NOT 
(economics OR cost-benefit)
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
    "version": "1.0.2"
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

## Refining Search Strings

One of the most common challenges in systematic literature screening is getting the search query "just right". Too broad and you'll spend hours manually reviewing irrelevant papers. Too narrow and you'll miss important work. This section provides practical strategies for refining your queries based on your initial results.

### Dealing with No Matches (0% inclusion)

**Symptom**: Your screening returns 0 or very few included papers (< 5%).

**Common Causes**:
1. Query is too restrictive (too many AND conditions)
2. Missing synonyms or variations of key terms
3. NOT clauses eliminating relevant papers
4. Exact phrases that don't match actual paper wording

**Solutions to Try** (in order):

1. **Add Synonyms with OR Logic**
   ```
   # Before (too narrow)
   forest AND management
   
   # After (more inclusive)
   (forest* OR woodland* OR silvicultur* OR forestry) AND (management OR planning OR governance)
   ```

2. **Use Wildcards Liberally**
   ```
   # Before
   model AND simulation
   
   # After
   model* AND simulat*
   # Matches: model, models, modeling, modelling, simulate, simulation, simulations
   ```

3. **Remove NOT Clauses Temporarily**
   ```
   # Before
   forest* AND management AND NOT economics
   
   # After (test without NOT first)
   forest* AND management
   # Then manually filter economics papers if needed
   ```

4. **Replace Exact Phrases with Flexible Terms**
   ```
   # Before (too specific)
   "climate adapted management" AND "ecosystem services"
   
   # After (more flexible)
   (climate* AND adapt* AND management) AND (ecosystem* AND service*)
   ```

5. **Test Individual Concepts First**
   ```
   # Step 1: Test each concept separately
   forest*                          # Should match most papers
   management                       # Should match many papers
   "ecosystem service*"             # Test this specific phrase
   
   # Step 2: Combine concepts that work
   (forest*) AND (management OR planning)
   ```

### Dealing with Too Many Matches (>80% inclusion)

**Symptom**: Your screening includes almost everything (> 80% inclusion rate).

**Common Causes**:
1. Query is too broad (too many OR conditions, not enough AND)
2. Very general terms that match almost any paper
3. Missing specificity for your research question

**Solutions to Try** (in order):

1. **Add More AND Conditions**
   ```
   # Before (too broad)
   forest* OR management
   
   # After (more specific)
   forest* AND management AND ("ecosystem service*" OR biodiversity)
   ```

2. **Use Exact Phrases for Precise Concepts**
   ```
   # Before
   carbon AND offset
   
   # After
   "carbon offset*" AND ("voluntary market*" OR "carbon credit*")
   ```

3. **Add Methodological Requirements**
   ```
   # Before
   forest* AND management
   
   # After
   forest* AND management AND ("systematic review" OR "meta-analysis" OR "randomized controlled trial")
   ```

4. **Add NOT Clauses for Common False Positives**
   ```
   # Before
   forest* AND management
   
   # After
   forest* AND management AND NOT (furniture OR timber OR wood* AND product*)
   ```

5. **Narrow to Specific Contexts**
   ```
   # Before
   biodiversity
   
   # After
   biodiversity AND (tropical OR rainforest OR "cloud forest") AND conservation
   ```

### Adapting Queries for Domain-Specific Literature

**The Swiss Grey Literature Problem** (Based on real user feedback):

**Scenario**: Mirko was searching for Swiss grey literature about voluntary carbon offset markets in forests. His query included explicit requirements for "voluntary offset market*" terms, but Swiss documents often assume this context implicitly and don't state it explicitly.

**Original Query** (too restrictive for Swiss context):
```
(forest*) AND 
(IFM OR "improved forest management" OR reserve OR "adapted management") AND 
("voluntary offset market*" OR "voluntary offset*" OR "voluntary market*") AND 
(quantification* OR baseline* OR additionality)
```

**Problem**: Swiss regulations and reports discuss carbon offsets in forests but don't always use "voluntary" because it's understood in their context.

**Solutions**:

1. **Create Domain-Specific Variants**
   ```
   # Generic International Query
   (forest*) AND ("voluntary carbon*" OR "carbon credit*") AND quantification*
   
   # Swiss-Adapted Query (remove "voluntary" requirement)
   (forest*) AND (carbon AND (offset* OR credit* OR "Zertifikat*")) AND (quantification* OR baseline*)
   ```

2. **Use Language-Specific Terms**
   ```
   # Add German/French/Italian terms for Swiss context
   (forest* OR Wald* OR "forêt*" OR "foresta*") AND 
   (carbon OR CO2 OR Kohlenstoff OR carbone) AND 
   (offset* OR Zertifikat* OR "crédit carbone")
   ```

3. **Make Implicit Concepts Explicit with OR**
   ```
   # Before (requires explicit mention)
   "voluntary carbon market*"
   
   # After (allows implicit or explicit)
   ("voluntary carbon market*" OR "carbon credit*" OR "offset* project*" OR climate* AND financ*)
   ```

4. **Test with Known Relevant Papers First**
   - Take 3-5 Swiss papers you know should be included
   - Run your query and check if they match
   - If not, examine which terms are missing and adjust

5. **Regional vs. Global Queries**
   ```
   # Strategy: Create separate queries for different literature types
   
   # Query A: International peer-reviewed (strict)
   (forest*) AND ("voluntary carbon market*") AND quantification* AND additionality
   
   # Query B: Swiss grey literature (relaxed)
   (Wald* OR forest*) AND (CO2 OR carbon) AND (Zertifikat* OR credit* OR offset*)
   ```

### General Refinement Strategies

**Strategy 1: Iterative Refinement**
```
Run 1: Broad query → Review results → Identify patterns
Run 2: Add specificity → Review again → Adjust
Run 3: Final query → Full screening
```

**Strategy 2: Benchmark with Known Papers**
1. Collect 10-20 papers you *know* should be included
2. Test your query against these benchmarks
3. If <80% of benchmarks match, refine the query
4. Iterate until 90%+ benchmark coverage

**Strategy 3: Pilot Testing**
1. Create a small test set (~20-30 diverse papers)
2. Run multiple query variants
3. Manually review results to see which query works best
4. Apply winning query to full dataset

**Strategy 4: Consult Domain Experts**
- Ask field experts: "What key terms would YOU search for?"
- Review existing systematic reviews in your field
- Check their search strategies and adapt

### When to Stop Refining

**Good Signs** (query is ready):
- Inclusion rate: 10-40% (balanced)
- Manual review of included papers: >85% truly relevant
- Manual review of excluded papers: >90% correctly excluded
- Query matches your known benchmark papers

**Warning Signs** (keep refining):
- <5% or >80% inclusion rate
- Many obviously irrelevant papers included
- Known relevant papers are excluded
- Colleagues disagree with screening results

### Pro Tips

1. **Document Your Refinement Process**: Keep notes on what you tried and why. This is important for the "Methods" section of your systematic review paper.

2. **Version Your Queries**: Save each iteration as `query_v1.txt`, `query_v2.txt`, etc. This creates an audit trail.

3. **Test Edge Cases**: Make sure your query handles:
   - Hyphenated terms: `eco-system` vs `ecosystem`
   - Plural variations: `service` vs `services`
   - British/American spelling: `analyse` vs `analyze`

4. **Balance Precision and Recall**: You'll never get 100% of both. Decide what's more important for your review:
   - High precision (few false positives) → Stricter query with AND
   - High recall (few false negatives) → Broader query with OR

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

#### ❌ "Python not found" or "'python' is not recognized"

**Cause:** Python not installed or not in PATH

**Solutions:**
```powershell
# Check if Python is installed
python --version
# or try
py --version
```

If neither works:
1. Download Python from [python.org](https://www.python.org/downloads/)
2. During installation, **check "Add Python to PATH"** (very important!)
3. Restart PowerShell/Terminal completely
4. Try `py --version` instead of `python --version`

#### ❌ "pip not recognized" or "pip not found"

**Cause:** pip not installed or environment issues

**Solutions:**
```powershell
# Re-run setup script (fixes pip automatically)
.\scripts\setup_windows.ps1

# Or manually repair pip
C:\uls_env\Scripts\python.exe -m ensurepip --upgrade
```

#### ❌ "Execution Policy" error in PowerShell

**Cause:** Windows blocks unsigned scripts by default for security

**Solution:**
```powershell
# Allow scripts for current session only (safe)
Set-ExecutionPolicy Bypass -Scope Process

# Then re-run setup
.\scripts\setup_windows.ps1
```

**Note:** This only affects the current PowerShell window and doesn't change system-wide security settings.

#### ❌ Setup script fails or hangs

**Solutions:**
1. Close all PowerShell/Terminal windows
2. Delete the `uls_env` folder if it exists
3. Re-run the setup script
4. Check internet connection (needed for downloading packages)

---

### Folder and File Issues

#### ❌ "No PDFs found in input_pdfs"

**Check these:**
- ✅ Folder is named exactly `input_pdfs` (not `Input_PDFs`, `input-pdfs`, or `InputPDFs`)
- ✅ PDFs are directly in the folder (not in a subfolder)
- ✅ Files have `.pdf` extension (not `.PDF`, `.pdf.txt`, or other extensions)
- ✅ Folder is in the same directory as `run_screening.py`

**Example of correct structure:**
```
universal-literature-screening-toolkit/
├─ run_screening.py
├─ input_pdfs/              ← Must be exactly this name
│  ├─ paper1.pdf           ← PDFs directly here
│  └─ paper2.pdf
└─ query.txt
```

#### ❌ "query.txt not found"

**Check these:**
- ✅ File is named exactly `query.txt` (not `Query.txt`, `query.txt.txt`, or other names)
- ✅ File is in the same folder as `run_screening.py`
- ✅ File is not empty

**Alternative:** Specify custom path:
```powershell
.\scripts\run_tool.ps1 -QueryFile "path/to/my_custom_query.txt"
```

---

### Processing Issues

#### ⚠️ "Some PDFs failed to process"

**This is normal!** Some PDFs can't be processed due to:

1. **Encrypted/Password-protected PDFs**
   - **Solution:** Remove password protection before screening
   - Tools: Adobe Acrobat, online PDF unlockers

2. **Corrupted/Damaged PDFs**
   - **Solution:** Try re-downloading the file
   - Test: Can you open it normally in a PDF reader?

3. **Scanned Images (no extractable text)**
   - **Solution:** Use OCR (Optical Character Recognition) first
   - Tools: Adobe Acrobat Pro, Tesseract, online OCR tools

4. **Unusual/Non-standard PDF format**
   - **Solution:** Open in Adobe Reader and "Save As" to re-save

**Check the report:** The HTML report lists exactly which PDFs failed and why.

#### ❌ "Text extraction failed"

**Common causes:**
- PDF contains only images (scanned documents)
- PDF has copy/paste protection enabled
- PDF uses non-standard encoding
- Corrupt PDF file

**Solutions:**
- Use OCR tools for scanned PDFs
- Remove restrictions/protection
- Try opening and re-saving in Adobe Reader
- Verify file integrity (can you open it normally?)

---

### Query and Results Issues

#### ❌ "No papers matched the query" (0 included)

**Cause:** Query is too restrictive

**Solutions (in order of preference):**

1. **Add more synonyms with OR:**
   ```
   # Instead of:
   forest*
   
   # Try:
   forest* OR woodland* OR silvicultur* OR tree*
   ```

2. **Use wildcards for variations:**
   ```
   # Instead of:
   management
   
   # Try:
   manage* OR manag*
   ```

3. **Remove NOT clauses temporarily:**
   ```
   # Instead of:
   forest* AND NOT economics
   
   # Try just:
   forest*
   ```

4. **Test one concept at a time:**
   Start with the most specific concept and add conditions gradually

5. **Verify PDFs contain expected text:**
   Open a PDF you expect to match and search for your terms manually

#### ⚠️ "Too many papers matched" (>80% included)

**Cause:** Query is too broad

**Solutions:**

1. **Add more AND conditions:**
   ```
   # Instead of:
   forest*
   
   # Try:
   forest* AND management AND "ecosystem service*"
   ```

2. **Use exact phrases:**
   ```
   # Instead of:
   review
   
   # Try:
   "systematic review" OR "literature review"
   ```

3. **Add NOT clauses to exclude irrelevant topics:**
   ```
   forest* AND NOT (economics OR cost* OR financial*)
   ```

4. **Make terms more specific:**
   Replace broad terms with specific concepts from your research question

#### ❌ "Tool included/excluded paper incorrectly"

**Check these:**

1. **Open the HTML report** - See exactly which terms matched
2. **Check evidence snippets** - Does the match make sense in context?
3. **Review your query** - Does it capture your intent accurately?
4. **Test query logic** - Try parts of your query separately

**Remember:** The tool matches text literally. It doesn't understand context or meaning.

---

### Result and Output Issues

#### ❌ "validation_report.html won't open"

**Solutions:**
- Right-click → "Open with" → Choose your web browser
- If blocked: Check file isn't quarantined by antivirus
- Move file out of `results` folder and try again

#### ❌ "Sorted PDFs folder is empty"

**Check:**
- Did the screening complete successfully?
- Check the terminal output for errors
- Verify `results/validation_results.json` exists
- Re-run with verbose output to see detailed messages

#### ❌ "Can't find my original PDFs"

**Don't worry!** Your original PDFs in `input_pdfs/` are never modified. The sorted PDFs in `results/sorted_pdfs/` are **copies**, not moves.

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
A: Tested with 100+ papers. Processing time scales linearly (~1-2 seconds per paper). For very large collections (1000+), consider processing in batches.

**Q: What file formats are supported?**  
A: PDF only. For other formats (Word, HTML, TXT), convert to PDF first using tools like Microsoft Word's "Save as PDF" or online converters.

**Q: Can I use this for non-English papers?**  
A: Yes! The toolkit handles Unicode text in any language (German, French, Spanish, Chinese, etc.). Just make sure your query terms match the language of your papers.

**Q: How accurate is the screening?**  
A: Accuracy depends on your search criteria. Well-designed queries achieve 90%+ precision. The tool is highly reliable for matching text patterns, but it doesn't understand context—always manually review results.

**Q: Where exactly do I create the `input_pdfs` folder?**  
A: In the same directory as `run_screening.py`. If you're in `C:\Users\YourName\universal-literature-screening-toolkit\`, create `C:\Users\YourName\universal-literature-screening-toolkit\input_pdfs\`.

**Q: Can PDF files have any name?**  
A: Yes! Your PDFs can have any filename. Only the folder name (`input_pdfs`) and query file (`query.txt`) must be exact.

**Q: Can I use subfolders to organize my PDFs?**  
A: Not by default. The toolkit only reads PDFs directly in `input_pdfs`. (Advanced users can modify `config.json` for recursive searching.)

---

### Setup and Installation

**Q: Do I need to run setup every time?**  
A: No! Setup is one-time only. After initial setup, just use `.\scripts\run_tool.ps1` or the Python command to run screenings.

**Q: The script says 'Python not found' but I installed it - what's wrong?**  
A: Python might not be in your system PATH. Try:
1. Close and reopen PowerShell/Terminal completely
2. Use `py --version` instead of `python --version`
3. Reinstall Python and **check "Add Python to PATH"** during installation

**Q: I get 'script execution blocked' - is this dangerous to bypass?**  
A: No. `Set-ExecutionPolicy Bypass -Scope Process` only affects the current PowerShell window and is safe. It doesn't change system-wide security settings.

**Q: Can I install this on a shared/network drive?**  
A: It's possible but not recommended. Install on your local drive for best performance and to avoid permission issues.

---

### Search Query Questions

**Q: Should I use AND or OR between terms?**  
A:
- **OR**: "Find papers with *any* of these terms" → More inclusive, good for initial exploratory screening
- **AND**: "Find papers with *all* of these terms" → More restrictive, good for focused final screening

**Example:**
```
# Inclusive (finds papers about forests OR climate):
forest* OR climate*

# Restrictive (finds papers about forests AND climate together):
forest* AND climate*
```

**Q: What does the `*` wildcard do?**  
A: It matches any ending. Examples:
- `forest*` matches: forest, forests, forestry, forestation, forester, forested
- `manage*` matches: manage, management, managing, manager, managerial

**Q: How do I search for an exact phrase?**  
A: Use double quotes: `"ecosystem services"`. This will NOT match "ecosystem service" (singular) or "services to ecosystems" (different order).

**Q: Can I use parentheses to group terms?**  
A: Yes! Parentheses control logic precedence:
```
# This means: (forest OR woodland) AND (management OR planning)
(forest* OR woodland*) AND (management OR planning)

# Without parentheses, logic can be ambiguous
```

**Q: How do I handle abbreviations?**  
A: Include both full terms and abbreviations with OR:
```
("artificial intelligence" OR AI OR "machine learning" OR ML)
```

**Q: What about case sensitivity?**  
A: By default, searches are case-insensitive (`forest` matches `Forest`, `FOREST`, `forest`). This is recommended for most research. Advanced users can change this in `config.json`.

---

### Results and Output

**Q: Why did the tool include/exclude a specific paper?**  
A: Open `validation_report.html` - it shows exactly which terms matched in each paper, with evidence snippets from the text showing where the matches occurred.

**Q: Can I re-run with a different query without re-processing PDFs?**  
A: Currently no - each run extracts text from PDFs again. (This feature is planned for future versions.)

**Q: Where are my original PDFs after screening?**  
A: Your originals in `input_pdfs/` are **never modified or moved**. The PDFs in `results/sorted_pdfs/` are copies, not moves. Your originals are safe!

**Q: No papers matched my query - is the tool broken?**  
A: Probably not! Your query is likely too restrictive. See the [Troubleshooting section](#troubleshooting) for strategies to adjust your query. Try searching for one term at a time to verify the tool is working.

**Q: Can I combine results from multiple screening runs?**  
A: Yes, but you need to do it manually or write a custom script. Each run creates a separate `results` folder. You can specify different output folders with `--output` parameter.

---

### PDF Processing

**Q: Why did some PDFs fail to process?**  
A: Common reasons:
1. **Encrypted/Password-protected** - Remove protection first
2. **Corrupted file** - Try re-downloading
3. **Scanned image (no extractable text)** - Needs OCR preprocessing
4. **Unusual PDF format** - Try opening and re-saving in Adobe Reader

**Q: How do I know which PDFs failed and why?**  
A: Check the HTML report - there's a "Failed PDFs" section at the bottom listing each file with the specific reason for failure.

**Q: Can the tool process scanned PDFs (images)?**  
A: Not directly. Scanned PDFs need OCR (Optical Character Recognition) first to convert images to text. Try:
- Adobe Acrobat Pro (paid)
- Tesseract OCR (free, open-source)
- Online OCR tools

**Q: Some of my papers are in German/French/Chinese - will this work?**  
A: Yes! The toolkit handles any Unicode text. Just make sure your query includes terms in the same language as your papers. You can even mix languages in your query if needed.

---

### Research Workflow

**Q: Should I manually review all included papers?**  
A: **Yes, absolutely!** Automated screening is the first step to filter out obviously irrelevant papers. Always manually review included papers to make final inclusion decisions for your review.

**Q: How do I validate my search strategy?**  
A:
1. **Test with known papers**: Include 5-10 papers you know should be included/excluded
2. **Manual review samples**: Randomly sample included and excluded papers
3. **Compare with expert screening**: Have another researcher screen a subset
4. **Calculate metrics**: Compute precision, recall, and inter-rater agreement

**Q: How do I handle duplicate papers?**  
A: Run duplicate detection **before** screening using tools like:
- Zotero (free)
- Mendeley (free)
- Covidence (paid)

**Q: What about grey literature from multiple sources?**  
A: Works with any PDFs regardless of source! Just ensure all PDFs are in the `input_pdfs` folder. The toolkit doesn't care where PDFs came from.

---

### Technical and Advanced Questions

**Q: What's the difference between PyMuPDF and pdfplumber?**  
A: Both extract PDF text. PyMuPDF (fitz) is faster; pdfplumber is more robust for complex layouts and tables. The toolkit tries both automatically for best results.

**Q: Can I modify the source code?**  
A: Yes! The toolkit is MIT licensed (open source). See CONTRIBUTING.md for development guidelines. Feel free to fork, modify, and contribute back!

**Q: How do I cite this toolkit?**  
A: See the Citation section in README.md or use the CITATION.cff file for automatic citation formatting in tools like Zotero.

**Q: How many search blocks should I use? (legacy mode)**  
A: For legacy block-based search (deprecated): 3-7 blocks typically work well. Too few = overly broad; too many = overly restrictive. **Note:** Query mode is now recommended.

**Q: Should I include methodology terms in my query?**  
A: Yes, if methodology is part of your inclusion criteria. Examples:
- `"randomized controlled trial" OR RCT`
- `"systematic review" OR "meta-analysis"`
- `"qualitative study" OR "case study"`

**Q: Can I process PDFs on a schedule or in batch mode?**  
A: Yes! You can create scheduled tasks (Windows Task Scheduler, cron on Linux/Mac) to run the toolkit automatically. Use the Python command directly for scripting.

**Q: Does the toolkit store or send my data anywhere?**  
A: No! All processing happens locally on your computer. No data is sent to external servers. Your PDFs and results stay completely private.

---

## Support & Community

### Getting Help
1. **Check this guide** for comprehensive solutions
2. **Review [Troubleshooting section](#troubleshooting)** for common issues  
3. **Run tests** to verify installation: `.\scripts\run_tests.ps1` (Windows) or `python3 -m pytest tests -q` (Mac/Linux)
4. **Open GitHub issue** for bugs or feature requests: [GitHub Issues](https://github.com/uhiltner/universal-literature-screening-toolkit/issues)
5. **Check examples folder** for domain-specific query templates

### Contributing
- **Bug reports**: Use GitHub issues with error messages and steps to reproduce
- **Feature requests**: Describe your research use case and why the feature would help
- **Code contributions**: See CONTRIBUTING.md for development workflow
- **Documentation**: Help improve this guide by submitting corrections or additions

### Academic Use
- **Cite the toolkit** in your publications (see CITATION.cff)
- **Share search strategies** with the community to help others in your field
- **Report validation studies** to improve the tool and establish best practices
- **Collaborate** on domain-specific templates and extensions

### Version History
- **v1.0.2** (Current) - Documentation improvements, enhanced query mode
- **v1.0.1** - Bug fixes and stability improvements  
- **v1.0.0** - Initial release with query mode as recommended workflow

---

*This guide covers the complete functionality of the Universal Literature Screening Toolkit v1.0.3. For the latest updates and community contributions, visit the [GitHub repository](https://github.com/uhiltner/universal-literature-screening-toolkit).*