"""
Tests for search_parser.py module.
Covers block parsing, quoted phrases, wildcards, and edge cases.
"""

import pytest
import tempfile
import os
from pathlib import Path
import sys

# Add scripts to path for testing
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))
from search_parser import parse_search_terms, create_regex_pattern, compile_regex_patterns


class TestSearchTermsParsing:
    """Test search terms file parsing."""
    
    def test_parse_basic_blocks(self):
        """Test parsing of basic block structure."""
        content = """
BLOCK 1: Primary Research
climate, environment, ecosystem

BLOCK 2: Secondary Context  
impact, effect, consequence
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
            f.write(content)
            f.flush()
            
            blocks = parse_search_terms(f.name)
            assert len(blocks) == 2
            assert blocks[0]["name"] == "Primary Research"
            assert blocks[0]["terms"] == ["climate", "environment", "ecosystem"]
            assert blocks[1]["name"] == "Secondary Context"
            assert blocks[1]["terms"] == ["impact", "effect", "consequence"]
            
        os.unlink(f.name)
    
    def test_parse_quoted_phrases(self):
        """Test parsing of exact phrases in quotes."""
        content = """
BLOCK 1: Exact Phrases
"climate change", "global warming", normal_term
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
            f.write(content)
            f.flush()
            
            blocks = parse_search_terms(f.name)
            assert len(blocks) == 1
            assert blocks[0]["terms"] == ['"climate change"', '"global warming"', 'normal_term']
            
        os.unlink(f.name)
    
    def test_parse_wildcards(self):
        """Test parsing of wildcard terms."""
        content = """
BLOCK 1: Wildcards
forest*, climat*, exact_word
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
            f.write(content)
            f.flush()
            
            blocks = parse_search_terms(f.name)
            assert len(blocks) == 1
            assert blocks[0]["terms"] == ["forest*", "climat*", "exact_word"]
            
        os.unlink(f.name)
    
    def test_parse_empty_file_raises_error(self):
        """Test that empty file raises ValueError."""
        content = """
# Just comments
# No actual blocks
"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.txt', delete=False, encoding='utf-8') as f:
            f.write(content)
            f.flush()
            
            with pytest.raises(ValueError, match="No valid search blocks found"):
                parse_search_terms(f.name)
                
        os.unlink(f.name)
    
    def test_parse_missing_file_raises_error(self):
        """Test that missing file raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
            parse_search_terms("nonexistent_file.txt")


class TestRegexPatternCreation:
    """Test regex pattern generation."""
    
    def test_exact_phrase_pattern(self):
        """Test quoted phrase becomes word-bounded regex."""
        terms = ['"climate change"']
        pattern = create_regex_pattern(terms)
        # re.escape() converts spaces to escaped spaces
        assert r'\bclimate\ change\b' in pattern
    
    def test_wildcard_pattern(self):
        """Test wildcard becomes stem + word characters."""
        terms = ['forest*']
        pattern = create_regex_pattern(terms)
        assert r'\bforest\w*' in pattern
    
    def test_normal_word_pattern(self):
        """Test normal word becomes word-bounded."""
        terms = ['ecosystem']
        pattern = create_regex_pattern(terms)
        assert r'\becosystem\b' in pattern
    
    def test_mixed_terms_pattern(self):
        """Test combination of different term types."""
        terms = ['"exact phrase"', 'wildcard*', 'normal']
        pattern = create_regex_pattern(terms)
        # re.escape() converts spaces to escaped spaces
        assert r'\bexact\ phrase\b' in pattern
        assert r'\bwildcard\w*' in pattern
        assert r'\bnormal\b' in pattern


class TestRegexCompilation:
    """Test compiled regex patterns."""
    
    def test_compile_patterns(self):
        """Test compilation of search blocks to regex."""
        blocks = [
            {"name": "Test Block", "terms": ["forest*", '"climate change"', "ecosystem"]}
        ]
        compiled = compile_regex_patterns(blocks)
        
        assert len(compiled) == 1
        assert compiled[0]["name"] == "Test Block"
        assert compiled[0]["term_count"] == 3
        assert compiled[0]["regex"] is not None
        
        # Test the compiled regex works
        test_text = "The forest ecosystem responds to climate change rapidly"
        matches = compiled[0]["regex"].findall(test_text.lower())
        assert len(matches) >= 2  # Should match 'forest' and 'climate change'