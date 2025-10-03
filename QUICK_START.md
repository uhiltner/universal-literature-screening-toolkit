# 🚀 Quick Start Guide — Universal Literature Screening Toolkit

**Complete beginner?** This step-by-step tutorial will guide you from installation to your first successful screening in about 15-20 minutes.

**💡 Tip:** This is a lean tutorial focusing on essential steps. For troubleshooting, FAQ, and advanced features, see the comprehensive **[USER_GUIDE.md](USER_GUIDE.md)**.

---

## What You'll Do

Here's a quick overview of the screening process:

1. **Install the toolkit** → Set up Python and required libraries (one-time, ~5 minutes)
2. **Prepare your PDFs** → Organize research papers in a folder (~2 minutes)
3. **Write your query** → Define which papers to include/exclude (~3 minutes)
4. **Run the screening** → Let the toolkit process your papers (~1-2 seconds per paper)
5. **Review results** → Check the HTML report and sorted papers (~5 minutes)

**Total time:** ~15 minutes + processing time

---

## 📋 What You'll Need

Before starting, make sure you have:

- **A computer** running Windows, macOS, or Linux
- **PDF files** of the research papers you want to screen
- **Internet connection** for the one-time setup
- **15 minutes** for installation and your first screening

---

## Step 1: Install the Toolkit (One-Time Setup)

### 📁 Understanding the Folder Structure

The toolkit needs files organized in a specific way. Here's what it looks like:

```
universal-literature-screening-toolkit/     ← Main folder (you downloaded this)
├─ input_pdfs/                              ← Put your PDF files here (you'll create this)
│  ├─ paper1.pdf                           ← Your PDF files (any names are fine)
│  ├─ paper2.pdf
│  └─ paper3.pdf
├─ query.txt                                ← Your search query (you'll create this)
├─ scripts/                                 ← Helper programs (already included)
│  ├─ setup_windows.ps1
│  └─ run_tool.ps1
└─ run_screening.py                         ← Main program (already included)
```

**Important to know:**
- ✅ Your **PDF files can have any names** you want
- ⚠️ The **folder `input_pdfs` must be named exactly** that (lowercase, with underscore)
- ⚠️ The **query file must be named** `query.txt` (unless you specify otherwise)
- 📍 Everything must be in the same location as `run_screening.py`

### 🪟 Windows Installation

**What is PowerShell?** It's a command-line tool built into Windows. Don't worry—you just need to copy and paste a few commands!

**Step 1: Open PowerShell**

- Press `Windows Key + X` on your keyboard
- Click "Windows PowerShell" or "Terminal"
- A blue or black window will open

**Step 2: Go to the Toolkit Folder**

```powershell
# Replace "YourName" with your actual Windows username
# Replace the path if you put the toolkit somewhere else
cd C:\Users\YourName\Downloads\universal-literature-screening-toolkit
```

**Tip:** If you don't know where you unzipped the toolkit, right-click the folder in File Explorer and select "Copy as path", then paste it after `cd `.

**Step 3: Allow PowerShell to Run the Installer**

```powershell
Set-ExecutionPolicy Bypass -Scope Process
```

**What does this do?** Windows blocks scripts for security by default. This command allows scripts to run in this PowerShell window only—it's safe and doesn't change your computer's security settings permanently.

**Step 4: Run the Installer**

```powershell
.\scripts\setup_windows.ps1
```

**What happens now?** The script will:
- Check if Python is installed (and help you install it if needed)
- Create a safe, isolated environment for the toolkit
- Install all required software libraries
- Take 2-3 minutes to complete

**Step 5: Verify Everything Works**

```powershell
.\scripts\run_tests.ps1
```

**Success looks like:** You'll see `✅ All tests passed successfully!`

**If you see warnings:** Don't worry! Warnings (in yellow) are not errors. As long as you see "All tests passed", everything is working correctly.

