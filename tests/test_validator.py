"""
Tests for validator.py module.
Covers AND/OR logic, block combinations, and edge cases.
"""

import pytest
import tempfile
import json
import os
from pathlib import Path
import sys

# Add scripts to path for testing
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from validator import validate_papers, validate_single_paper, load_config, create_validation_result
from search_parser import compile_regex_patterns


class TestConfigLoading:
    """Test configuration loading and defaults."""
    
    def test_load_missing_config_uses_defaults(self):
        """Test that missing config file uses defaults."""
        config = load_config("nonexistent_config.json")
        assert config["validation_logic"]["default_operator"] == "AND"
        assert config["text_processing"]["case_sensitive"] == False
        assert config["text_processing"]["encoding"] == "utf-8"
    
    def test_load_valid_config(self):
        """Test loading a valid config file."""
        config_data = {
            "validation_logic": {"default_operator": "OR"},
            "text_processing": {"case_sensitive": True}
        }
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False, encoding='utf-8') as f:
            json.dump(config_data, f)
            f.flush()
            
            config = load_config(f.name)
            assert config["validation_logic"]["default_operator"] == "OR"
            assert config["text_processing"]["case_sensitive"] == True
            
        os.unlink(f.name)


class TestValidationLogic:
    """Test validation logic for AND/OR operations."""
    
    def test_and_logic_all_blocks_must_pass(self):
        """Test AND logic requires all blocks to pass."""
        # Create compiled blocks
        blocks = [
            {"name": "Block1", "regex": compile_regex_pattern(["forest"]), "pattern": "", "term_count": 1},
            {"name": "Block2", "regex": compile_regex_pattern(["ocean"]), "pattern": "", "term_count": 1}  # Use a word not in text
        ]

        # Paper with only one matching block
        paper = {
            "filename": "test.json",
            "full_text": "This paper discusses forest management but not marine environments."
        }

        config = {"validation_logic": {"default_operator": "AND"}}
        result = validate_single_paper(paper, blocks, config)
        
        assert result["overall_result"] == False  # AND requires all blocks
        assert result["blocks_passed"] == 1
        assert result["total_blocks"] == 2
    
    def test_or_logic_any_block_passes(self):
        """Test OR logic requires only one block to pass."""
        blocks = [
            {"name": "Block1", "regex": compile_regex_pattern(["forest"]), "pattern": "", "term_count": 1},
            {"name": "Block2", "regex": compile_regex_pattern(["ocean"]), "pattern": "", "term_count": 1}  # Use a word not in text
        ]

        paper = {
            "filename": "test.json",
            "full_text": "This paper discusses forest management but not marine environments."
        }

        config = {"validation_logic": {"default_operator": "OR"}}
        result = validate_single_paper(paper, blocks, config)
        
        assert result["overall_result"] == True  # OR requires any block
        assert result["blocks_passed"] == 1

    def test_empty_text_returns_false_with_error(self):
        """Test that empty text returns False with error."""
        blocks = [
            {"name": "Block1", "regex": compile_regex_pattern(["forest"]), "pattern": "", "term_count": 1}
        ]
        
        paper = {"filename": "empty.json", "full_text": ""}
        config = {"validation_logic": {"default_operator": "AND"}}
        
        result = validate_single_paper(paper, blocks, config)
        assert result["overall_result"] == False
        assert result["error"] == "No text content"


class TestBlockCombinations:
    """Test block combination functionality."""
    
    def test_block_combinations_and(self):
        """Test combining blocks with AND logic."""
        blocks = [
            {"name": "Regular Block", "regex": compile_regex_pattern(["forest"]), "pattern": "", "term_count": 1},
            {"name": "3A Special", "regex": compile_regex_pattern(["climate"]), "pattern": "", "term_count": 1},
            {"name": "3B Special", "regex": compile_regex_pattern(["change"]), "pattern": "", "term_count": 1}
        ]
        
        paper = {
            "filename": "test.json",
            "full_text": "Forest research on climate change impacts."
        }
        
        config = {
            "validation_logic": {
                "default_operator": "AND",
                "block_combinations": {
                    "blocks": ["3A", "3B"], 
                    "operator": "AND",
                    "combined_name": "Combined Environmental"
                }
            }
        }
        
        result = validate_single_paper(paper, blocks, config)
        
        # Should have regular block + combined block
        assert len(result["block_results"]) == 2
        combined_block = next(b for b in result["block_results"] if b["block_name"] == "Combined Environmental")
        assert combined_block["passed"] == True  # Both 3A and 3B should match
    
    def test_block_combinations_or(self):
        """Test combining blocks with OR logic."""
        blocks = [
            {"name": "3A Special", "regex": compile_regex_pattern(["climate"]), "pattern": "", "term_count": 1},
            {"name": "3B Special", "regex": compile_regex_pattern(["weather"]), "pattern": "", "term_count": 1}
        ]
        
        paper = {
            "filename": "test.json",
            "full_text": "This discusses climate but not weather."
        }
        
        config = {
            "validation_logic": {
                "default_operator": "AND",
                "block_combinations": {
                    "blocks": ["3A", "3B"],
                    "operator": "OR", 
                    "combined_name": "Either Climate"
                }
            }
        }
        
        result = validate_single_paper(paper, blocks, config)
        combined_block = result["block_results"][0]
        assert combined_block["block_name"] == "Either Climate"
        assert combined_block["passed"] == True  # OR requires only one match


def compile_regex_pattern(terms):
    """Helper to compile regex from terms."""
    import re
    from search_parser import create_regex_pattern
    pattern = create_regex_pattern(terms)
    return re.compile(pattern, re.IGNORECASE)