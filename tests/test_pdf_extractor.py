"""
Tests for pdf_extractor.py module.
Covers capability reporting, empty directories, and corrupt files.
"""

import pytest
import tempfile
import shutil
import os
from pathlib import Path
import sys
from unittest.mock import patch

# Add scripts to path for testing
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from pdf_extractor import (
    extract_pdfs_to_json, 
    check_pdf_extraction_capabilities,
    load_json_content,
    get_paper_filename
)


class TestCapabilityReporting:
    """Test PDF extraction capability reporting."""
    
    def test_capability_reporting_with_libraries(self):
        """Test capability string when libraries are available."""
        capabilities = check_pdf_extraction_capabilities()
        # Should contain at least one of the libraries
        assert "PyMuPDF" in capabilities or "pdfplumber" in capabilities
    
    @patch('pdf_extractor.PYMUPDF_AVAILABLE', False)
    @patch('pdf_extractor.PDFPLUMBER_AVAILABLE', False)
    def test_capability_reporting_no_libraries(self):
        """Test capability string when no libraries are available."""
        capabilities = check_pdf_extraction_capabilities()
        assert "No PDF extraction libraries available" in capabilities


class TestPDFExtraction:
    """Test PDF extraction functionality."""
    
    def test_extract_no_pdfs_returns_zero(self):
        """Test that empty PDF directory returns 0 and prints warning."""
        with tempfile.TemporaryDirectory() as temp_dir:
            input_dir = Path(temp_dir) / "input"
            output_dir = Path(temp_dir) / "output" 
            input_dir.mkdir()
            output_dir.mkdir()
            
            # No PDF files in input directory
            result = extract_pdfs_to_json(str(input_dir), str(output_dir))
            assert result == 0
    
    def test_extract_corrupt_pdf_handled_gracefully(self):
        """Test that corrupt PDF files are handled without crashing."""
        with tempfile.TemporaryDirectory() as temp_dir:
            input_dir = Path(temp_dir) / "input"
            output_dir = Path(temp_dir) / "output"
            input_dir.mkdir()
            output_dir.mkdir()
            
            # Create a fake "PDF" that's actually just text
            fake_pdf = input_dir / "corrupt.pdf"
            fake_pdf.write_text("This is not a real PDF file content", encoding='utf-8')
            
            # Should handle gracefully without crashing
            result = extract_pdfs_to_json(str(input_dir), str(output_dir))
            
            # Result should be 0 since extraction failed
            assert result == 0
            
            # No JSON should be created for the corrupt file
            json_files = list(output_dir.glob("*.json"))
            assert len(json_files) == 0


class TestJSONHandling:
    """Test JSON loading and filename conversion."""
    
    def test_load_json_content(self):
        """Test loading JSON files from directory."""
        with tempfile.TemporaryDirectory() as temp_dir:
            json_dir = Path(temp_dir)
            
            # Create sample JSON files
            json1 = {
                "filename": "paper1.pdf",
                "full_text": "Sample text content for paper 1",
                "text_length": 30
            }
            json2 = {
                "filename": "paper2.pdf", 
                "full_text": "Sample text content for paper 2",
                "text_length": 30
            }
            
            (json_dir / "paper1.json").write_text(
                json.dumps(json1, indent=2), encoding='utf-8'
            )
            (json_dir / "paper2.json").write_text(
                json.dumps(json2, indent=2), encoding='utf-8'
            )
            
            papers = load_json_content(str(json_dir))
            assert len(papers) == 2
            assert all("full_text" in paper for paper in papers)
    
    def test_get_paper_filename_conversion(self):
        """Test conversion from JSON filename to PDF filename."""
        assert get_paper_filename("paper1.json") == "paper1.pdf"
        assert get_paper_filename("paper.pdf") == "paper.pdf"  # Already PDF
        assert get_paper_filename("no_extension") == "no_extension"
    
    def test_load_json_handles_corrupt_files(self):
        """Test that corrupt JSON files are handled gracefully."""
        with tempfile.TemporaryDirectory() as temp_dir:
            json_dir = Path(temp_dir)
            
            # Create a valid JSON
            valid_json = {"filename": "valid.pdf", "full_text": "Valid content"}
            (json_dir / "valid.json").write_text(
                json.dumps(valid_json), encoding='utf-8'
            )
            
            # Create corrupt JSON
            (json_dir / "corrupt.json").write_text(
                "{ invalid json content", encoding='utf-8'
            )
            
            papers = load_json_content(str(json_dir))
            # Should load only the valid JSON
            assert len(papers) == 1
            assert papers[0]["filename"] == "valid.pdf"


# Need to import json for the tests
import json