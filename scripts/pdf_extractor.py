"""
PDF Extractor Module

Handles PDF text extraction and converts PDFs to JSON format for processing.
Supports multiple PDF extraction methods for maximum compatibility.
"""

import json
import os
from pathlib import Path
import re

# PDF extraction libraries
try:
    import fitz  # PyMuPDF
    PYMUPDF_AVAILABLE = True
except ImportError:
    PYMUPDF_AVAILABLE = False

try:
    import pdfplumber
    PDFPLUMBER_AVAILABLE = True
except ImportError:
    PDFPLUMBER_AVAILABLE = False

def extract_text_with_pymupdf(pdf_path):
    """Extract text using PyMuPDF (primary method)."""
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text.strip()
    except Exception as e:
        print(f"PyMuPDF extraction failed for {pdf_path}: {e}")
        return None

def extract_text_with_pdfplumber(pdf_path):
    """Extract text using pdfplumber (fallback method)."""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text.strip()
    except Exception as e:
        print(f"pdfplumber extraction failed for {pdf_path}: {e}")
        return None

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF using available methods."""
    # Try PyMuPDF first (fastest and most reliable)
    if PYMUPDF_AVAILABLE:
        text = extract_text_with_pymupdf(pdf_path)
        if text and len(text) > 50:  # Reasonable text extracted
            return text
    
    # Fallback to pdfplumber
    if PDFPLUMBER_AVAILABLE:
        text = extract_text_with_pdfplumber(pdf_path)
        if text and len(text) > 50:
            return text
    
    # No extraction possible
    raise Exception("No PDF extraction libraries available. Install PyMuPDF or pdfplumber.")

def clean_extracted_text(text):
    """Clean and normalize extracted text."""
    if not text:
        return ""
    
    # Remove excessive whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove page numbers and common artifacts
    text = re.sub(r'\b\d+\b\s*(?=\n|$)', '', text)  # Standalone numbers
    text = re.sub(r'^\s*\d+\s*$', '', text, flags=re.MULTILINE)  # Page numbers
    
    # Normalize encoding issues - fix smart quotes and similar characters
    text = text.replace(''', "'")  # Left single quote
    text = text.replace(''', "'")  # Right single quote  
    text = text.replace('"', '"')  # Left double quote
    text = text.replace('"', '"')  # Right double quote
    
    return text.strip()

def extract_pdfs_to_json(input_dir, output_dir):
    """
    Extract text from PDF files and save as JSON files.
    
    Args:
        input_dir: Directory containing PDF files
        output_dir: Directory to save JSON files
    
    Returns:
        Number of successfully processed files
    """
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    pdf_files = list(Path(input_dir).glob("*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in {input_dir}")
        return 0
    
    print(f"Found {len(pdf_files)} PDF files to process...")
    
    processed_count = 0
    failed_files = []
    
    for pdf_path in pdf_files:
        try:
            print(f"Processing: {pdf_path.name}")
            
            # Extract text
            full_text = extract_text_from_pdf(pdf_path)
            
            if not full_text or len(full_text) < 100:
                print(f"  Warning: Minimal text extracted from {pdf_path.name}")
                failed_files.append(pdf_path.name)
                continue
            
            # Clean text
            cleaned_text = clean_extracted_text(full_text)
            
            # Create JSON structure
            json_data = {
                "filename": pdf_path.name,
                "pdf_path": str(pdf_path),
                "full_text": cleaned_text,
                "text_length": len(cleaned_text),
                "extraction_method": "PyMuPDF" if PYMUPDF_AVAILABLE else "pdfplumber",
                "extraction_date": "2025-09-05"
            }
            
            # Save JSON file
            json_filename = pdf_path.stem + ".json"
            json_path = Path(output_dir) / json_filename
            
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(json_data, f, ensure_ascii=False, indent=2)
            
            processed_count += 1
            print(f"  ✅ Successfully extracted {len(cleaned_text)} characters")
            
        except Exception as e:
            print(f"  ❌ Failed to process {pdf_path.name}: {e}")
            failed_files.append(pdf_path.name)
    
    print(f"\n📊 Extraction Summary:")
    print(f"  Successful: {processed_count}/{len(pdf_files)} files")
    if failed_files:
        print(f"  Failed: {', '.join(failed_files[:5])}")
        if len(failed_files) > 5:
            print(f"  ... and {len(failed_files) - 5} more")
    
    return processed_count

def load_json_content(json_dir):
    """Load all JSON files from directory."""
    json_files = list(Path(json_dir).glob("*.json"))
    papers = []
    
    for json_path in json_files:
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                papers.append(data)
        except Exception as e:
            print(f"Error loading {json_path.name}: {e}")
    
    print(f"Loaded {len(papers)} papers from JSON files")
    return papers

def get_paper_filename(json_filename):
    """Convert JSON filename back to PDF filename."""
    if json_filename.endswith('.json'):
        return json_filename[:-5] + '.pdf'  # Replace .json with .pdf
    return json_filename

def check_pdf_extraction_capabilities():
    """Check which PDF extraction libraries are available."""
    capabilities = []
    
    if PYMUPDF_AVAILABLE:
        capabilities.append("PyMuPDF (recommended)")
    
    if PDFPLUMBER_AVAILABLE:
        capabilities.append("pdfplumber (fallback)")
    
    if not capabilities:
        return "No PDF extraction libraries available. Please install PyMuPDF or pdfplumber."
    
    return f"Available: {', '.join(capabilities)}"
