# 🚀 Quick Start Guide — Universal Literature Screening Toolkit

Beginner-friendly steps to run your first screening in ~10 minutes.

Tip: Need more depth? See the full USER_GUIDE.md.
## Troubleshooting (plain language)

### Setup Issues

**❌ "Python not found" or "'python' is not recognized"**
- **Cause**: Python not installed or not in PATH
- **Solution**: 
  1. Download Python from [python.org](https://www.python.org/downloads/)
  2. During installation, **check "Add Python to PATH"**
  3. Restart PowerShell
  4. Try `py --version` instead of `python --version`

**❌ "Execution Policy" error in PowerShell**
- **Cause**: Windows blocks unsigned scripts by default
- **Solution**: Run `Set-ExecutionPolicy Bypass -Scope Process` before setup
- **Note**: This only affects the current PowerShell window (safe)

**❌ "pip not found" or installation fails**
- **Cause**: pip not installed or environment issues
- **Solution**: Re-run `.\scripts\setup_windows.ps1` which fixes pip automatically

### Folder and File Issues

**❌ "No PDFs found in input_pdfs"**
- **Check 1**: Folder named exactly `input_pdfs` (not `Input_PDFs` or `input-pdfs`)
- **Check 2**: PDFs are directly in the folder (not in a subfolder)
- **Check 3**: Files have `.pdf` extension (not `.PDF` or `.pdf.txt`)

**❌ "query.txt not found"**
- **Check 1**: File is named exactly `query.txt` (not `Query.txt` or `query.txt.txt`)
- **Check 2**: File is in the same folder as `run_screening.py`
- **Solution**: Specify custom path: `--query-file "path/to/my_query.txt"`

### Processing Issues

**⚠️ "Some PDFs failed to process"**
- **This is normal!** Some PDFs can't be processed due to:
  - **Encrypted/Protected**: Password-protected or restricted PDFs
  - **Corrupted**: Damaged file (try re-downloading)
  - **Scanned Images**: PDFs without extractable text (need OCR)
- **Check the report**: The HTML report lists exactly which PDFs failed and why

**❌ "No papers matched the query" (0 included)**
- **Cause**: Query is too restrictive
- **Solutions**:
  1. Add more synonyms with OR: `forest* OR woodland* OR silvicultur*`
  2. Use wildcards: `manage*` instead of `management`
  3. Remove NOT clauses temporarily
  4. Try searching for just one concept first
  5. See USER_GUIDE.md - Refining Search Strings section

**⚠️ "Too many papers matched" (>80% included)**
- **Cause**: Query is too broad
- **Solutions**:
  1. Add more AND conditions: `forest* AND management AND "ecosystem service"`
  2. Use exact phrases: `"systematic review"` instead of `review`
  3. Add NOT clauses: `AND NOT (economics OR cost*)`
  4. See USER_GUIDE.md - Refining Search Strings section

---

## ❓ Frequently Asked Questions (FAQ)

### General Questions

**Q: Where exactly do I create the `input_pdfs` folder?**
A: In the same directory as `run_screening.py`. If you're in `C:\Users\YourName\universal-literature-screening-toolkit\`, create `C:\Users\YourName\universal-literature-screening-toolkit\input_pdfs\`.

**Q: Can PDF files have any name?**
A: Yes! Your PDFs can have any filename. Only the folder name (`input_pdfs`) and query file (`query.txt`) must be exact.

**Q: Can I use subfolders to organize my PDFs?**
A: Not for the first run. The toolkit only reads PDFs directly in `input_pdfs`. (Advanced users can modify `config.json` for recursive searching.)

**Q: How many PDFs can I process at once?**
A: Tested with 100+ PDFs. Processing time is ~1-2 seconds per PDF.

**Q: What if I have PDFs in multiple languages?**
A: The toolkit handles Unicode text (German, French, Spanish, Chinese, etc.). Just make sure your query terms match the language of your papers.

### Setup and Installation

**Q: The script says 'Python not found' but I installed it - what's wrong?**
A: Python might not be in your system PATH. Try:
1. Close and reopen PowerShell
2. Use `py --version` instead of `python --version`
3. Reinstall Python and check "Add Python to PATH"

**Q: I get 'script execution blocked' - is this dangerous to bypass?**
A: No. `Set-ExecutionPolicy Bypass -Scope Process` only affects the current PowerShell window and is safe. It doesn't change system-wide security settings.

**Q: Do I need to run setup every time?**
A: No! Setup is one-time. After that, just use `.\scripts\run_tool.ps1` to run screenings.

### Search Query Questions

**Q: Should I use AND or OR between terms?**
A: 
- **OR**: "Find papers with *any* of these terms" → More inclusive, good for initial screening
- **AND**: "Find papers with *all* of these terms" → More restrictive, good for focused screening

**Q: What does the `*` wildcard do?**
A: It matches any ending. `forest*` matches: forest, forests, forestry, forestation, forester, etc.

**Q: How do I search for an exact phrase?**
A: Use double quotes: `"ecosystem services"` (will not match "ecosystem service" or "services to ecosystems")

**Q: Can I use parentheses to group terms?**
A: Yes! `(forest* OR wood*) AND (management OR planning)` ensures proper logic.

### Results and Output

**Q: Why did the tool include/exclude a specific paper?**
A: Open `validation_report.html` - it shows exactly which terms matched in each paper, with evidence snippets from the text.

**Q: Can I re-run with different query without re-processing PDFs?**
A: Currently no - each run extracts text again. (This feature is planned for future versions.)

**Q: Where are my original PDFs after screening?**
A: They're copied to `results/sorted_pdfs/include` or `exclude\`. Your originals in `input_pdfs` are unchanged.

**Q: No papers matched my query - is the tool broken?**
A: Probably not! Your query might be too restrictive. See USER_GUIDE.md - Refining Search Strings for strategies to adjust your query.

### PDF Processing Issues

**Q: Why did some PDFs fail to process?**
A: Common reasons:
1. **Encrypted/Password-protected**: Remove protection first
2. **Corrupted file**: Try re-downloading
3. **Scanned image (no text)**: Needs OCR preprocessing
4. **Unusual PDF format**: Try opening and re-saving in Adobe Reader

**Q: How do I know which PDFs failed and why?**
A: Check the HTML report - there's a "Failed PDFs" section at the bottom listing each file with the specific reason.

**Q: Can the tool process scanned PDFs (images)?**
A: Not currently. Scanned PDFs need OCR (Optical Character Recognition) first. Try Adobe Acrobat or online OCR tools.

**Q: Some of my papers are in German/French/Chinese - will this work?**
A: Yes! The toolkit handles any Unicode text. Just make sure your query includes terms in the same language as your papers.

### Research Workflow

**Q: Should I manually review all included papers?**
A: Yes! Automated screening is just the first step. Always manually review included papers for final inclusion decisions.

**Q: How accurate is the screening?**
A: Accuracy depends on your query quality. Well-designed queries achieve 85-95% precision. Always validate with manual review.

**Q: Can I use this for full-text screening?**
A: The toolkit focuses on abstracts and keywords for speed. For full-text analysis, consider after initial screening.

**Q: How do I handle duplicates?**
A: Run duplicate detection *before* screening using tools like Zotero, Mendeley, or Covidence.

---

**💡 Pro Tip**: The toolkit works best when you iterate! Start broad, review results, refine your query, and run again. This is exactly how expert screeners work - the tool just makes it 100x faster.at you’ll do

- Put your PDFs into a folder (default: input_pdfs)
- Write one Boolean query (query.txt)
- Run the tool and review a clean HTML report

## 1) Install and verify

### 📁 Important: Folder Structure and Naming

**⚠️ CRITICAL**: The toolkit is **path-sensitive** and requires specific folder and file names. Follow this structure exactly:

```
C:\Users\YourName\universal-literature-screening-toolkit\
├─ input_pdfs\              ⬅️ MUST be named exactly "input_pdfs"
│  ├─ paper1.pdf           ⬅️ PDF files can have any name
│  ├─ study_forest.pdf     ⬅️ PDF files can have any name
│  └─ another_doc.pdf      ⬅️ PDF files can have any name
├─ query.txt                ⬅️ MUST be named exactly "query.txt" (or specify with --query-file)
├─ scripts\                 ⬅️ Don't modify these
│  ├─ setup_windows.ps1
│  └─ run_tool.ps1
└─ run_screening.py         ⬅️ Main program
```

**Key Rules:**
- ✅ **PDF files**: Can have any name you want
- ❌ **Folders**: Must be named exactly as shown (`input_pdfs`, `scripts`)
- ❌ **Query file**: Must be named `query.txt` (or specify a custom name with `--query-file`)
- ❌ **Location**: The `input_pdfs` folder must be in the same directory as `run_screening.py`

### Windows Setup (PowerShell)

**Step-by-step with verification:**

```powershell
# Step 1: Navigate to the toolkit folder
cd C:\Users\YourName\universal-literature-screening-toolkit

# Step 2: Allow PowerShell to run scripts (for this session only)
Set-ExecutionPolicy Bypass -Scope Process

# Step 3: Run the automated setup
.\scripts\setup_windows.ps1

# Step 4: Verify Python installation
python --version
# Expected output: Python 3.8.0 or higher

# Step 5: Verify PDF extraction libraries
python -c "import fitz; import pdfplumber; print('✅ PDF libraries installed correctly')"
# Expected output: ✅ PDF libraries installed correctly

# Step 6: Run the test suite to verify everything works
.\scripts\run_tests.ps1
# Expected output: All tests passed successfully! ✅
```

**If Step 4 fails** (Python not found):
- Install Python from [python.org](https://www.python.org/downloads/)
- ⚠️ **During installation, check "Add Python to PATH"**
- Restart PowerShell and try again

**If Step 5 fails** (libraries not installed):
- Re-run `.\scripts\setup_windows.ps1`
- If still failing, manually install: `pip install PyMuPDF pdfplumber`

### macOS/Linux Setup

```bash
# Step 1: Navigate to toolkit folder
cd /path/to/universal-literature-screening-toolkit

# Step 2: Make scripts executable (first time only)
chmod +x scripts/setup_unix.sh scripts/run_tool.sh scripts/run_tests.sh

# Step 3: Run automated setup
./scripts/setup_unix.sh

# Step 4: Verify installation
python3 --version
python3 -c "import fitz; import pdfplumber; print('✅ PDF libraries installed correctly')"

# Step 5: Run tests
python3 -m pytest tests -q
```

## 2) Prepare your data

### Create the Input Folder

**Windows:**
```powershell
# Make sure you're in the toolkit directory
cd C:\Users\YourName\universal-literature-screening-toolkit

# Create the input_pdfs folder
New-Item -ItemType Directory -Name "input_pdfs" -Force
```

**macOS/Linux:**
```bash
mkdir -p input_pdfs
```

### Copy Your PDFs

1. **Copy all PDF files** you want to screen into the `input_pdfs\` folder
2. **Keep it flat**: All PDFs directly in `input_pdfs\`, no subfolders
3. **Any PDF names work**: `paper1.pdf`, `Smith_2020_forest.pdf`, etc.

**Example:**
```
input_pdfs\
├─ Smith_2020_climate.pdf
├─ Jones_2021_forest_management.pdf
├─ Lee_2022_ecosystem_services.pdf
└─ Garcia_2023_biodiversity.pdf
```

## 3) Write your query (recommended)

Create query.txt and paste one Boolean query. Lines starting with # are comments and ignored.

Example:

```
# Forest decision-support focus with ES and management context; exclude economics
((forest* OR wood*) AND (management OR planning)) AND ("ecosystem service*" OR biodiversity) AND NOT (economics)
```

Quick syntax tips:

- Operators: NOT > AND > OR (use parentheses to group)
- Quotes for phrases: "ecosystem service"
- Wildcards: model* matches model, models, modeling, modelling

## 4) Run the tool

Windows (PowerShell):

```powershell
./scripts/run_tool.ps1 -InputPath "input_pdfs" -OutputPath "results" -QueryFile "query.txt"
```

macOS/Linux:

```bash
./scripts/run_tool.sh --input "input_pdfs" --output "results" --query-file "query.txt"
```

Or run the Python entry point directly:

```bash
python run_screening.py --input input_pdfs --output results --query-file query.txt
```

Outputs appear in results/:

```
results/
├─ validation_report.html   # Open in a browser
├─ validation_results.json  # Machine-readable
└─ sorted_pdfs/
   ├─ include/
   └─ exclude/
```

## 5) Example you can try now

We ship an example query at examples/query.txt.

Windows:

```powershell
./scripts/run_tool.ps1 -InputPath "input_pdfs" -OutputPath "example_results" -QueryFile "examples/query.txt"
```

macOS/Linux:

```bash
./scripts/run_tool.sh --input "input_pdfs" --output "example_results" --query-file "examples/query.txt"
```

## Troubleshooting (plain language)

- “Python not found”: Install from python.org; on Windows try `py -V`.
- Script blocked: `Set-ExecutionPolicy Bypass -Scope Process` (Windows).
- No PDFs found: Check files are in input_pdfs and have .pdf extension.
- No matches: Loosen your query (add OR synonyms, use wildcards).

Deprecation note: The older block-based --search-terms flow is still available for one transition release but will be removed. Prefer --query-file. In query mode, validation_logic in config.json is ignored.