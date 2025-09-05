"""
Test suite for Universal Literature Screening Toolkit
Run with: python -m pytest tests/
"""

import os
import pytest
from pathlib import Path

# A simple placeholder test to verify pytest is working
def test_toolkit_exists():
    """Test that core scripts exist in the toolkit."""
    toolkit_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    scripts_dir = os.path.join(toolkit_dir, 'scripts')
    
    # Check that key script files exist
    assert os.path.exists(os.path.join(scripts_dir, 'pdf_extractor.py'))
    assert os.path.exists(os.path.join(scripts_dir, 'search_parser.py'))
    assert os.path.exists(os.path.join(scripts_dir, 'validator.py'))
    assert os.path.exists(os.path.join(scripts_dir, 'report_generator.py'))

def test_config_exists():
    """Test that config file exists."""
    toolkit_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assert os.path.exists(os.path.join(toolkit_dir, 'config.json'))

def test_documentation_exists():
    """Test that documentation files exist."""
    toolkit_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    assert os.path.exists(os.path.join(toolkit_dir, 'README.md'))
    assert os.path.exists(os.path.join(toolkit_dir, 'LICENSE'))
    assert os.path.exists(os.path.join(toolkit_dir, 'CITATION.cff'))

if __name__ == "__main__":
    # Run tests when script is executed directly
    pytest.main([__file__, "-v"])
