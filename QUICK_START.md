# 🚀 Quick Start Guide# 🚀 Quick Start Guide — Universal Literature Screening Toolkit



Get your first screening done in 15 minutes. For troubleshooting, FAQ, and advanced features, see [USER_GUIDE.md](USER_GUIDE.md).**Get your first screening done.** This tutorial covers the essential steps to install and run the toolkit.



---

💡 **For troubleshooting, FAQ, and advanced features**, see the [USER_GUIDE.md](USER_GUIDE.md).**Welcome!** This quick tutorial will guide you through your first screening in about 15-20 minutes, even if you've never used command-line tools before.

## What You'll Do

---

1. **Install** → Run automated setup script

2. **Prepare PDFs** → Put papers in `input_pdfs/` folder## What You'll Do 

3. **Write Query** → Create `query.txt` with search criteria

4. **Run Screening** → Execute the tool**What you'll learn:****Welcome!** This guide will help you screen your first batch of research papers in about 10 minutes, even if you've never used a command line tool before.**Welcome!** This guide will help you screen your first batch of research papers in about 10 minutes, even if you've never used a command line tool before.

5. **View Results** → Open HTML report

1. **Install** → Run automated setup script (~5 min)- How to install the toolkit (one-time setup)

---

2. **Prepare PDFs** → Put papers in `input_pdfs/` folder (~2 min)

## 1. Installation

3. **Write Query** → Create `query.txt` with search criteria (~3 min)- How to organize your PDF files

### Windows

4. **Run Screening** → Execute the tool (~1 min + processing time)

Open PowerShell (`Win+X` → PowerShell), navigate to toolkit folder:

5. **View Results** → Open HTML report (~2 min)- How to write a search query

```powershell

cd C:\Users\YourName\Downloads\universal-literature-screening-toolkit

Set-ExecutionPolicy Bypass -Scope Process

.\scripts\setup_windows.ps1**Total time:** ~15 minutes + processing (1-2 seconds per PDF)- How to run your first screening**What you'll learn:****What you'll learn:**

.\scripts\run_tests.ps1

```



✅ **Expected:** "All tests passed successfully!"---- Where to find your results



### macOS/Linux



Open Terminal:## 1. Installation (5 Minutes)- How to install the toolkit (one-time setup)- How to install the toolkit (one-time setup)



```bash

cd ~/Downloads/universal-literature-screening-toolkit

chmod +x scripts/setup_unix.sh scripts/run_tool.sh scripts/run_tests.sh### Windows**💡 Tip:** This is a lean tutorial focusing on the essential steps. For detailed explanations, troubleshooting, and advanced features, see the comprehensive [USER_GUIDE.md](USER_GUIDE.md).

./scripts/setup_unix.sh

python3 -m pytest tests -q

```

Open PowerShell (`Win+X` → PowerShell), navigate to the toolkit folder, and run:- How to organize your PDF files- How to organize your PDF files

✅ **Expected:** Tests passed



