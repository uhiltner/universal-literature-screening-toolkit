# IMPORTANT: PDF Input Workflow Clarification

## 🔧 **How the Toolkit Actually Works**

### **INPUT**: PDF Files
- Place your PDF research papers in the `input_pdfs/` folder
- The toolkit automatically extracts text from PDFs using PyMuPDF or pdfplumber

### **WORKFLOW**:
1. **PDF Text Extraction**: Automatically converts PDFs to text
2. **Search Pattern Matching**: Applies your search criteria  
3. **Validation Logic**: Determines include/exclude based on configuration
4. **Report Generation**: Creates professional HTML reports

### **DEPENDENCIES REQUIRED**:
```bash
pip install PyMuPDF>=1.23.0
pip install pdfplumber>=0.10.0
```

### **CORRECT USAGE**:
```bash
# Put PDF files in input_pdfs/
python run_screening.py --input input_pdfs --output results --search-terms search_terms.txt
```

### **What You Need to Install**:
```bash
pip install -r requirements.txt
```

This will install the PDF extraction libraries needed to process PDF files directly.

## 📋 **File Structure**:
```
input_pdfs/
├── paper1.pdf        ← Your PDF files go here
├── paper2.pdf
└── paper3.pdf

results/
├── extracted_json/   ← Tool creates this automatically
├── validation_report.html
└── validation_results.json
```

The toolkit handles the PDF-to-text conversion automatically - you just need to provide the PDF files!
