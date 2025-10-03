# Universal Literature Screening Toolkit (ULST)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17063676.svg)](https://doi.org/10.5281/zenodo.17063676)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**Automate the initial screening of systematic literature reviews** - Process hundreds of research papers in minutes instead of hours!

---

## 🚀 Complete Beginner? Start Here!

**Never used a command-line tool before?** No problem! This guide will walk you through everything.

### Step 1: Get the Toolkit on Your Computer

**Option A: Download as ZIP (Recommended for beginners)**

1. Click the green **`<> Code`** button at the top of this GitHub page
2. Select **"Download ZIP"**
3. **Unzip/Extract the file**:
   - **Windows**: Right-click the downloaded ZIP file → "Extract All..." → Choose a location (e.g., `Downloads` folder)
   - **Mac**: Double-click the ZIP file (it extracts automatically)
   - **Linux**: Right-click → "Extract Here"

4. Remember where you saved it! You'll need this location later.

**Option B: Clone with Git** (For users who know Git)
```bash
git clone https://github.com/uhiltner/universal-literature-screening-toolkit.git
```

### Step 2: Understand the Documentation Files

This toolkit includes three important documentation files (all ending in `.md`):

| File | What It Does | When to Read It |
|------|-------------|-----------------|
| **README.md** (you're here!) | Overview of what the tool does | Read first to understand the toolkit |
| **[QUICK_START.md](QUICK_START.md)** | Step-by-step tutorial for your first screening | Follow this to actually use the tool |
| **[USER_GUIDE.md](USER_GUIDE.md)** | Complete reference manual | Refer to this when you need help or want advanced features |

**What are `.md` files?**

`.md` files are **Markdown** files - they're just text files with simple formatting. You can read them in several ways:

- **On GitHub** (easiest): Just click the filename and GitHub shows it nicely formatted
- **In a free text editor like VS Code**: Download [VS Code](https://code.visualstudio.com/), open the file, press `Ctrl+Shift+V` (Windows/Linux) or `Cmd+Shift+V` (Mac) to see formatted preview
- **In any text editor**: Notepad (Windows), TextEdit (Mac), gedit (Linux) - you'll see the raw text
- **Online Markdown viewer**: Upload to [Dillinger.io](https://dillinger.io/) or similar

### Step 3: Your Learning Path

**👉 Recommended order for beginners:**

1. ✅ **You are here!** Read this README to understand what the tool does (5-10 minutes)
2. **Next:** Open [QUICK_START.md](QUICK_START.md) and follow the step-by-step tutorial (15-20 minutes)
3. **Later:** Bookmark [USER_GUIDE.md](USER_GUIDE.md) for when you need troubleshooting or advanced features

**Ready to start?** → **[Go to QUICK_START.md now!](QUICK_START.md)** 🚀

---

## 📖 What Does This Toolkit Do?

### The Problem

Systematic literature reviews require reading hundreds or thousands of research papers to find the ones relevant to your study. **Manual screening is:**
- ⏰ **Time-consuming**: Hours or days of tedious reading
- 😓 **Exhausting**: Attention fatigue leads to mistakes
- ❌ **Inconsistent**: Subjective decisions vary over time
- 📝 **Hard to document**: Difficult to prove your methodology was rigorous

### The Solution

The **Universal Literature Screening Toolkit** automates the first screening step:

1. **You define criteria once** (e.g., "papers about forests AND climate change, but NOT economics")
2. **The toolkit reads all your PDFs** automatically (100 papers in ~2 minutes)
3. **You get organized results** - papers sorted into include/exclude folders with a detailed report

**Think of it as:** A tireless research assistant who reads hundreds of papers in minutes and never gets inconsistent!

### What It Does ✅

- **Extracts text from PDF files** - Reads research papers automatically
- **Applies your search criteria** - Uses Boolean logic (AND/OR/NOT) just like database searches
- **Handles multiple languages** - Works with English, German, French, Spanish, Chinese, etc.
- **Creates detailed reports** - Shows exactly why each paper was included/excluded
- **Sorts papers automatically** - Copies PDFs into include/exclude folders
- **Ensures reproducibility** - Same criteria applied consistently to every paper

### What It Doesn't Do ❌

- **Replace human judgment** - You still need to manually review included papers
- **Assess research quality** - Doesn't judge if a study is "good" or "bad"
- **Read full 50-page papers** - Focuses on abstracts/key sections for speed
- **Manage citations** - Use tools like Zotero, Mendeley, or Covidence for reference management

---

## 💡 How It Works: A Simple Example

**Scenario:** You're researching forest management and ecosystem services. You downloaded 200 PDF reports from various websites.

**Step 1 - Define Your Criteria (in query.txt):**
```
((forest* OR wood*) AND management) AND "ecosystem service*" AND NOT economics
```

**Step 2 - Run the Toolkit:**
```bash
python run_screening.py --input input_pdfs --output results --query-file query.txt
```

**Step 3 - Get Results (in ~3 minutes):**
- `results/validation_report.html` - Beautiful report showing which papers matched
- `results/sorted_pdfs/include/` - Papers that met your criteria (e.g., 45 papers)
- `results/sorted_pdfs/exclude/` - Papers that didn't match (e.g., 155 papers)

**Time saved:** Instead of manually reading 200 abstracts (8-10 hours), you get organized results in 3 minutes!

---

## 🎯 Who Should Use This?

**This toolkit is perfect for:**
- 🎓 **Graduate students** conducting systematic reviews for theses/dissertations
- 🔬 **Researchers** screening large volumes of literature
- 📚 **Librarians** helping with evidence synthesis projects
- 🌍 **Anyone** working with gray literature (government reports, technical documents, etc.)

**Domain-agnostic:** Works for any field - medicine, environmental science, social sciences, engineering, etc.

---

## 🌟 Key Features

### 1. Flexible Boolean Query System
Define complex inclusion/exclusion criteria using familiar search syntax:
- **AND/OR/NOT operators** - Combine concepts with Boolean logic
- **Wildcards (`*`)** - Match word variations: `forest*` matches forest, forests, forestry
- **Exact phrases (`"quotes"`)** - Match specific multi-word terms
- **Parentheses grouping** - Control logic precedence

### 2. Multi-Language Support
Process papers in any language with Unicode text support:
- English, German, French, Spanish, Chinese, Japanese, etc.
- Case-insensitive matching
- Handles special characters and diacritics

### 3. Robust PDF Processing
Dual-library approach ensures reliable text extraction:
- Primary: PyMuPDF (fast, handles most PDFs)
- Fallback: pdfplumber (handles complex layouts)
- Error categorization: Clearly identifies encrypted, corrupted, or scanned PDFs

### 4. Professional Reporting
Multiple output formats for different needs:
- **HTML report** - Visual, easy to read, perfect for sharing
- **JSON files** - Machine-readable data for further analysis
- **Sorted PDF folders** - Organized copies of papers ready for next steps

### 5. Reproducible & Auditable
Complete documentation trail:
- Exact query used is logged
- Every decision is documented with evidence
- Text snippets show exactly why papers matched
- Failed PDFs are tracked with specific error reasons

---

## 📊 Real-World Example: Environmental Science

**Challenge:** A researcher needs to review regional environmental impact reports (gray literature) from various governmental websites. These sites have limited search capabilities, so 500 PDF reports were downloaded based on simple title searches.

**Task:** Find reports that discuss forest management with ecosystem services focus, but exclude purely economic studies.

**Traditional Manual Approach:**
- Time: 25-30 hours
- Risk: Inconsistency after hours of reading
- Documentation: Difficult to prove systematic methodology

**Using ULST:**

1. **Define criteria in `query.txt`:**
   ```
   ((forest* OR woodland*) AND management) 
   AND ("ecosystem service*" OR biodiversity) 
   AND NOT (economics OR cost*)
   ```

2. **Run screening:**
   ```bash
   python run_screening.py --input input_pdfs --output results --query-file query.txt
   ```

3. **Results (in ~10 minutes):**
   - 500 PDFs processed
   - 87 papers included for manual review
   - 413 papers excluded with documented reasons
   - HTML report shows evidence for every decision

4. **Outcome:**
   - ⏱️ Time saved: ~25 hours
   - ✅ Consistency: Same criteria applied to all 500 papers
   - 📝 Audit trail: Complete documentation for methodology section
   - 🎯 Focus: Manual review only on relevant 87 papers

---

## 🔧 Technical Details

**Requirements:**
- Python 3.8 or higher
- ~500 MB disk space
- Windows, macOS, or Linux

**Key Dependencies:**
- PyMuPDF (fitz) - Primary PDF text extraction
- pdfplumber - Fallback PDF extraction
- pyparsing - Boolean query parsing
- regex - Advanced pattern matching

**Processing Speed:**
- ~1-2 seconds per PDF (typical)
- 100 PDFs ≈ 2-3 minutes
- 500 PDFs ≈ 10-15 minutes

**Limitations:**
- Requires extractable text (scanned PDFs need OCR preprocessing)
- Password-protected PDFs must be unlocked first
- Focuses on abstracts/keywords for speed (not full-text deep analysis)

---

## 📚 Documentation Overview

| Document | Purpose | Best For |
|----------|---------|----------|
| **README.md** (this file) | Overview, technical details, examples | Understanding what the tool does and why |
| **[QUICK_START.md](QUICK_START.md)** | Step-by-step beginner tutorial | Your first screening (15-20 min) |
| **[USER_GUIDE.md](USER_GUIDE.md)** | Comprehensive reference manual | Troubleshooting, FAQ, advanced features |

**→ Ready to start?** **[Go to QUICK_START.md](QUICK_START.md)** for your first screening!

---

## 📄 Citation

If you use this toolkit in your research, please cite:

```bibtex
@software{hiltner2025universal,
  author       = {Hiltner, Ulrike},
  title        = {Universal Literature Screening Toolkit},
  month        = sep,
  year         = 2025,
  version      = {1.0.3},
  url          = {https://github.com/uhiltner/universal-literature-screening-toolkit}
}
```

---

## 🤝 Contributing

We welcome contributions! Please see:
- [CONTRIBUTING.md](CONTRIBUTING.md) - How to contribute
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - Community guidelines

---

## 📜 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

## 🆘 Need Help?

- **First screening:** Follow [QUICK_START.md](QUICK_START.md)
- **Troubleshooting:** See [USER_GUIDE.md - Troubleshooting](USER_GUIDE.md#troubleshooting)
- **Questions:** See [USER_GUIDE.md - FAQ](USER_GUIDE.md#frequently-asked-questions)
- **Bug reports:** [Open an issue on GitHub](https://github.com/uhiltner/universal-literature-screening-toolkit/issues)

**Good luck with your literature review!** 📚✨