❌ **Issues?** See [Troubleshooting](USER_GUIDE.md#troubleshooting) in USER_GUIDE.md

```powershell---

---

cd C:\Users\YourName\Downloads\universal-literature-screening-toolkit

## 2. Prepare PDFs

Set-ExecutionPolicy Bypass -Scope Process- How to write a simple search query- How to write a simple search query

### Create Input Folder

.\scripts\setup_windows.ps1

**Windows:**

```powershell.\scripts\run_tests.ps1## What You'll Do

New-Item -ItemType Directory -Name "input_pdfs" -Force

``````



**macOS/Linux:**- How to run the screening and view results- How to run the screening and view results

```bash

mkdir -p input_pdfs### macOS/Linux

```

Here's a quick overview of the screening process:

### Add PDFs

Open Terminal and run:

Copy all PDF files into the `input_pdfs/` folder.



**Rules:**

- All PDFs directly in `input_pdfs/` (no subfolders)```bash

- Any file names work

- Folder must be named exactly `input_pdfs`cd ~/Downloads/universal-literature-screening-toolkit1. **Install the toolkit** → Set up Python and required libraries (one-time, ~5 minutes)



---chmod +x scripts/setup_unix.sh scripts/run_tool.sh scripts/run_tests.sh



## 3. Write Query./scripts/setup_unix.sh2. **Prepare your PDFs** → Organize research papers in a folder (~2 minutes)**Need more details?** See the full USER_GUIDE.md for advanced features and troubleshooting.**Need more details?** See the full USER_GUIDE.md for advanced features and troubleshooting.



Create `query.txt` in the toolkit folder.python3 -m pytest tests -q



**Simple example:**```3. **Write your query** → Define which papers to include/exclude (~3 minutes)

```

forest* AND climate*

```

✅ **Expected output:** "All tests passed successfully!"4. **Run the screening** → Let the toolkit process your papers (~1-2 seconds per paper)## Troubleshooting (plain language)

**Complex example:**

```

(forest* OR woodland*) AND ("ecosystem service*" OR biodiversity) AND NOT economics

```❌ **Having issues?** See [Troubleshooting](USER_GUIDE.md#troubleshooting) in USER_GUIDE.md5. **Review results** → Check the HTML report and sorted papers (~5 minutes)



**Syntax:**

- `*` = wildcard (e.g., `forest*` matches forest, forests, forestry)

- `"phrase"` = exact phrase------

- `AND` = both required

- `OR` = either required

- `NOT` = exclude

- `(parentheses)` = group terms## 2. Prepare Your PDFs (2 Minutes)**What is this toolkit?** Think of it as an automated assistant that reads all your research papers and tells you which ones match your specific criteria—saving you hours of manual screening work.



More examples: [Query Syntax Guide](USER_GUIDE.md#query-syntax)



---### Create Input Folder### Setup Issues



## 4. Run Screening



**Windows:****Windows:**---

```powershell

.\scripts\run_tool.ps1 -QueryFile "query.txt"```powershell

```

New-Item -ItemType Directory -Name "input_pdfs" -Force## 📋 What You'll Need

**macOS/Linux:**

```bash```

./scripts/run_tool.sh --query-file "query.txt"

```## Step 1: Install and Verify



**Alternative (all platforms):****macOS/Linux:**

```bash

python run_screening.py --input input_pdfs --output results --query-file query.txt```bash**❌ "Python not found" or "'python' is not recognized"**

```

mkdir -p input_pdfs

---

```### 📁 Understanding Folder Structure

## 5. View Results



Open `results/validation_report.html` in your web browser.

### Add Your PDFsBefore starting, make sure you have:- **Cause**: Python not installed or not in PATH

**Results structure:**

```

results/

├─ validation_report.html    ← Your reportCopy all PDF files you want to screen into the `input_pdfs/` folder.The toolkit needs files organized in a specific way. Here's what your folder should look like:

├─ validation_results.json   ← Raw data

└─ sorted_pdfs/

   ├─ include/               ← Matched papers

   └─ exclude/               ← Excluded papers**Rules:**- **A computer** running Windows, macOS, or Linux- **Solution**: 

```

- ✅ All PDFs directly in `input_pdfs/` (no subfolders)

**Report shows:**

- Summary statistics (total, included, excluded)- ✅ Any file names are fine```

- Included papers with matched terms and evidence

- Your search query- ⚠️ Folder name must be exactly `input_pdfs`



---universal-literature-screening-toolkit/     ← Main folder (you'll download/clone this)- **PDF files** of the research papers you want to screen  1. Download Python from [python.org](https://www.python.org/downloads/)



## Next Steps---



✅ You've completed your first screening!├─ input_pdfs/                              ← You'll create this folder for your PDFs



**Now:**## 3. Write Your Query (3 Minutes)

1. Review included papers

2. Refine query if needed│  ├─ paper1.pdf                           ← Your PDF files (any names are fine)- **Internet connection** for the one-time setup  2. During installation, **check "Add Python to PATH"**

3. Run again with improved criteria

### Create Query File

**Learn more:**

- [USER_GUIDE.md](USER_GUIDE.md) - Comprehensive reference│  ├─ paper2.pdf

  - Troubleshooting

  - FAQCreate a file named `query.txt` in the toolkit folder with your search criteria.

  - Advanced query techniques

  - Configuration options│  └─ paper3.pdf- **15 minutes** for installation and your first screening  3. Restart PowerShell

  - Best practices

**Simple example:**

**Get help:**

- [USER_GUIDE.md](USER_GUIDE.md) - Documentation```├─ query.txt                                ← You'll create this file with your search query

- [GitHub Issues](https://github.com/uhiltner/universal-literature-screening-toolkit/issues) - Report bugs

forest* AND climate*

---

```├─ scripts/                                 ← Helper scripts (already included)  4. Try `py --version` instead of `python --version`

Happy screening! 📚✨



**Complex example:**│  ├─ setup_windows.ps1

```

(forest* OR woodland*) AND ("ecosystem service*" OR biodiversity) AND NOT economics│  └─ run_tool.ps1---

```

└─ run_screening.py                         ← Main program (already included)

### Query Syntax

```**❌ "Execution Policy" error in PowerShell**

- `*` = wildcard (e.g., `forest*` matches forest, forests, forestry)

- `"exact phrase"` = match exact phrase

- `AND` = both terms required

- `OR` = either term required**Important to know:**## Step 1: Install the Toolkit (One-Time Setup)- **Cause**: Windows blocks unsigned scripts by default

- `NOT` = exclude papers with this term

- `(parentheses)` = group terms- ✅ Your **PDF files can have any names** you want



💡 **More examples:** See [Query Syntax Guide](USER_GUIDE.md#query-syntax) in USER_GUIDE.md- ⚠️ The **folder `input_pdfs` must be named exactly** that (lowercase, with underscore)- **Solution**: Run `Set-ExecutionPolicy Bypass -Scope Process` before setup



---- ⚠️ The **query file must be named `query.txt`** (unless you specify a different name later)



## 4. Run the Screening (1 Minute)- 📍 Everything must be in the same location as `run_screening.py`### 📁 Understanding the Folder Structure- **Note**: This only affects the current PowerShell window (safe)



### Windows

```powershell

.\scripts\run_tool.ps1 -QueryFile "query.txt"### Windows Setup (PowerShell)

```



### macOS/Linux

```bash**What is PowerShell?** It's a command-line tool built into Windows. Don't worry—you just need to copy and paste a few commands!The toolkit needs files organized in a specific way. Here's what it looks like:**❌ "pip not found" or installation fails**

./scripts/run_tool.sh --query-file "query.txt"

```



### Alternative (All Platforms)**Step 1: Open PowerShell**- **Cause**: pip not installed or environment issues

```bash

python run_screening.py --input input_pdfs --output results --query-file query.txt- Press `Windows Key + X` on your keyboard

```

- Click "Windows PowerShell" or "Terminal"```- **Solution**: Re-run `.\scripts\setup_windows.ps1` which fixes pip automatically

**Processing time:** ~1-2 seconds per PDF

- A blue or black window will open

---

universal-literature-screening-toolkit/     ← Main folder (you downloaded this)

## 5. View Results (2 Minutes)

**Step 2: Navigate to the toolkit folder**

Open `results/validation_report.html` in your web browser.

```powershell├─ input_pdfs/                              ← Put your PDF files here (you'll create this)### Folder and File Issues

### Results Structure

# Replace "YourName" with your actual Windows username

```

results/# Replace the path if you put the toolkit somewhere else│  ├─ paper1.pdf

├─ validation_report.html      ← Your screening report

├─ validation_results.json     ← Raw datacd C:\Users\YourName\Downloads\universal-literature-screening-toolkit

└─ sorted_pdfs/

   ├─ include/                 ← Papers that matched```│  ├─ paper2.pdf**❌ "No PDFs found in input_pdfs"**

   └─ exclude/                 ← Papers that didn't match

```



### The Report Shows**Tip:** If you don't know where you unzipped the toolkit, right-click the folder in File Explorer and select "Copy as path", then paste it after `cd `.│  └─ paper3.pdf- **Check 1**: Folder named exactly `input_pdfs` (not `Input_PDFs` or `input-pdfs`)



- **Summary:** Total papers, included/excluded counts

- **Included papers table:** Which terms matched, text snippets

- **Your query:** Search criteria used**Step 3: Allow PowerShell to run the installer**├─ query.txt                                ← Your search query (you'll create this)- **Check 2**: PDFs are directly in the folder (not in a subfolder)



**Next:** Manually review the included papers to confirm they're relevant.```powershell



---Set-ExecutionPolicy Bypass -Scope Process├─ scripts/                                 ← Helper programs (already included)- **Check 3**: Files have `.pdf` extension (not `.PDF` or `.pdf.txt`)



## Next Steps```



🎉 **You've completed your first screening!**└─ run_screening.py                         ← Main program (already included)



### Improve Your Results
**What does this do?** Windows blocks scripts for security by default. This command allows scripts to run in this PowerShell window only—it's safe and doesn't change your computer's security settings permanently.



1. Review the included papers```**❌ "query.txt not found"**

2. Refine your query if needed

3. Run screening again**Step 4: Run the automated setup**



### Learn More```powershell- **Check 1**: File is named exactly `query.txt` (not `Query.txt` or `query.txt.txt`)



See [USER_GUIDE.md](USER_GUIDE.md) for:.\scripts\setup_windows.ps1

- **Troubleshooting** → Common errors and solutions

- **FAQ** → Quick answers to common questions```**Important Notes:**- **Check 2**: File is in the same folder as `run_screening.py`

- **Advanced Query Techniques** → Complex search strategies

- **Configuration Options** → Customize the toolkit

- **Best Practices** → Tips from experienced users

**What happens now?** The script will:- ✅ Your **PDF files can have any names** you want- **Solution**: Specify custom path: `--query-file "path/to/my_query.txt"`

### Get Help

- Check if Python is installed (if not, it will guide you to install it)

- 📖 [USER_GUIDE.md](USER_GUIDE.md) - Comprehensive documentation

- 🐛 [GitHub Issues](https://github.com/uhiltner/universal-literature-screening-toolkit/issues) - Report bugs- Create a safe, isolated environment for the toolkit- ⚠️ The **folder names must be exact**: `input_pdfs` (not `Input_PDFs` or `pdfs`)



---- Install required software libraries



**Happy screening!** 📚✨- This takes 2-3 minutes- ⚠️ The **query file must be named**: `query.txt` (unless you specify otherwise)### Processing Issues




**Step 5: Verify everything works**

```powershell

.\scripts\run_tests.ps1### 🪟 Windows Installation**⚠️ "Some PDFs failed to process"**

```

- **This is normal!** Some PDFs can't be processed due to:

**Expected output:** You should see `✅ All tests passed successfully!`

**Step 1: Open PowerShell**  - **Encrypted/Protected**: Password-protected or restricted PDFs

**If you see warnings:** Don't worry! Warnings (in yellow) are not errors. As long as you see "All tests passed", everything is working correctly.

- Press `Windows Key + X`  - **Corrupted**: Damaged file (try re-downloading)

**If something goes wrong:** See the [Troubleshooting section](USER_GUIDE.md#troubleshooting) in the User Guide, or check the [FAQ](USER_GUIDE.md#frequently-asked-questions).

- Click "Windows PowerShell" or "Terminal"  - **Scanned Images**: PDFs without extractable text (need OCR)

### macOS/Linux Setup

- **Check the report**: The HTML report lists exactly which PDFs failed and why

**What is Terminal?** It's the command-line tool for Mac and Linux. You'll use it to run a few simple commands.

**Step 2: Go to the Toolkit Folder**

**Step 1: Open Terminal**

- **macOS:** Press `Cmd + Space`, type "Terminal", press Enter```powershell**❌ "No papers matched the query" (0 included)**

- **Linux:** Press `Ctrl + Alt + T`

# Replace "YourName" with your actual Windows username- **Cause**: Query is too restrictive

**Step 2: Navigate to the toolkit folder**

```bashcd C:\Users\YourName\Downloads\universal-literature-screening-toolkit- **Solutions**:

# Replace with the actual path where you unzipped the toolkit

cd ~/Downloads/universal-literature-screening-toolkit```  1. Add more synonyms with OR: `forest* OR woodland* OR silvicultur*`

```

  2. Use wildcards: `manage*` instead of `management`

**Step 3: Make the setup scripts executable**

```bash**Step 3: Allow PowerShell to Run the Installer**  3. Remove NOT clauses temporarily

chmod +x scripts/setup_unix.sh scripts/run_tool.sh scripts/run_tests.sh

``````powershell  4. Try searching for just one concept first



**What does this do?** This tells your computer that these files are programs that can be run.Set-ExecutionPolicy Bypass -Scope Process  5. See USER_GUIDE.md - Refining Search Strings section



**Step 4: Run the automated setup**```

```bash

./scripts/setup_unix.sh**Don't worry!** This is safe. It only affects this PowerShell window and allows our installer to run.**⚠️ "Too many papers matched" (>80% included)**

```

- **Cause**: Query is too broad

**Step 5: Verify everything works**

```bash**Step 4: Run the Installer**- **Solutions**:

python3 -m pytest tests -q

``````powershell  1. Add more AND conditions: `forest* AND management AND "ecosystem service"`



**Expected output:** You should see test results showing tests passed..\scripts\setup_windows.ps1  2. Use exact phrases: `"systematic review"` instead of `review`



---```  3. Add NOT clauses: `AND NOT (economics OR cost*)`



## Step 2: Prepare Your Data  4. See USER_GUIDE.md - Refining Search Strings section



### Create the Input FolderThis will:



You need to create a folder called `input_pdfs` where you'll put all the research papers you want to screen.- Check if Python is installed (and help you install it if needed)---



**Windows (PowerShell):**- Create a safe, isolated environment for the toolkit

```powershell

# Make sure you're still in the toolkit directory- Install all required software libraries## ❓ Frequently Asked Questions (FAQ)

# If you closed PowerShell, repeat Step 2 from above

- Take 2-3 minutes to complete

New-Item -ItemType Directory -Name "input_pdfs" -Force

```### General Questions



**macOS/Linux (Terminal):****Step 5: Verify Everything Works**

```bash

mkdir -p input_pdfs```powershell**Q: Where exactly do I create the `input_pdfs` folder?**

```

.\scripts\run_tests.ps1A: In the same directory as `run_screening.py`. If you're in `C:\Users\YourName\universal-literature-screening-toolkit\`, create `C:\Users\YourName\universal-literature-screening-toolkit\input_pdfs\`.

**Or use your File Explorer/Finder:** You can also just create a new folder called `input_pdfs` using your normal file browser—just make sure it's inside the toolkit folder!

```

### Copy Your PDF Files

**Q: Can PDF files have any name?**

Now, copy all the research papers (PDF files) you want to screen into the `input_pdfs` folder.

**Success looks like:** You'll see `✅ All tests passed successfully!`A: Yes! Your PDFs can have any filename. Only the folder name (`input_pdfs`) and query file (`query.txt`) must be exact.

**Important rules:**

- ✅ Put all PDFs **directly in the `input_pdfs` folder**

- ❌ Don't create subfolders inside `input_pdfs`

- ✅ File names don't matter—name them however you like### 🍎 macOS / 🐧 Linux Installation**Q: Can I use subfolders to organize my PDFs?**



**Example of a correct setup:**A: Not for the first run. The toolkit only reads PDFs directly in `input_pdfs`. (Advanced users can modify `config.json` for recursive searching.)

```

input_pdfs/**Step 1: Open Terminal**

├─ Smith_2020_climate_change.pdf

├─ Jones_forest_management.pdf- macOS: Press `Cmd + Space`, type "Terminal", press Enter**Q: How many PDFs can I process at once?**

├─ my_important_paper.pdf

└─ study_from_2023.pdf- Linux: Press `Ctrl + Alt + T`A: Tested with 100+ PDFs. Processing time is ~1-2 seconds per PDF.

```



---

**Step 2: Go to the Toolkit Folder****Q: What if I have PDFs in multiple languages?**

## Step 3: Write Your Query

```bashA: The toolkit handles Unicode text (German, French, Spanish, Chinese, etc.). Just make sure your query terms match the language of your papers.

### What is a Query?

cd ~/Downloads/universal-literature-screening-toolkit

A query is like a set of rules that tells the toolkit which papers to include or exclude. Think of it as creating a filter for your papers.

```### Setup and Installation

**Example:** "Show me papers that mention forests AND climate change, but NOT economics"



### Create the Query File

**Step 3: Make the Installer Executable****Q: The script says 'Python not found' but I installed it - what's wrong?**

**Step 1: Open a text editor**

- **Windows:** Open Notepad (search for it in the Start Menu)```bashA: Python might not be in your system PATH. Try:

- **macOS:** Open TextEdit

- **Linux:** Open gedit or your preferred text editorchmod +x scripts/setup_unix.sh scripts/run_tool.sh scripts/run_tests.sh1. Close and reopen PowerShell



**Step 2: Write your query**```2. Use `py --version` instead of `python --version`



Here's a simple example to get you started:3. Reinstall Python and check "Add Python to PATH"



```**Step 4: Run the Installer**

# My first literature screening query

# Lines starting with # are comments and won't affect the search```bash**Q: I get 'script execution blocked' - is this dangerous to bypass?**



forest* AND climate*./scripts/setup_unix.shA: No. `Set-ExecutionPolicy Bypass -Scope Process` only affects the current PowerShell window and is safe. It doesn't change system-wide security settings.

```

```

This query will find papers that mention both "forest" (or forests, forestry, etc.) AND "climate" (or climatic, etc.)

**Q: Do I need to run setup every time?**

**Step 3: Save the file**

- Save it as `query.txt` in the toolkit folder (same place as `run_screening.py`)**Step 5: Verify Everything Works**A: No! Setup is one-time. After that, just use `.\scripts\run_tool.ps1` to run screenings.

- **Windows users:** Make sure it's saved as `query.txt`, not `query.txt.txt`!

```bash

### Query Syntax Quick Reference

python3 -m pytest tests -q### Search Query Questions

**Wildcards (`*`):** Match variations of a word

- `forest*` matches: forest, forests, forestry, forestation, forester```



**Exact phrases (`"quotes"`):** Match multi-word terms exactly**Q: Should I use AND or OR between terms?**

- `"climate change"` matches only "climate change", not "climate" alone

**Success looks like:** You'll see messages saying tests passed.A: 

**Combining terms:**

- `AND` = both terms must be in the paper- **OR**: "Find papers with *any* of these terms" → More inclusive, good for initial screening

- `OR` = at least one term must be in the paper

- `NOT` = exclude papers with this term---- **AND**: "Find papers with *all* of these terms" → More restrictive, good for focused screening



**Grouping (`parentheses`):** Control the logic

- `(forest* OR woodland*) AND climate*` means: (forest OR woodland) AND climate

## Step 2: Prepare Your Research Papers**Q: What does the `*` wildcard do?**

### Example Queries

A: It matches any ending. `forest*` matches: forest, forests, forestry, forestation, forester, etc.

**Basic search:**

```### Create the Input Folder

forest* AND management

```**Q: How do I search for an exact phrase?**



**More flexible:****Windows PowerShell:**A: Use double quotes: `"ecosystem services"` (will not match "ecosystem service" or "services to ecosystems")

```

(forest* OR woodland* OR tree*) AND (management OR planning)```powershell

```

# Make sure you're in the toolkit folder**Q: Can I use parentheses to group terms?**

**With exclusions:**

```cd C:\Users\YourName\Downloads\universal-literature-screening-toolkitA: Yes! `(forest* OR wood*) AND (management OR planning)` ensures proper logic.

forest* AND management AND NOT economics

```



**Complex search:**# Create the input_pdfs folder### Results and Output

```

# Find papers about forests with ecosystem services, excluding economic studiesNew-Item -ItemType Directory -Name "input_pdfs" -Force

(forest* OR woodland*) AND ("ecosystem service*" OR biodiversity) AND NOT (economics OR cost*)

``````**Q: Why did the tool include/exclude a specific paper?**



**💡 Tip:** Start with a simple query first. You can always refine it after seeing the results!A: Open `validation_report.html` - it shows exactly which terms matched in each paper, with evidence snippets from the text.



---**macOS/Linux Terminal:**



## Step 4: Run the Tool```bash**Q: Can I re-run with different query without re-processing PDFs?**



Now you're ready to screen your papers! The toolkit will read all your PDFs, check each one against your query, and organize the results.mkdir -p input_pdfsA: Currently no - each run extracts text again. (This feature is planned for future versions.)



### Windows (PowerShell)```



```powershell**Q: Where are my original PDFs after screening?**

# If you closed PowerShell, open it again and navigate to the toolkit folder:

# cd C:\Users\YourName\Downloads\universal-literature-screening-toolkit### Add Your PDF FilesA: They're copied to `results/sorted_pdfs/include` or `exclude\`. Your originals in `input_pdfs` are unchanged.



# Run the screening

.\scripts\run_tool.ps1 -QueryFile "query.txt"

```1. **Copy all your research papers (PDF files)** into the `input_pdfs` folder**Q: No papers matched my query - is the tool broken?**



**What you'll see:** Messages like "Processing papers..." and "Extracted text from paper1.pdf". This is normal!2. **Keep all files in one folder** - don't create subfolders inside `input_pdfs`A: Probably not! Your query might be too restrictive. See USER_GUIDE.md - Refining Search Strings for strategies to adjust your query.



### macOS/Linux (Terminal)3. **File names don't matter** - name them however you like



```bash### PDF Processing Issues

# If you closed Terminal, open it again and navigate to the toolkit folder

**Example of what `input_pdfs` should look like:**

# Run the screening

./scripts/run_tool.sh --query-file "query.txt"```**Q: Why did some PDFs fail to process?**

```

input_pdfs/A: Common reasons:

### Alternative: Direct Python Command (All Platforms)

├─ Smith_2020_climate_change.pdf1. **Encrypted/Password-protected**: Remove protection first

```bash

python run_screening.py --input input_pdfs --output results --query-file query.txt├─ Jones_forest_study.pdf2. **Corrupted file**: Try re-downloading

```

├─ biodiversity_paper.pdf3. **Scanned image (no text)**: Needs OCR preprocessing

### What Happens During Screening?

└─ my_important_paper.pdf4. **Unusual PDF format**: Try opening and re-saving in Adobe Reader

The toolkit will:

1. Read text from each PDF file (~1-2 seconds per paper)```

2. Check if the text matches your query

3. Create a detailed report**Q: How do I know which PDFs failed and why?**

4. Sort papers into "include" and "exclude" folders

---A: Check the HTML report - there's a "Failed PDFs" section at the bottom listing each file with the specific reason.

**How long does it take?** About 1-2 seconds per PDF. So 50 papers = ~1-2 minutes total.



---

## Step 3: Create Your Search Query**Q: Can the tool process scanned PDFs (images)?**

## Step 5: Review Your Results

A: Not currently. Scanned PDFs need OCR (Optical Character Recognition) first. Try Adobe Acrobat or online OCR tools.

After the screening completes, you'll find a new `results` folder with all your screening results!

### What is a Search Query?

### What's in the Results Folder?

**Q: Some of my papers are in German/French/Chinese - will this work?**

```

results/A search query tells the toolkit which papers to include or exclude. It's like a Google search, but more precise.A: Yes! The toolkit handles any Unicode text. Just make sure your query includes terms in the same language as your papers.

├─ validation_report.html      ← Open this in your web browser!

├─ validation_results.json     ← Raw data (for advanced users)

└─ sorted_pdfs/

   ├─ include/                 ← Papers that matched your query**Think of it this way:**### Research Workflow

   └─ exclude/                 ← Papers that didn't match

```- "Show me papers about **forests** AND **management**"



### Understanding the HTML Report- "Include papers about **climate** OR **weather**"**Q: Should I manually review all included papers?**



**Double-click `validation_report.html`** to open it in your web browser (Chrome, Firefox, Edge, Safari—any browser works).- "Exclude papers about **economics**"A: Yes! Automated screening is just the first step. Always manually review included papers for final inclusion decisions.



The report shows:



**1. Summary Statistics**### Create the Query File**Q: How accurate is the screening?**

```

Total Papers: 50A: Accuracy depends on your query quality. Well-designed queries achieve 85-95% precision. Always validate with manual review.

✅ Included: 12 (24%)

❌ Excluded: 38 (76%)**Windows:**

```

1. Open Notepad (search for it in Start Menu)**Q: Can I use this for full-text screening?**

**2. Detailed Results Table**

- Lists every paper that was included2. Type your search query (see examples below)A: The toolkit focuses on abstracts and keywords for speed. For full-text analysis, consider after initial screening.

- Shows which search terms matched

- Displays text snippets from the paper showing the matches3. Save as: `query.txt` in the toolkit folder



**3. Your Query****Q: How do I handle duplicates?**

- Shows exactly what query was used

- Helps you remember your search criteria**macOS/Linux:**A: Run duplicate detection *before* screening using tools like Zotero, Mendeley, or Covidence.



### What to Do Next1. Open TextEdit (Mac) or gedit (Linux)



1. **Open the HTML report** to see your results2. Type your search query---

2. **Check the included papers** in `results/sorted_pdfs/include/`

3. **Manually review** a few papers to confirm they're relevant3. Save as: `query.txt` in the toolkit folder

4. **Refine if needed:** If too many or too few papers matched, adjust your query and run again

**💡 Pro Tip**: The toolkit works best when you iterate! Start broad, review results, refine your query, and run again. This is exactly how expert screeners work - the tool just makes it 100x faster.at you’ll do

**Important:** Automated screening is just the first step! You should always manually review the included papers to make your final inclusion decisions.

### Simple Query Examples

---

- Put your PDFs into a folder (default: input_pdfs)

## Try an Example

**Example 1: Basic Search (Find papers about forests AND climate)**- Write one Boolean query (query.txt)

We've included a sample query file you can try right away to see how the toolkit works!

```- Run the tool and review a clean HTML report

**Windows:**

```powershellforest* AND climate*

.\scripts\run_tool.ps1 -InputPath "input_pdfs" -OutputPath "example_results" -QueryFile "examples\dss4es_search_terms.txt"

``````## 1) Install and verify



**macOS/Linux:**

```bash

./scripts/run_tool.sh --input "input_pdfs" --output "example_results" --query-file "examples/dss4es_search_terms.txt"**Example 2: Flexible Search (Find papers about forests OR woodlands)**### 📁 Important: Folder Structure and Naming

```

```

This will create a separate `example_results` folder so you can see how the output looks without affecting your main results.

(forest* OR woodland* OR tree*)**⚠️ CRITICAL**: The toolkit is **path-sensitive** and requires specific folder and file names. Follow this structure exactly:

---

```

## Next Steps

```

**🎉 Congratulations!** You've completed your first literature screening!

**Example 3: Exclude Topics (Find forest papers, but exclude economics)**C:\Users\YourName\universal-literature-screening-toolkit\

### What to do now:

```├─ input_pdfs\              ⬅️ MUST be named exactly "input_pdfs"

1. **Review your results** carefully—automated screening is just the beginning

2. **Refine your query** if you got too many or too few matchesforest* AND NOT economics│  ├─ paper1.pdf           ⬅️ PDF files can have any name

3. **Run again** with improved criteria

4. **Learn more:** Check out the [USER_GUIDE.md](USER_GUIDE.md) for:```│  ├─ study_forest.pdf     ⬅️ PDF files can have any name

   - Detailed troubleshooting

   - FAQ (Frequently Asked Questions)│  └─ another_doc.pdf      ⬅️ PDF files can have any name

   - Advanced query techniques

   - Tips for refining search strategies**Example 4: Complex Search (Multiple concepts)**├─ query.txt                ⬅️ MUST be named exactly "query.txt" (or specify with --query-file)

   - Complex use cases and workflows

```├─ scripts\                 ⬅️ Don't modify these

### Need Help?

# This is a comment - it won't affect the search│  ├─ setup_windows.ps1

**Having problems?** 

- 📖 See the [Troubleshooting section](USER_GUIDE.md#troubleshooting) in the User Guide# Find papers about: forests with ecosystem services, but not about economics│  └─ run_tool.ps1

- ❓ Check the [FAQ](USER_GUIDE.md#frequently-asked-questions) for quick answers

- 🐛 Report bugs on GitHub: [Issues page](https://github.com/uhiltner/universal-literature-screening-toolkit/issues)└─ run_screening.py         ⬅️ Main program



### Pro Tips(forest* OR woodland*) AND ("ecosystem service*" OR biodiversity) AND NOT (economics OR cost*)```



**💡 Iterate your query:** Most researchers run screening 2-3 times with different queries before finding the right balance. Start broad, review results, then make it more specific.```



**💡 Test with known papers:** If you have 5-10 papers you know should be included, run your query and check if they match. If not, adjust your query.**Key Rules:**



**💡 Document your process:** Keep notes on your queries and results. This is important for the "Methods" section of your systematic review paper.### Query Syntax Explained- ✅ **PDF files**: Can have any name you want



---- ❌ **Folders**: Must be named exactly as shown (`input_pdfs`, `scripts`)



**Thank you for using the Universal Literature Screening Toolkit!** We hope it saves you hours of manual screening work. Happy researching! 📚✨**For beginners, remember these 4 rules:**- ❌ **Query file**: Must be named `query.txt` (or specify a custom name with `--query-file`)



*For detailed documentation, advanced features, and comprehensive troubleshooting, see [USER_GUIDE.md](USER_GUIDE.md)*- ❌ **Location**: The `input_pdfs` folder must be in the same directory as `run_screening.py`


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
