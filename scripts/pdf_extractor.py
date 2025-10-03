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
    """
    Extract text using PyMuPDF (primary method).
    
    Returns:
        tuple: (text, error_code) where error_code is None on success or one of:
               'PDF_ENCRYPTED', 'PDF_CORRUPTED', 'FILE_NOT_FOUND', 'UNKNOWN_ERROR'
    """
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text.strip(), None
    except fitz.FileDataError as e:
        # Corrupted or invalid PDF structure
        print(f"PyMuPDF extraction failed for {pdf_path}: Corrupted PDF file")
        return None, 'PDF_CORRUPTED'
    except fitz.FileNotFoundError as e:
        print(f"PyMuPDF extraction failed for {pdf_path}: File not found")
        return None, 'FILE_NOT_FOUND'
    except RuntimeError as e:
        # Check for encryption/password protection
        error_str = str(e).lower()
        if 'password' in error_str or 'encrypted' in error_str or 'crypt' in error_str:
            print(f"PyMuPDF extraction failed for {pdf_path}: PDF is encrypted or password-protected")
            return None, 'PDF_ENCRYPTED'
        print(f"PyMuPDF extraction failed for {pdf_path}: {e}")
        return None, 'UNKNOWN_ERROR'
    except Exception as e:
        # Catch-all for other errors
        error_str = str(e).lower()
        if 'password' in error_str or 'encrypted' in error_str or 'crypt' in error_str:
            print(f"PyMuPDF extraction failed for {pdf_path}: PDF is encrypted or password-protected")
            return None, 'PDF_ENCRYPTED'
        print(f"PyMuPDF extraction failed for {pdf_path}: {e}")
        return None, 'UNKNOWN_ERROR'

def extract_text_with_pdfplumber(pdf_path):
    """
    Extract text using pdfplumber (fallback method).
    
    Returns:
        tuple: (text, error_code) where error_code is None on success or one of:
               'PDF_ENCRYPTED', 'PDF_CORRUPTED', 'FILE_NOT_FOUND', 'UNKNOWN_ERROR'
    """
    try:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text.strip(), None
    except FileNotFoundError as e:
        print(f"pdfplumber extraction failed for {pdf_path}: File not found")
        return None, 'FILE_NOT_FOUND'
    except Exception as e:
        error_str = str(e).lower()
        if 'password' in error_str or 'encrypted' in error_str or 'crypt' in error_str:
            print(f"pdfplumber extraction failed for {pdf_path}: PDF is encrypted or password-protected")
            return None, 'PDF_ENCRYPTED'
        elif 'corrupt' in error_str or 'invalid' in error_str or 'damaged' in error_str:
            print(f"pdfplumber extraction failed for {pdf_path}: Corrupted PDF file")
            return None, 'PDF_CORRUPTED'
        print(f"pdfplumber extraction failed for {pdf_path}: {e}")
        return None, 'UNKNOWN_ERROR'

def extract_text_from_pdf(pdf_path):
    """
    Extract text from PDF using available methods with fallback strategy.
    
    Returns:
        tuple: (text, error_code) where error_code is one of:
               None (success), 'PDF_ENCRYPTED', 'PDF_CORRUPTED', 'NO_TEXT_CONTENT',
               'LIBRARY_MISSING', 'FILE_NOT_FOUND', 'UNKNOWN_ERROR'
    """
    # Check if any extraction library is available
    if not PYMUPDF_AVAILABLE and not PDFPLUMBER_AVAILABLE:
        return None, 'LIBRARY_MISSING'
    
    # Try PyMuPDF first (fastest and most reliable)
    if PYMUPDF_AVAILABLE:
        text, error_code = extract_text_with_pymupdf(pdf_path)
        if text and len(text) > 50:  # Reasonable text extracted
            return text, None
        elif error_code in ['PDF_ENCRYPTED', 'PDF_CORRUPTED', 'FILE_NOT_FOUND']:
            # These errors are definitive, no point trying fallback
            return None, error_code
        # Otherwise, try fallback (might be scanned PDF or OCR needed)
    
    # Fallback to pdfplumber
    if PDFPLUMBER_AVAILABLE:
        text, error_code = extract_text_with_pdfplumber(pdf_path)
        if text and len(text) > 50:
            return text, None
        elif error_code:
            return None, error_code
    
    # Both methods failed to extract sufficient text
    # This usually means scanned PDF without OCR or truly empty PDF
    return None, 'NO_TEXT_CONTENT'

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
        tuple: (successful_count, failed_list) where failed_list contains
               dicts with keys 'filename', 'error_code', 'error_message'
    """
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    pdf_files = list(Path(input_dir).glob("*.pdf"))
    
    if not pdf_files:
        print(f"No PDF files found in {input_dir}")
        return 0, []
    
    print(f"Found {len(pdf_files)} PDF files to process...")
    
    processed_count = 0
    failed_files = []
    
    # Error code descriptions for user-friendly messages
    ERROR_MESSAGES = {
        'PDF_ENCRYPTED': 'PDF is password-protected or encrypted',
        'PDF_CORRUPTED': 'PDF file is corrupted or has invalid structure',
        'NO_TEXT_CONTENT': 'PDF contains no extractable text (likely scanned image)',
        'LIBRARY_MISSING': 'No PDF extraction libraries available (install PyMuPDF or pdfplumber)',
        'FILE_NOT_FOUND': 'PDF file not found or inaccessible',
        'UNKNOWN_ERROR': 'Unknown error during PDF extraction'
    }
    
    for pdf_path in pdf_files:
        try:
            print(f"Processing: {pdf_path.name}")
            
            # Extract text with error categorization
            full_text, error_code = extract_text_from_pdf(pdf_path)
            
            if error_code:
                # Extraction failed with specific error
                error_msg = ERROR_MESSAGES.get(error_code, 'Unknown error')
                print(f"  ❌ Failed: {error_msg}")
                failed_files.append({
                    'filename': pdf_path.name,
                    'error_code': error_code,
                    'error_message': error_msg
                })
                continue
            
            if not full_text or len(full_text) < 100:
                print(f"  ⚠️  Warning: Minimal text extracted from {pdf_path.name}")
                failed_files.append({
                    'filename': pdf_path.name,
                    'error_code': 'NO_TEXT_CONTENT',
                    'error_message': ERROR_MESSAGES['NO_TEXT_CONTENT']
                })
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
            print(f"  ❌ Unexpected error processing {pdf_path.name}: {e}")
            failed_files.append({
                'filename': pdf_path.name,
                'error_code': 'UNKNOWN_ERROR',
                'error_message': str(e)
            })
    
    print(f"\n📊 Extraction Summary:")
    print(f"  Successful: {processed_count}/{len(pdf_files)} files")
    if failed_files:
        print(f"  Failed: {len(failed_files)} files")
        # Group by error type
        error_counts = {}
        for failure in failed_files:
            error_code = failure['error_code']
            error_counts[error_code] = error_counts.get(error_code, 0) + 1
        
        print(f"  Error breakdown:")
        for error_code, count in sorted(error_counts.items()):
            print(f"    - {ERROR_MESSAGES.get(error_code, error_code)}: {count} file(s)")
    
    return processed_count, failed_files

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
