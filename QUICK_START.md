# Universal Literature Screening Toolkit v2.0 - Quick Start Guide

## 🎯 What This Does
Automatically screens PDF research papers based on your custom search criteria. Perfect for systematic literature reviews in any research domain.

## ⚡ 5-Minute Setup

### Step 1: Install Python
- Download Python 3.8+ from python.org
- During installation, check "Add Python to PATH"

### Step 2: Setup Environment
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate
# OR Activate (Mac/Linux)  
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Prepare Your Data
```
literature_screening_toolkit/
├── input_pdfs/          ← Put your PDF files here (the tool extracts text automatically)
├── search_terms.txt     ← Define your search criteria here
└── results/             ← Results appear here
```

### Step 4: Run Screening
```bash
python run_screening.py --input input_pdfs --output results --search-terms search_terms.txt
```

**What happens:**
1. 📄 **PDF Text Extraction**: Automatically extracts text from PDF files
2. 🔍 **Search Pattern Matching**: Applies your search criteria to extracted text  
3. ✅ **Validation**: Determines include/exclude based on your logic
4. 📊 **Report Generation**: Creates HTML report and organizes results

## 📋 Customize Search Terms

Edit `search_terms.txt`:
```
BLOCK 1: Primary Concept
keyword1*, keyword2, "exact phrase"

BLOCK 2: Context
context1*, domain*, field*

BLOCK 3: Methods
method*, approach*, technique*
```

## 🎨 Choose Template

Use pre-made examples:
```bash
# Medical research
cp examples/medical_literature_terms.txt search_terms.txt

# Environmental science  
cp examples/environmental_science_terms.txt search_terms.txt

# Social science
cp examples/social_science_terms.txt search_terms.txt
```

## 📊 View Results

The toolkit generates:
- `validation_report.html` - Professional visual report
- `validation_results.json` - Data for further analysis
- Organized folders with included/excluded papers

## 🆘 Need Help?

1. Check `user_manual.md` for detailed instructions
2. See `examples/` for domain-specific templates
3. Review `README.md` for complete documentation

## 🌍 Multi-Language Support

The toolkit works with any language:
- Unicode text processing
- Case-insensitive matching  
- Wildcard patterns (`*`)
- Exact phrases (`"quotes"`)

---

**Ready to automate your literature review!** 🚀
