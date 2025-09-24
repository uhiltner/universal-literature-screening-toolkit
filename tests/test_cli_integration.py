"""
CLI integration tests for run_screening.py.
Tests edge cases like empty directories, JSON-only mode, and missing files.
"""

import pytest
import tempfile
import subprocess
import json
import os
import sys
from pathlib import Path


class TestCLIIntegration:
    """Test CLI integration and edge cases."""
    
    def test_empty_input_directory_fails_gracefully(self):
        """Test that empty input directory produces clear error message."""
        with tempfile.TemporaryDirectory() as temp_dir:
            input_dir = Path(temp_dir) / "empty_input"
            output_dir = Path(temp_dir) / "output"
            search_terms = Path(temp_dir) / "search_terms.txt"
            config_file = Path(temp_dir) / "config.json"
            
            # Create empty input directory
            input_dir.mkdir()
            
            # Create minimal search terms
            search_terms.write_text("""
BLOCK 1: Test
test, sample
""", encoding='utf-8')
            
            # Create minimal config
            config_file.write_text('{}', encoding='utf-8')
            
            # Run the CLI tool
            repo_root = Path(__file__).parent.parent
            script_path = repo_root / "run_screening.py"
            
            result = subprocess.run([
                sys.executable, str(script_path),
                "--input", str(input_dir),
                "--output", str(output_dir), 
                "--search-terms", str(search_terms),
                "--config", str(config_file)
            ], capture_output=True, text=True)
            
            # Should exit with non-zero code and clear error message
            assert result.returncode != 0
            assert "No PDF or JSON files found" in result.stdout
    
    def test_json_only_mode_skips_extraction(self):
        """Test that existing JSON files skip PDF extraction."""
        with tempfile.TemporaryDirectory() as temp_dir:
            input_dir = Path(temp_dir) / "json_input"
            output_dir = Path(temp_dir) / "output"
            search_terms = Path(temp_dir) / "search_terms.txt"
            config_file = Path(temp_dir) / "config.json"
            
            input_dir.mkdir()
            
            # Create sample JSON file (no PDFs)
            sample_json = {
                "filename": "sample.pdf",
                "full_text": "This is a sample document about testing methods.",
                "text_length": 50
            }
            (input_dir / "sample.json").write_text(
                json.dumps(sample_json, indent=2), encoding='utf-8'
            )
            
            # Create search terms that will match
            search_terms.write_text("""
BLOCK 1: Methods
testing, methods, sample
""", encoding='utf-8')
            
            config_file.write_text('{"validation_logic": {"default_operator": "AND"}}', encoding='utf-8')
            
            # Run the CLI tool
            repo_root = Path(__file__).parent.parent
            script_path = repo_root / "run_screening.py"
            
            result = subprocess.run([
                sys.executable, str(script_path),
                "--input", str(input_dir),
                "--output", str(output_dir),
                "--search-terms", str(search_terms),
                "--config", str(config_file)
            ], capture_output=True, text=True)
            
            # Should succeed
            assert result.returncode == 0
            assert "Using existing JSON files" in result.stdout or "Loaded" in result.stdout
            
            # Should create output files
            assert (output_dir / "validation_report.html").exists()
            assert (output_dir / "validation_results.json").exists()
    
    def test_missing_search_terms_fails_clearly(self):
        """Test that missing search terms file produces clear error."""
        with tempfile.TemporaryDirectory() as temp_dir:
            input_dir = Path(temp_dir) / "input"
            output_dir = Path(temp_dir) / "output" 
            search_terms = Path(temp_dir) / "nonexistent_search_terms.txt"
            
            input_dir.mkdir()
            # Create a dummy PDF so input validation passes
            (input_dir / "dummy.pdf").write_text("dummy content")
            
            repo_root = Path(__file__).parent.parent
            script_path = repo_root / "run_screening.py"
            
            result = subprocess.run([
                sys.executable, str(script_path),
                "--input", str(input_dir),
                "--output", str(output_dir),
                "--search-terms", str(search_terms)
            ], capture_output=True, text=True)
            
            assert result.returncode != 0
            assert "Search terms file not found" in result.stdout
    
    def test_missing_config_uses_defaults(self):
        """Test that missing config file uses defaults but continues."""
        with tempfile.TemporaryDirectory() as temp_dir:
            input_dir = Path(temp_dir) / "input"
            output_dir = Path(temp_dir) / "output"
            search_terms = Path(temp_dir) / "search_terms.txt"
            missing_config = Path(temp_dir) / "nonexistent_config.json"
            
            input_dir.mkdir()
            
            # Create a sample JSON since we're testing config handling
            sample_json = {
                "filename": "test.pdf",
                "full_text": "Sample text for configuration testing.",
                "text_length": 42
            }
            (input_dir / "test.json").write_text(
                json.dumps(sample_json, indent=2), encoding='utf-8'
            )
            
            search_terms.write_text("""
BLOCK 1: Test
testing, sample
""", encoding='utf-8')
            
            repo_root = Path(__file__).parent.parent
            script_path = repo_root / "run_screening.py"
            
            result = subprocess.run([
                sys.executable, str(script_path),
                "--input", str(input_dir),
                "--output", str(output_dir),
                "--search-terms", str(search_terms),
                "--config", str(missing_config)
            ], capture_output=True, text=True)
            
            # Should succeed with default config
            assert result.returncode == 0
            assert "Using default configuration" in result.stdout or "Config file not found" in result.stdout
    
    def test_successful_run_creates_expected_outputs(self):
        """Test that successful run creates all expected output files."""
        with tempfile.TemporaryDirectory() as temp_dir:
            input_dir = Path(temp_dir) / "input"
            output_dir = Path(temp_dir) / "output"
            search_terms = Path(temp_dir) / "search_terms.txt"
            config_file = Path(temp_dir) / "config.json"
            
            input_dir.mkdir()
            
            # Create sample JSON files
            json1 = {
                "filename": "included.pdf",
                "full_text": "This document discusses forest management and climate change impacts on ecosystems.",
                "text_length": 80
            }
            json2 = {
                "filename": "excluded.pdf", 
                "full_text": "This document is about urban planning and transportation systems.",
                "text_length": 70
            }
            
            (input_dir / "included.json").write_text(json.dumps(json1, indent=2), encoding='utf-8')
            (input_dir / "excluded.json").write_text(json.dumps(json2, indent=2), encoding='utf-8')
            
            # Create search terms that will match only the first document
            search_terms.write_text("""
BLOCK 1: Environment
forest, climate, ecosystem

BLOCK 2: Impact  
impact, change, management
""", encoding='utf-8')
            
            config_file.write_text('{"validation_logic": {"default_operator": "AND"}}', encoding='utf-8')
            
            repo_root = Path(__file__).parent.parent
            script_path = repo_root / "run_screening.py"
            
            result = subprocess.run([
                sys.executable, str(script_path),
                "--input", str(input_dir),
                "--output", str(output_dir),
                "--search-terms", str(search_terms),
                "--config", str(config_file)
            ], capture_output=True, text=True)
            
            # Should succeed
            assert result.returncode == 0
            
            # Check all expected outputs exist
            assert (output_dir / "validation_report.html").exists()
            assert (output_dir / "validation_results.json").exists()
            # Note: summary_statistics.json is not generated by the main CLI
            
            # Verify results content
            with open(output_dir / "validation_results.json", 'r') as f:
                results = json.load(f)
            
            assert len(results) == 2
            # Should have one included and one excluded
            included_count = sum(1 for r in results if r["overall_result"])
            assert included_count == 1