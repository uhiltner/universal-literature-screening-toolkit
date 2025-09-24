"""
Tests for report_generator.py module.
Covers folder creation, report filenames, and summary statistics.
"""

import pytest
import tempfile
import json
import os
from pathlib import Path
import sys

# Add scripts to path for testing
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from report_generator import (
    generate_html_report,
    generate_summary_stats,
    sort_pdf_files
)


class TestReportGeneration:
    """Test HTML report generation."""
    
    def test_generate_html_report_creates_file(self):
        """Test that HTML report is created with correct filename."""
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            
            # Sample validation results
            results = [
                {
                    "filename": "paper1.pdf",
                    "overall_result": True,
                    "blocks_passed": 3,
                    "total_blocks": 3,
                    "block_results": [
                        {"block_name": "Block1", "passed": True}
                    ]
                },
                {
                    "filename": "paper2.pdf",
                    "overall_result": False,
                    "blocks_passed": 1,
                    "total_blocks": 3,
                    "block_results": [
                        {"block_name": "Block1", "passed": False}
                    ]
                }
            ]
            
            # Sample search blocks
            search_blocks = [
                {"name": "Test Block", "terms": ["test"]}
            ]
            
            generate_html_report(results, search_blocks, str(output_dir))
            
            # Check that validation_report.html is created
            html_file = output_dir / "validation_report.html"
            assert html_file.exists()
            
            # Check content contains expected elements
            content = html_file.read_text(encoding='utf-8')
            assert "Literature Screening Results" in content
            assert "paper1.pdf" in content
            assert "paper2.pdf" in content
            # Check the actual format used by the generator
            assert "Total Papers Analyzed:</strong> 2" in content


class TestSummaryStatistics:
    """Test summary statistics generation."""
    
    def test_generate_summary_stats_creates_file(self):
        """Test that summary statistics file is created with expected fields."""
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            
            results = [
                {"overall_result": True, "block_results": []},
                {"overall_result": False, "block_results": []},
                {"overall_result": True, "block_results": []}
            ]
            
            generate_summary_stats(results, str(output_dir))
            
            stats_file = output_dir / "summary_statistics.json"
            assert stats_file.exists()
            
            with open(stats_file, 'r', encoding='utf-8') as f:
                stats = json.load(f)
            
            assert stats["total_papers"] == 3
            assert stats["included_papers"] == 2
            assert stats["excluded_papers"] == 1
            assert stats["inclusion_rate"] == 66.7
            assert "screening_date" in stats


class TestPDFSorting:
    """Test PDF file sorting functionality."""
    
    def test_sort_pdf_files_creates_directories(self):
        """Test that include/exclude directories are created."""
        with tempfile.TemporaryDirectory() as temp_dir:
            input_dir = Path(temp_dir) / "input"
            output_dir = Path(temp_dir) / "output"
            input_dir.mkdir()
            
            # Create sample PDF files
            pdf1 = input_dir / "included.pdf"
            pdf2 = input_dir / "excluded.pdf"
            pdf1.write_text("fake pdf content 1")
            pdf2.write_text("fake pdf content 2")
            
            results = [
                {"filename": "included.pdf", "overall_result": True},
                {"filename": "excluded.pdf", "overall_result": False}
            ]
            
            sort_pdf_files(results, str(input_dir), str(output_dir))
            
            # Check directories were created
            include_dir = output_dir / "sorted_pdfs" / "include"
            exclude_dir = output_dir / "sorted_pdfs" / "exclude"
            assert include_dir.exists()
            assert exclude_dir.exists()
            
            # Check files were copied
            assert (include_dir / "included.pdf").exists()
            assert (exclude_dir / "excluded.pdf").exists()
    
    def test_sort_pdf_files_handles_missing_files(self):
        """Test that missing PDF files are handled gracefully."""
        with tempfile.TemporaryDirectory() as temp_dir:
            input_dir = Path(temp_dir) / "input"
            output_dir = Path(temp_dir) / "output"
            input_dir.mkdir()
            
            # Results reference files that don't exist
            results = [
                {"filename": "missing1.pdf", "overall_result": True},
                {"filename": "missing2.pdf", "overall_result": False}
            ]
            
            # Should not crash, just handle missing files gracefully
            sort_pdf_files(results, str(input_dir), str(output_dir))
            
            # Directories should still be created
            include_dir = output_dir / "sorted_pdfs" / "include"
            exclude_dir = output_dir / "sorted_pdfs" / "exclude"
            assert include_dir.exists()
            assert exclude_dir.exists()


class TestReportIntegration:
    """Test integration between report components."""
    
    def test_full_report_workflow(self):
        """Test complete report generation workflow."""
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir)
            
            results = [
                {
                    "filename": "test.pdf",
                    "overall_result": True,
                    "blocks_passed": 2,
                    "total_blocks": 2,
                    "block_results": [
                        {"block_name": "Block1", "passed": True},
                        {"block_name": "Block2", "passed": True}
                    ]
                }
            ]
            
            search_blocks = [
                {"name": "Block1", "terms": ["term1"]},
                {"name": "Block2", "terms": ["term2"]}
            ]
            
            # Generate all reports
            generate_html_report(results, search_blocks, str(output_dir))
            generate_summary_stats(results, str(output_dir))
            
            # Verify all files created
            assert (output_dir / "validation_report.html").exists()
            assert (output_dir / "summary_statistics.json").exists()
            
            # Verify content consistency
            with open(output_dir / "summary_statistics.json", 'r') as f:
                stats = json.load(f)
            assert stats["total_papers"] == 1
            assert stats["included_papers"] == 1