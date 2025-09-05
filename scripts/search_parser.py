"""
Search Terms Parser Module

Parses user-defined search criteria from search_terms.txt file.
Converts search terms into regex patterns for validation.
"""

import re
from pathlib import Path

def parse_search_terms(file_path):
    """Parse search terms from configuration file."""
    blocks = []
    current_block = None
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                
                # Skip comments and empty lines
                if not line or line.startswith("#"):
                    continue
                
                # Check for block header
                if line.startswith("BLOCK") and ":" in line:
                    if current_block:
                        blocks.append(current_block)
                    
                    block_name = line.split(":", 1)[1].strip()
                    current_block = {
                        "name": block_name,
                        "terms": [],
                        "line_number": line_num
                    }
                elif current_block is not None:
                    # Parse terms from line
                    terms = parse_terms_line(line)
                    current_block["terms"].extend(terms)
            
            # Add final block
            if current_block:
                blocks.append(current_block)
                
    except FileNotFoundError:
        raise FileNotFoundError(f"Search terms file not found: {file_path}")
    except Exception as e:
        raise Exception(f"Error parsing search terms: {e}")
    
    if not blocks:
        raise ValueError("No valid search blocks found in search terms file")
    
    return blocks

def parse_terms_line(line):
    """Parse individual terms from a line."""
    terms = []
    
    # Split by commas but preserve quoted phrases
    parts = re.split(r",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", line)
    
    for part in parts:
        term = part.strip()
        if term:
            terms.append(term)
    
    return terms

def create_regex_pattern(terms):
    """
    Converts a list of search terms into a single, case-insensitive regex pattern.
    - 'word*' becomes r'\bword\w*'
    - '"exact phrase"' becomes r'\bexact phrase\b'
    """
    processed_terms = []
    for term in terms:
        if term.startswith('"') and term.endswith('"'):
            # Exact phrase
            phrase = term.strip('"')
            processed_terms.append(r'\b' + re.escape(phrase) + r'\b')
        elif term.endswith('*'):
            # Wildcard term
            stem = term.rstrip('*')
            processed_terms.append(r'\b' + re.escape(stem) + r'\w*')
        else:
            # A term that should be matched as a whole word
            processed_terms.append(r'\b' + re.escape(term) + r'\b')
            
    return '|'.join(processed_terms)

def compile_regex_patterns(blocks):
    """Compile regex patterns from search blocks."""
    compiled_blocks = []
    
    for block in blocks:
        # Create regex pattern for this block
        pattern = create_regex_pattern(block["terms"])
        compiled_regex = re.compile(pattern, re.IGNORECASE)
        
        compiled_blocks.append({
            "name": block["name"],
            "regex": compiled_regex,
            "pattern": pattern,
            "term_count": len(block["terms"])
        })
    
    return compiled_blocks