**If something goes wrong:** See the [Troubleshooting section](USER_GUIDE.md#troubleshooting) in the User Guide, or check the [FAQ](USER_GUIDE.md#frequently-asked-questions).

### 🍎 macOS / 🐧 Linux Installation

**What is Terminal?** It's the command-line tool for Mac and Linux. You'll use it to run a few simple commands.

**Step 1: Open Terminal**

- **macOS:** Press `Cmd + Space`, type "Terminal", press Enter
- **Linux:** Press `Ctrl + Alt + T`

**Step 2: Go to the Toolkit Folder**

```bash
# Replace with the actual path where you unzipped the toolkit
cd ~/Downloads/universal-literature-screening-toolkit
```

**Step 3: Make the Installer Executable**

```bash
chmod +x scripts/setup_unix.sh scripts/run_tool.sh scripts/run_tests.sh
```

**What does this do?** This tells your computer that these files are programs that can be run.

**Step 4: Run the Installer**

```bash
./scripts/setup_unix.sh
```

**Step 5: Verify Everything Works**

```bash
python3 -m pytest tests -q
```

**Success looks like:** You'll see messages saying tests passed.

---

## Step 2: Prepare Your Research Papers

### Create the Input Folder

You need to create a folder called `input_pdfs` where you'll put all the research papers you want to screen.

**Windows (PowerShell):**
```powershell
# Make sure you're still in the toolkit directory
# If you closed PowerShell, repeat Step 2 from above

New-Item -ItemType Directory -Name "input_pdfs" -Force
```

**macOS/Linux (Terminal):**
```bash
mkdir -p input_pdfs
```

**Or use your File Explorer/Finder:** You can also just create a new folder called `input_pdfs` using your normal file browser—just make sure it's inside the toolkit folder!

### Copy Your PDF Files

Now, copy all the research papers (PDF files) you want to screen into the `input_pdfs` folder.

**Important rules:**
- ✅ Put all PDFs **directly in the `input_pdfs` folder**
- ❌ Don't create subfolders inside `input_pdfs`
- ✅ File names don't matter—name them however you like

**Example of a correct setup:**
```
input_pdfs/
├─ Smith_2020_climate_change.pdf
├─ Jones_forest_management.pdf
├─ my_important_paper.pdf
└─ study_from_2023.pdf
```

---

## Step 3: Create Your Search Query

### What is a Search Query?

A search query tells the toolkit which papers to include or exclude. It's like a Google search, but more precise.

**Think of it this way:**
- "Show me papers about **forests** AND **management**"
- "Include papers about **climate** OR **weather**"
- "Exclude papers about **economics**"

### Create the Query File

**Step 1: Open a text editor**

- **Windows:** Open Notepad (search for it in the Start Menu)
- **macOS:** Open TextEdit
- **Linux:** Open gedit or your preferred text editor

**Step 2: Write your query**

Here's a simple example to get you started:

```
# My first literature screening query
# Lines starting with # are comments and won't affect the search

forest* AND climate*
```

This query will find papers that mention both "forest" (or forests, forestry, etc.) AND "climate" (or climatic, etc.)

**Step 3: Save the file**

- Save it as `query.txt` in the toolkit folder (same place as `run_screening.py`)
- **Windows users:** Make sure it's saved as `query.txt`, not `query.txt.txt`!

### Query Syntax Quick Reference

**Wildcards (`*`):** Match variations of a word
- `forest*` matches: forest, forests, forestry, forestation, forester

**Exact phrases (`"quotes"`):** Match multi-word terms exactly
- `"climate change"` matches only "climate change", not "climate" alone

**Combining terms:**
- `AND` = both terms must be in the paper
- `OR` = at least one term must be in the paper
- `NOT` = exclude papers with this term

**Grouping (`parentheses`):** Control the logic
- `(forest* OR woodland*) AND climate*` means: (forest OR woodland) AND climate

### Example Queries

**Basic search:**
```
forest* AND management
```

**More flexible:**
```
(forest* OR woodland* OR tree*) AND (management OR planning)
```

**With exclusions:**
```
forest* AND management AND NOT economics
```

**Complex search:**
```
# Find papers about forests with ecosystem services, excluding economic studies
(forest* OR woodland*) AND ("ecosystem service*" OR biodiversity) AND NOT (economics OR cost*)
```

**💡 Tip:** Start with a simple query first. You can always refine it after seeing the results!

---

## Step 4: Run the Tool

Now you're ready to screen your papers! The toolkit will read all your PDFs, check each one against your query, and organize the results.

### Windows (PowerShell)

```powershell
# If you closed PowerShell, open it again and navigate to the toolkit folder:
# cd C:\Users\YourName\Downloads\universal-literature-screening-toolkit

# Run the screening
.\scripts\run_tool.ps1 -QueryFile "query.txt"
```

**What you'll see:** Messages like "Processing papers..." and "Extracted text from paper1.pdf". This is normal!

### macOS/Linux (Terminal)

```bash
# If you closed Terminal, open it again and navigate to the toolkit folder

# Run the screening
./scripts/run_tool.sh --query-file "query.txt"
```

### Alternative: Direct Python Command (All Platforms)

```bash
python run_screening.py --input input_pdfs --output results --query-file query.txt
```

### What Happens During Screening?

The toolkit will:
1. Read text from each PDF file (~1-2 seconds per paper)
2. Check if the text matches your query
3. Create a detailed report
4. Sort papers into "include" and "exclude" folders

**How long does it take?** About 1-2 seconds per PDF. So 50 papers = ~1-2 minutes total.

---

## Step 5: Review Your Results

After the screening completes, you'll find a new `results` folder with all your screening results!

### What's in the Results Folder?

```
results/
├─ validation_report.html      ← Open this in your web browser!
├─ validation_results.json     ← Raw data (for advanced users)
└─ sorted_pdfs/
   ├─ include/                 ← Papers that matched your query
   └─ exclude/                 ← Papers that didn't match
```

### Understanding the HTML Report

**Double-click `validation_report.html`** to open it in your web browser (Chrome, Firefox, Edge, Safari—any browser works).

The report shows:

**1. Summary Statistics**
```
Total Papers: 50
✅ Included: 12 (24%)
❌ Excluded: 38 (76%)
```

**2. Detailed Results Table**
- Lists every paper that was included
- Shows which search terms matched
- Displays text snippets from the paper showing the matches

**3. Your Query**
- Shows exactly what query was used
- Helps you remember your search criteria

### What to Do Next

1. **Open the HTML report** to see your results
2. **Check the included papers** in `results/sorted_pdfs/include/`
3. **Manually review** a few papers to confirm they're relevant
4. **Refine if needed:** If too many or too few papers matched, adjust your query and run again

**💡 Pro Tip**: The toolkit works best when you iterate! Start broad, review results, refine your query, and run again. This is exactly how expert screeners work - the tool just makes it 100x faster.

**Important:** Automated screening is just the first step! You should always manually review the included papers to make your final inclusion decisions.

---

## Try an Example

We've included a sample query file you can try right away to see how the toolkit works!

**Windows:**
```powershell
.\scripts\run_tool.ps1 -InputPath "input_pdfs" -OutputPath "example_results" -QueryFile "examples\query.txt"
```

**macOS/Linux:**
```bash
./scripts/run_tool.sh --input "input_pdfs" --output "example_results" --query-file "examples/query.txt"
```

This will create a separate `example_results` folder so you can see how the output looks without affecting your main results.

---

## 🎉 Congratulations!

**You've completed your first literature screening!**

### What to do now:

1. **Review your results** carefully—automated screening is just the beginning
2. **Refine your query** if you got too many or too few matches
3. **Run again** with improved criteria
4. **Learn more:** Check out the [USER_GUIDE.md](USER_GUIDE.md) for:
   - Detailed troubleshooting
   - FAQ (Frequently Asked Questions)
   - Advanced query techniques
   - Tips for refining search strategies
   - Complex use cases and workflows

### Need Help?

**Having problems?** 
- 📖 See the [Troubleshooting section](USER_GUIDE.md#troubleshooting) in the User Guide
- ❓ Check the [FAQ](USER_GUIDE.md#frequently-asked-questions) for quick answers
- 🐛 Report bugs on GitHub: [Issues page](https://github.com/uhiltner/universal-literature-screening-toolkit/issues)

### Pro Tips

**💡 Iterate your query:** Most researchers run screening 2-3 times with different queries before finding the right balance. Start broad, review results, then make it more specific.

**💡 Test with known papers:** If you have 5-10 papers you know should be included, run your query and check if they match. If not, adjust your query.

**💡 Document your process:** Keep notes on your queries and results. This is important for the "Methods" section of your systematic review paper.

---

**Thank you for using the Universal Literature Screening Toolkit!** We hope it saves you hours of manual screening work. Happy researching! 📚✨

*For detailed documentation, advanced features, and comprehensive troubleshooting, see [USER_GUIDE.md](USER_GUIDE.md)*
