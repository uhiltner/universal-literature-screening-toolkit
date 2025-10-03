# 🚀 Quick Start Guide — Universal Literature Screening Toolkit# 🚀 Quick Start Guide — Universal Literature Screening Toolkit



**Welcome!** This guide will help you screen your first batch of research papers in about 10 minutes, even if you've never used a command line tool before.**Welcome!** This guide will help you screen your first batch of research papers in about 10 minutes, even if you've never used a command line tool before.



**What you'll learn:****What you'll learn:**

- How to install the toolkit (one-time setup)- How to install the toolkit (one-time setup)

- How to organize your PDF files- How to organize your PDF files

- How to write a simple search query- How to write a simple search query

- How to run the screening and view results- How to run the screening and view results



**Need more details?** See the full USER_GUIDE.md for advanced features and troubleshooting.**Need more details?** See the full USER_GUIDE.md for advanced features and troubleshooting.

## Troubleshooting (plain language)

---

### Setup Issues

## 📋 What You'll Need

**❌ "Python not found" or "'python' is not recognized"**

Before starting, make sure you have:- **Cause**: Python not installed or not in PATH

- **A computer** running Windows, macOS, or Linux- **Solution**: 

- **PDF files** of the research papers you want to screen  1. Download Python from [python.org](https://www.python.org/downloads/)

- **Internet connection** for the one-time setup  2. During installation, **check "Add Python to PATH"**

- **15 minutes** for installation and your first screening  3. Restart PowerShell

  4. Try `py --version` instead of `python --version`

---

**❌ "Execution Policy" error in PowerShell**

## Step 1: Install the Toolkit (One-Time Setup)- **Cause**: Windows blocks unsigned scripts by default

- **Solution**: Run `Set-ExecutionPolicy Bypass -Scope Process` before setup

### 📁 Understanding the Folder Structure- **Note**: This only affects the current PowerShell window (safe)



The toolkit needs files organized in a specific way. Here's what it looks like:**❌ "pip not found" or installation fails**

- **Cause**: pip not installed or environment issues

```- **Solution**: Re-run `.\scripts\setup_windows.ps1` which fixes pip automatically

universal-literature-screening-toolkit/     ← Main folder (you downloaded this)

├─ input_pdfs/                              ← Put your PDF files here (you'll create this)### Folder and File Issues

│  ├─ paper1.pdf

│  ├─ paper2.pdf**❌ "No PDFs found in input_pdfs"**

│  └─ paper3.pdf- **Check 1**: Folder named exactly `input_pdfs` (not `Input_PDFs` or `input-pdfs`)

├─ query.txt                                ← Your search query (you'll create this)- **Check 2**: PDFs are directly in the folder (not in a subfolder)

├─ scripts/                                 ← Helper programs (already included)- **Check 3**: Files have `.pdf` extension (not `.PDF` or `.pdf.txt`)

└─ run_screening.py                         ← Main program (already included)

```**❌ "query.txt not found"**

- **Check 1**: File is named exactly `query.txt` (not `Query.txt` or `query.txt.txt`)

**Important Notes:**- **Check 2**: File is in the same folder as `run_screening.py`

- ✅ Your **PDF files can have any names** you want- **Solution**: Specify custom path: `--query-file "path/to/my_query.txt"`

- ⚠️ The **folder names must be exact**: `input_pdfs` (not `Input_PDFs` or `pdfs`)

- ⚠️ The **query file must be named**: `query.txt` (unless you specify otherwise)### Processing Issues



### 🪟 Windows Installation**⚠️ "Some PDFs failed to process"**

- **This is normal!** Some PDFs can't be processed due to:

**Step 1: Open PowerShell**  - **Encrypted/Protected**: Password-protected or restricted PDFs

- Press `Windows Key + X`  - **Corrupted**: Damaged file (try re-downloading)

- Click "Windows PowerShell" or "Terminal"  - **Scanned Images**: PDFs without extractable text (need OCR)

- **Check the report**: The HTML report lists exactly which PDFs failed and why

**Step 2: Go to the Toolkit Folder**

```powershell**❌ "No papers matched the query" (0 included)**

# Replace "YourName" with your actual Windows username- **Cause**: Query is too restrictive

cd C:\Users\YourName\Downloads\universal-literature-screening-toolkit- **Solutions**:

```  1. Add more synonyms with OR: `forest* OR woodland* OR silvicultur*`

  2. Use wildcards: `manage*` instead of `management`

**Step 3: Allow PowerShell to Run the Installer**  3. Remove NOT clauses temporarily

```powershell  4. Try searching for just one concept first

Set-ExecutionPolicy Bypass -Scope Process  5. See USER_GUIDE.md - Refining Search Strings section

```

**Don't worry!** This is safe. It only affects this PowerShell window and allows our installer to run.**⚠️ "Too many papers matched" (>80% included)**

- **Cause**: Query is too broad

**Step 4: Run the Installer**- **Solutions**:

```powershell  1. Add more AND conditions: `forest* AND management AND "ecosystem service"`

.\scripts\setup_windows.ps1  2. Use exact phrases: `"systematic review"` instead of `review`

```  3. Add NOT clauses: `AND NOT (economics OR cost*)`

  4. See USER_GUIDE.md - Refining Search Strings section

This will:

- Check if Python is installed (and help you install it if needed)---

- Create a safe, isolated environment for the toolkit

- Install all required software libraries## ❓ Frequently Asked Questions (FAQ)

- Take 2-3 minutes to complete

### General Questions

**Step 5: Verify Everything Works**

```powershell**Q: Where exactly do I create the `input_pdfs` folder?**

.\scripts\run_tests.ps1A: In the same directory as `run_screening.py`. If you're in `C:\Users\YourName\universal-literature-screening-toolkit\`, create `C:\Users\YourName\universal-literature-screening-toolkit\input_pdfs\`.

```

**Q: Can PDF files have any name?**

**Success looks like:** You'll see `✅ All tests passed successfully!`A: Yes! Your PDFs can have any filename. Only the folder name (`input_pdfs`) and query file (`query.txt`) must be exact.



### 🍎 macOS / 🐧 Linux Installation**Q: Can I use subfolders to organize my PDFs?**

A: Not for the first run. The toolkit only reads PDFs directly in `input_pdfs`. (Advanced users can modify `config.json` for recursive searching.)

**Step 1: Open Terminal**

- macOS: Press `Cmd + Space`, type "Terminal", press Enter**Q: How many PDFs can I process at once?**

- Linux: Press `Ctrl + Alt + T`A: Tested with 100+ PDFs. Processing time is ~1-2 seconds per PDF.



**Step 2: Go to the Toolkit Folder****Q: What if I have PDFs in multiple languages?**

```bashA: The toolkit handles Unicode text (German, French, Spanish, Chinese, etc.). Just make sure your query terms match the language of your papers.

cd ~/Downloads/universal-literature-screening-toolkit

```### Setup and Installation



**Step 3: Make the Installer Executable****Q: The script says 'Python not found' but I installed it - what's wrong?**

```bashA: Python might not be in your system PATH. Try:

chmod +x scripts/setup_unix.sh scripts/run_tool.sh scripts/run_tests.sh1. Close and reopen PowerShell

```2. Use `py --version` instead of `python --version`

3. Reinstall Python and check "Add Python to PATH"

**Step 4: Run the Installer**

```bash**Q: I get 'script execution blocked' - is this dangerous to bypass?**

./scripts/setup_unix.shA: No. `Set-ExecutionPolicy Bypass -Scope Process` only affects the current PowerShell window and is safe. It doesn't change system-wide security settings.

```

**Q: Do I need to run setup every time?**

**Step 5: Verify Everything Works**A: No! Setup is one-time. After that, just use `.\scripts\run_tool.ps1` to run screenings.

```bash

python3 -m pytest tests -q### Search Query Questions

```

**Q: Should I use AND or OR between terms?**

**Success looks like:** You'll see messages saying tests passed.A: 

- **OR**: "Find papers with *any* of these terms" → More inclusive, good for initial screening

---- **AND**: "Find papers with *all* of these terms" → More restrictive, good for focused screening



## Step 2: Prepare Your Research Papers**Q: What does the `*` wildcard do?**

A: It matches any ending. `forest*` matches: forest, forests, forestry, forestation, forester, etc.

### Create the Input Folder

**Q: How do I search for an exact phrase?**

**Windows PowerShell:**A: Use double quotes: `"ecosystem services"` (will not match "ecosystem service" or "services to ecosystems")

```powershell

# Make sure you're in the toolkit folder**Q: Can I use parentheses to group terms?**

cd C:\Users\YourName\Downloads\universal-literature-screening-toolkitA: Yes! `(forest* OR wood*) AND (management OR planning)` ensures proper logic.



# Create the input_pdfs folder### Results and Output

New-Item -ItemType Directory -Name "input_pdfs" -Force

```**Q: Why did the tool include/exclude a specific paper?**

A: Open `validation_report.html` - it shows exactly which terms matched in each paper, with evidence snippets from the text.

**macOS/Linux Terminal:**

```bash**Q: Can I re-run with different query without re-processing PDFs?**

mkdir -p input_pdfsA: Currently no - each run extracts text again. (This feature is planned for future versions.)

```

**Q: Where are my original PDFs after screening?**

### Add Your PDF FilesA: They're copied to `results/sorted_pdfs/include` or `exclude\`. Your originals in `input_pdfs` are unchanged.



1. **Copy all your research papers (PDF files)** into the `input_pdfs` folder**Q: No papers matched my query - is the tool broken?**

2. **Keep all files in one folder** - don't create subfolders inside `input_pdfs`A: Probably not! Your query might be too restrictive. See USER_GUIDE.md - Refining Search Strings for strategies to adjust your query.

3. **File names don't matter** - name them however you like

### PDF Processing Issues

**Example of what `input_pdfs` should look like:**

```**Q: Why did some PDFs fail to process?**

input_pdfs/A: Common reasons:

├─ Smith_2020_climate_change.pdf1. **Encrypted/Password-protected**: Remove protection first

├─ Jones_forest_study.pdf2. **Corrupted file**: Try re-downloading

├─ biodiversity_paper.pdf3. **Scanned image (no text)**: Needs OCR preprocessing

└─ my_important_paper.pdf4. **Unusual PDF format**: Try opening and re-saving in Adobe Reader

```

**Q: How do I know which PDFs failed and why?**

---A: Check the HTML report - there's a "Failed PDFs" section at the bottom listing each file with the specific reason.



## Step 3: Create Your Search Query**Q: Can the tool process scanned PDFs (images)?**

A: Not currently. Scanned PDFs need OCR (Optical Character Recognition) first. Try Adobe Acrobat or online OCR tools.

### What is a Search Query?

**Q: Some of my papers are in German/French/Chinese - will this work?**

A search query tells the toolkit which papers to include or exclude. It's like a Google search, but more precise.A: Yes! The toolkit handles any Unicode text. Just make sure your query includes terms in the same language as your papers.



**Think of it this way:**### Research Workflow

- "Show me papers about **forests** AND **management**"

- "Include papers about **climate** OR **weather**"**Q: Should I manually review all included papers?**

- "Exclude papers about **economics**"A: Yes! Automated screening is just the first step. Always manually review included papers for final inclusion decisions.



### Create the Query File**Q: How accurate is the screening?**

A: Accuracy depends on your query quality. Well-designed queries achieve 85-95% precision. Always validate with manual review.

**Windows:**

1. Open Notepad (search for it in Start Menu)**Q: Can I use this for full-text screening?**

2. Type your search query (see examples below)A: The toolkit focuses on abstracts and keywords for speed. For full-text analysis, consider after initial screening.

3. Save as: `query.txt` in the toolkit folder

**Q: How do I handle duplicates?**

**macOS/Linux:**A: Run duplicate detection *before* screening using tools like Zotero, Mendeley, or Covidence.

1. Open TextEdit (Mac) or gedit (Linux)

2. Type your search query---

3. Save as: `query.txt` in the toolkit folder

**💡 Pro Tip**: The toolkit works best when you iterate! Start broad, review results, refine your query, and run again. This is exactly how expert screeners work - the tool just makes it 100x faster.at you’ll do

### Simple Query Examples

- Put your PDFs into a folder (default: input_pdfs)

**Example 1: Basic Search (Find papers about forests AND climate)**- Write one Boolean query (query.txt)

```- Run the tool and review a clean HTML report

forest* AND climate*

```## 1) Install and verify



**Example 2: Flexible Search (Find papers about forests OR woodlands)**### 📁 Important: Folder Structure and Naming

```

(forest* OR woodland* OR tree*)**⚠️ CRITICAL**: The toolkit is **path-sensitive** and requires specific folder and file names. Follow this structure exactly:

```

```

**Example 3: Exclude Topics (Find forest papers, but exclude economics)**C:\Users\YourName\universal-literature-screening-toolkit\

```├─ input_pdfs\              ⬅️ MUST be named exactly "input_pdfs"

forest* AND NOT economics│  ├─ paper1.pdf           ⬅️ PDF files can have any name

```│  ├─ study_forest.pdf     ⬅️ PDF files can have any name

│  └─ another_doc.pdf      ⬅️ PDF files can have any name

**Example 4: Complex Search (Multiple concepts)**├─ query.txt                ⬅️ MUST be named exactly "query.txt" (or specify with --query-file)

```├─ scripts\                 ⬅️ Don't modify these

# This is a comment - it won't affect the search│  ├─ setup_windows.ps1

# Find papers about: forests with ecosystem services, but not about economics│  └─ run_tool.ps1

└─ run_screening.py         ⬅️ Main program

(forest* OR woodland*) AND ("ecosystem service*" OR biodiversity) AND NOT (economics OR cost*)```

```

**Key Rules:**

### Query Syntax Explained- ✅ **PDF files**: Can have any name you want

- ❌ **Folders**: Must be named exactly as shown (`input_pdfs`, `scripts`)

**For beginners, remember these 4 rules:**- ❌ **Query file**: Must be named `query.txt` (or specify a custom name with `--query-file`)

- ❌ **Location**: The `input_pdfs` folder must be in the same directory as `run_screening.py`

1. **Wildcards (`*`)**: Use `*` at the end of a word to match variations

   - `forest*` matches: forest, forests, forestry, forestation### Windows Setup (PowerShell)

   

2. **Exact Phrases**: Use quotes for multi-word terms**Step-by-step with verification:**

   - `"climate change"` matches exactly "climate change" (not "climate" alone)

   ```powershell

3. **Combining Terms**:# Step 1: Navigate to the toolkit folder

   - `AND` = both terms must be presentcd C:\Users\YourName\universal-literature-screening-toolkit

   - `OR` = at least one term must be present

   - `NOT` = exclude papers with this term# Step 2: Allow PowerShell to run scripts (for this session only)

   Set-ExecutionPolicy Bypass -Scope Process

4. **Grouping**: Use parentheses to control logic

   - `(forest* OR tree*) AND climate*` = (forest OR tree) AND climate# Step 3: Run the automated setup

.\scripts\setup_windows.ps1

---

# Step 4: Verify Python installation

## Step 4: Run the Screeningpython --version

# Expected output: Python 3.8.0 or higher

Now you're ready to screen your papers!

# Step 5: Verify PDF extraction libraries

### 🪟 Windowspython -c "import fitz; import pdfplumber; print('✅ PDF libraries installed correctly')"

# Expected output: ✅ PDF libraries installed correctly

Open PowerShell and run:

```powershell# Step 6: Run the test suite to verify everything works

.\scripts\run_tool.ps1 -QueryFile "query.txt".\scripts\run_tests.ps1

```# Expected output: All tests passed successfully! ✅

```

**What this does:**

- Reads all PDFs from `input_pdfs`**If Step 4 fails** (Python not found):

- Checks each paper against your query- Install Python from [python.org](https://www.python.org/downloads/)

- Creates a report in the `results` folder- ⚠️ **During installation, check "Add Python to PATH"**

- Takes about 1-2 seconds per paper- Restart PowerShell and try again



### 🍎 macOS / 🐧 Linux**If Step 5 fails** (libraries not installed):

- Re-run `.\scripts\setup_windows.ps1`

Open Terminal and run:- If still failing, manually install: `pip install PyMuPDF pdfplumber`

```bash

./scripts/run_tool.sh --query-file "query.txt"### macOS/Linux Setup

```

```bash

### What Happens During Screening# Step 1: Navigate to toolkit folder

cd /path/to/universal-literature-screening-toolkit

You'll see messages like:

```# Step 2: Make scripts executable (first time only)

📄 Processing papers...chmod +x scripts/setup_unix.sh scripts/run_tool.sh scripts/run_tests.sh

✅ Extracted text from paper1.pdf

✅ Extracted text from paper2.pdf# Step 3: Run automated setup

✅ Extracted text from paper3.pdf./scripts/setup_unix.sh

📊 Screening complete!

```# Step 4: Verify installation

python3 --version

**This is normal!** The toolkit is:python3 -c "import fitz; import pdfplumber; print('✅ PDF libraries installed correctly')"

1. Reading text from each PDF

2. Checking if it matches your query# Step 5: Run tests

3. Organizing the resultspython3 -m pytest tests -q

```

---

## 2) Prepare your data

## Step 5: View Your Results

### Create the Input Folder

### Where to Find Results

**Windows:**

After screening, you'll find a new `results` folder:```powershell

# Make sure you're in the toolkit directory

```cd C:\Users\YourName\universal-literature-screening-toolkit

results/

├─ validation_report.html        ← Open this in your web browser!# Create the input_pdfs folder

├─ validation_results.json       ← Data file (for advanced users)New-Item -ItemType Directory -Name "input_pdfs" -Force

└─ sorted_pdfs/```

   ├─ include/                   ← Papers that matched your query

   └─ exclude/                   ← Papers that didn't match**macOS/Linux:**

``````bash

mkdir -p input_pdfs

### Understanding the HTML Report```



**Open `validation_report.html` in your web browser** (double-click the file)### Copy Your PDFs



The report shows:1. **Copy all PDF files** you want to screen into the `input_pdfs\` folder

2. **Keep it flat**: All PDFs directly in `input_pdfs\`, no subfolders

**1. Summary Section**3. **Any PDF names work**: `paper1.pdf`, `Smith_2020_forest.pdf`, etc.

```

📊 Screening Results Summary**Example:**

Total Papers: 50```

✅ Included: 12 (24%)input_pdfs\

❌ Excluded: 38 (76%)├─ Smith_2020_climate.pdf

```├─ Jones_2021_forest_management.pdf

├─ Lee_2022_ecosystem_services.pdf

**2. Detailed Results Table**└─ Garcia_2023_biodiversity.pdf

```

For each included paper, you'll see:

- **Paper name**## 3) Write your query (recommended)

- **Why it was included** (which terms matched)

- **Evidence snippets** (actual text from the paper showing the match)Create query.txt and paste one Boolean query. Lines starting with # are comments and ignored.



**3. Your Query**Example:



Shows exactly what search query was used, so you can remember your criteria.```

# Forest decision-support focus with ES and management context; exclude economics

### What to Do Next((forest* OR wood*) AND (management OR planning)) AND ("ecosystem service*" OR biodiversity) AND NOT (economics)

```

1. **Review the included papers** in `results/sorted_pdfs/include/`

2. **Read the HTML report** to see why each paper was includedQuick syntax tips:

3. **Manually check** a few papers to ensure the results make sense

4. **Refine your query** if needed and run again- Operators: NOT > AND > OR (use parentheses to group)

- Quotes for phrases: "ecosystem service"

**Remember:** Automated screening is the first step. Always manually review the included papers for your final decision!- Wildcards: model* matches model, models, modeling, modelling



---## 4) Run the tool



## 🎯 Try an Example Right NowWindows (PowerShell):



We've included a sample query file you can try:```powershell

./scripts/run_tool.ps1 -InputPath "input_pdfs" -OutputPath "results" -QueryFile "query.txt"

**Windows:**```

```powershell

.\scripts\run_tool.ps1 -InputPath "input_pdfs" -OutputPath "example_results" -QueryFile "examples\query.txt"macOS/Linux:

```

```bash

**macOS/Linux:**./scripts/run_tool.sh --input "input_pdfs" --output "results" --query-file "query.txt"

```bash```

./scripts/run_tool.sh --input "input_pdfs" --output "example_results" --query-file "examples/query.txt"

```Or run the Python entry point directly:



This runs the example query and saves results to a separate `example_results` folder so you can see how it works.```bash

python run_screening.py --input input_pdfs --output results --query-file query.txt

---```



## 🆘 Common Problems and SolutionsOutputs appear in results/:



### Installation Problems```

results/

**❌ "Python not found" or "'python' is not recognized"**├─ validation_report.html   # Open in a browser

├─ validation_results.json  # Machine-readable

**What this means:** Python isn't installed or Windows can't find it.└─ sorted_pdfs/

   ├─ include/

**How to fix:**   └─ exclude/

1. Download Python from [python.org/downloads](https://www.python.org/downloads/)```

2. **Important:** During installation, check the box that says **"Add Python to PATH"**

3. Restart PowerShell## 5) Example you can try now

4. Try running the setup again

We ship an example query at examples/query.txt.

**Alternative:** Try using `py` instead of `python`:

```powershellWindows:

py --version

``````powershell

./scripts/run_tool.ps1 -InputPath "input_pdfs" -OutputPath "example_results" -QueryFile "examples/query.txt"

---```



**❌ PowerShell says "Execution Policy" error**macOS/Linux:



**What this means:** Windows is blocking the script for security.```bash

./scripts/run_tool.sh --input "input_pdfs" --output "example_results" --query-file "examples/query.txt"

**How to fix:** Run this command first:```

```powershell

Set-ExecutionPolicy Bypass -Scope Process## Troubleshooting (plain language)

```

- “Python not found”: Install from python.org; on Windows try `py -V`.

**Why it's safe:** This only affects your current PowerShell window and doesn't change your computer's security settings.- Script blocked: `Set-ExecutionPolicy Bypass -Scope Process` (Windows).

- No PDFs found: Check files are in input_pdfs and have .pdf extension.

---- No matches: Loosen your query (add OR synonyms, use wildcards).



**❌ "pip not found" error**Deprecation note: The older block-based --search-terms flow is still available for one transition release but will be removed. Prefer --query-file. In query mode, validation_logic in config.json is ignored.

**What this means:** The Python package installer isn't working.

**How to fix:** Run the setup script again:
```powershell
.\scripts\setup_windows.ps1
```

The setup script will automatically fix pip.

---

### File and Folder Problems

**❌ "No PDFs found in input_pdfs"**

**How to fix:**
1. Check the folder is named exactly **`input_pdfs`** (all lowercase, with underscore)
2. Make sure PDF files are **directly in the folder**, not in a subfolder
3. Check files end with **`.pdf`** (not `.PDF` or `.pdf.txt`)

**Check your setup:**
```powershell
# Windows - list files in input_pdfs
dir input_pdfs

# macOS/Linux - list files in input_pdfs
ls input_pdfs
```

---

**❌ "query.txt not found"**

**How to fix:**
1. Make sure the file is named exactly **`query.txt`** (all lowercase)
2. Save it in the **same folder** as `run_screening.py`
3. If you saved it somewhere else, specify the path:
   ```powershell
   .\scripts\run_tool.ps1 -QueryFile "path\to\your\query.txt"
   ```

**Windows users:** Make sure you're not accidentally saving as `query.txt.txt`. In File Explorer, go to View → Show file extensions to check.

---

### Screening Problems

**⚠️ "Some PDFs failed to process"**

**What this means:** Some PDF files couldn't be read. This is normal!

**Common reasons:**
- **Password-protected PDFs**: The file is locked
- **Scanned documents**: The PDF is just an image with no text
- **Corrupted files**: The file is damaged

**What to do:**
1. Check the HTML report - it lists which files failed and why
2. For scanned PDFs, you'll need OCR (Optical Character Recognition) first
3. For protected PDFs, remove the password protection
4. For corrupted PDFs, try re-downloading them

---

**❌ "No papers matched the query" (0 included)**

**What this means:** Your search query is too strict. No papers met all the criteria.

**How to fix:** Make your query more flexible:

1. **Add more synonyms with OR:**
   ```
   # Too strict:
   forest
   
   # Better:
   (forest* OR woodland* OR tree* OR silvicultur*)
   ```

2. **Use wildcards:**
   ```
   # Too strict:
   management
   
   # Better:
   manage*
   (matches: manage, management, managing, manager, etc.)
   ```

3. **Remove NOT clauses temporarily:**
   ```
   # Too strict:
   forest* AND management AND NOT economics
   
   # Try first:
   forest* AND management
   ```

4. **Test one concept at a time:**
   ```
   # Start simple to test:
   forest*
   
   # Then add more:
   forest* AND management
   ```

---

**⚠️ "Too many papers matched" (>80% included)**

**What this means:** Your search query is too broad. Almost everything matched.

**How to fix:** Make your query more specific:

1. **Add more AND conditions:**
   ```
   # Too broad:
   forest*
   
   # Better:
   forest* AND management AND ("ecosystem service*" OR biodiversity)
   ```

2. **Use exact phrases:**
   ```
   # Too broad:
   review
   
   # Better:
   "systematic review"
   ```

3. **Add exclusions with NOT:**
   ```
   # Too broad:
   forest* AND management
   
   # Better:
   forest* AND management AND NOT (furniture OR timber)
   ```

---

## ❓ Frequently Asked Questions

**Q: Do I need to know programming to use this?**
A: No! Just follow this guide. You'll use simple commands, but you don't need to understand programming.

---

**Q: How long does screening take?**
A: About 1-2 seconds per PDF. So 100 papers = about 2-3 minutes.

---

**Q: Can I stop and resume later?**
A: Not currently. Each time you run the tool, it processes all papers fresh. (This feature is planned for future versions.)

---

**Q: What if my papers are in different languages?**
A: The toolkit works with any language! Just make sure your search query uses terms in the same language as your papers.

---

**Q: Can I search for papers in multiple languages at once?**
A: Yes! Include terms in different languages in your query:
```
(forest* OR Wald* OR forêt*) AND (management OR Verwaltung OR gestion)
```

---

**Q: Why are some papers in the "exclude" folder even though they seem relevant?**
A: The toolkit only checks if papers match your exact query. It doesn't understand context or meaning. Always manually review the results!

---

**Q: Can I use this for my thesis/publication?**
A: Yes! Many researchers use automated screening as the first step in systematic reviews. Just make sure to:
1. Manually review all included papers
2. Document your search query in your methods section
3. Cite the toolkit (see CITATION.cff file)

---

**Q: Where can I get help if I'm stuck?**
A: 
1. Check this Quick Start guide
2. Read the USER_GUIDE.md for more details
3. Open an issue on GitHub: [github.com/uhiltner/universal-literature-screening-toolkit](https://github.com/uhiltner/universal-literature-screening-toolkit)

---

## 🎓 Next Steps

**You've completed your first screening! Here's what to do next:**

1. **Review your results** manually - automated screening is just the start
2. **Refine your query** based on what you found
3. **Run again** with improved criteria if needed
4. **Read the USER_GUIDE.md** for advanced features like:
   - Complex Boolean queries
   - Handling different types of PDFs
   - Improving search accuracy
   - Domain-specific search strategies

**Remember:** Getting the perfect query takes practice. Most researchers run screening 2-3 times with different queries before finding the right balance!

---

**🎉 Congratulations!** You're now ready to screen research papers efficiently. Happy researching!

*For detailed information and advanced features, see USER_GUIDE.md*
