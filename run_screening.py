#!/usr/bin/env python3
"""
Universal Literature Screening Toolkit v1.0.0
===========================================

A configurable tool for systematic literature review and paper screening.
Supports any research domain with customizable search criteria and validation logic.

Usage:
    python run_screening.py --input <pdf_folder> --output <results_folder> --search-terms <search_file> [--config <config_file>]
    python run_screening.py --input <pdf_folder> --output <results_folder> --query-file <query_txt> [--config <config_file>]

Examples:
    # Basic usage
    python run_screening.py --input input_pdfs --output results --search-terms search_terms.txt
    
    # With custom configuration
    python run_screening.py --input papers --output analysis --search-terms criteria.txt --config my_config.json
"""

import argparse
import sys
import json
from pathlib import Path

# Import toolkit modules
sys.path.append(str(Path(__file__).parent / "scripts"))
from search_parser import parse_search_terms
from validator import validate_papers, load_config
from report_generator import generate_html_report, sort_pdf_files

# Optional: new query parser
try:
    from query_parser import parse_query, pretty_print
except Exception:
    parse_query = None  # type: ignore
    pretty_print = None  # type: ignore

def print_banner():
    """Print toolkit banner."""
    print("=" * 60)
    print(" Universal Literature Screening Toolkit v1.0.0")
    print("   Configurable automated PDF screening for any domain")
    print("=" * 60)

def check_prerequisites(args):
    """Check if all required files and directories exist."""
    print("🔍 Checking prerequisites...")
    
    errors = []
    
    # Check input directory
    input_path = Path(args.input)
    if not input_path.exists():
        errors.append(f"❌ Input directory not found: {input_path}")
    else:
        pdf_files = list(input_path.glob("*.pdf"))
        json_files = list(input_path.glob("*.json"))
        
        if pdf_files:
            print(f"✅ Found {len(pdf_files)} PDF files")
        elif json_files:
            print(f"✅ Found {len(json_files)} JSON files (pre-extracted)")
        else:
            errors.append(f"❌ No PDF or JSON files found in {input_path}")
    
    # Check query or search file
    if getattr(args, "query_file", None):
        qf = Path(args.query_file)
        if not qf.exists():
            errors.append(f"❌ Query file not found: {qf}")
        else:
            print(f"✅ Query file: {qf}")
    else:
        search_file = Path(args.search_terms)
        if not search_file.exists():
            errors.append(f"❌ Search terms file not found: {search_file}")
        else:
            print(f"✅ Search terms file: {search_file}")
    
    # Check config file
    config_file = Path(args.config)
    if not config_file.exists():
        print(f"⚠️  Config file not found: {config_file}")
        print("   Using default configuration")
    else:
        print(f"✅ Configuration file: {config_file}")
    
    # Create output directory
    output_path = Path(args.output)
    output_path.mkdir(exist_ok=True)
    print(f"✅ Output directory: {output_path}")
    
    # Check PDF extraction capabilities
    from pdf_extractor import check_pdf_extraction_capabilities
    capabilities = check_pdf_extraction_capabilities()
    print(f"📄 PDF extraction: {capabilities}")
    
    if errors:
        for error in errors:
            print(error)
        return False
    
    return True

def load_and_validate_search_terms(search_file):
    """Load and validate search terms configuration."""
    print(" Loading search criteria...")
    
    try:
        search_blocks = parse_search_terms(search_file)
        print(f" Loaded {len(search_blocks)} search blocks:")
        
        for i, block in enumerate(search_blocks, 1):
            print(f"   Block {i}: {block['name']} ({len(block['terms'])} terms)")
        
        return search_blocks
        
    except Exception as e:
        print(f" Error loading search terms: {e}")
        return None

def load_query_string(query_file: Path) -> str | None:
    """Load a raw Boolean query string from file.

    Supports comment lines starting with '#'. Blank lines are ignored.
    Remaining lines are joined with single spaces.
    """
    try:
        lines = Path(query_file).read_text(encoding="utf-8").splitlines()
        filtered = []
        for line in lines:
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith("#"):
                continue
            filtered.append(stripped)
        text = " ".join(filtered).strip()
        if not text:
            print(" Error: Query file is empty or contains only comments")
            return None
        return text
    except Exception as e:
        print(f" Error reading query file: {e}")
        return None

def display_configuration(config):
    """Display current configuration settings."""
    print("  Configuration settings:")
    
    validation = config.get("validation_logic", {})
    print(f"   Logic: {validation.get('default_operator', 'AND')} (blocks combined with {validation.get('default_operator', 'AND')})")
    
    domain = config.get("domain_info", {})
    print(f"   Domain: {domain.get('research_area', 'Generic Literature Review')}")
    
    text_proc = config.get("text_processing", {})
    print(f"   Case sensitive: {text_proc.get('case_sensitive', False)}")
    print(f"   Encoding: {text_proc.get('encoding', 'utf-8')}")

def run_validation(input_dir, search_blocks, config, *, query_node=None):
    """Run the validation process."""
    print("🔍 Starting validation process...")
    
    try:
        # Step 1: Check if we need to extract PDFs first
        input_path = Path(input_dir)
        pdf_files = list(input_path.glob("*.pdf"))
        json_files = list(input_path.glob("*.json"))
        
        json_source_dir = input_dir
        
        # If we have PDFs but no JSONs, extract first
        if pdf_files and not json_files:
            print("📄 PDF files detected - extracting text...")
            
            # Create extraction directory
            extraction_dir = Path("test_results") / "extracted_json"
            extraction_dir.mkdir(parents=True, exist_ok=True)
            
            # Import here to handle missing libraries gracefully
            from pdf_extractor import extract_pdfs_to_json
            
            extracted_count = extract_pdfs_to_json(input_dir, extraction_dir)
            
            if extracted_count == 0:
                raise Exception("PDF extraction failed - no text could be extracted")
            
            json_source_dir = str(extraction_dir)
            print(f"✅ Extracted text from {extracted_count} PDF files")
        
        elif json_files:
            print(f"📝 Using existing JSON files ({len(json_files)} found)")
        
        # Step 2: Run validation on JSON files
        results = validate_papers(json_source_dir, search_blocks, "config.json", query_node=query_node)
        
        # Statistics
        total_papers = len(results)
        included = sum(1 for r in results if r["overall_result"])
        excluded = total_papers - included
        
        print(f"✅ Validation complete!")
        print(f"   Total papers: {total_papers}")
        print(f"   Included: {included}")
        print(f"   Excluded: {excluded}")
        
        return results
        
    except Exception as e:
        print(f"❌ Validation failed: {e}")
        return None

def generate_outputs(results, output_dir, search_blocks, config, *, query_string: str | None = None):
    """Generate all output files and reports."""
    print(" Generating reports and organizing results...")
    
    output_path = Path(output_dir)
    
    try:
        # Generate HTML report
        if config.get("output_settings", {}).get("html_report", True):
            html_file = output_path / "validation_report.html"
            generate_html_report(results, search_blocks, output_path, query_string=query_string)
            print(f" HTML report: {html_file}")
        
        # Save JSON results
        if config.get("output_settings", {}).get("json_results", True):
            json_file = output_path / "validation_results.json"
            with open(json_file, "w", encoding="utf-8") as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            print(f" JSON results: {json_file}")
        
        # Sort PDFs (if available)
        try:
            sort_pdf_files(results, "input_pdfs", output_path)
            print(" PDFs organized by validation results")
        except Exception as e:
            print(f"  PDF sorting skipped: {e}")
        
        return True
        
    except Exception as e:
        print(f" Output generation failed: {e}")
        return False

def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description="Universal Literature Screening Toolkit v1.0.0",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_screening.py --input input_pdfs --output results --search-terms search_terms.txt
  python run_screening.py --input papers --output analysis --search-terms criteria.txt --config my_config.json
        """
    )
    
    parser.add_argument("--input", required=True,
                       help="Directory containing JSON files from PDF extraction")
    parser.add_argument("--output", required=True,
                       help="Output directory for results and reports")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--search-terms",
                       help="(Deprecated) File containing block-based search terms configuration")
    group.add_argument("--query-file",
                       help="File containing a raw Boolean query string")
    parser.add_argument("--config", default="config.json",
                       help="Configuration file (default: config.json)")
    
    args = parser.parse_args()
    
    # Print banner
    print_banner()
    
    # Load configuration
    config = load_config(args.config)
    display_configuration(config)
    print()
    
    # Check prerequisites
    if not check_prerequisites(args):
        print("\n Prerequisites check failed. Please fix the issues above.")
        sys.exit(1)
    
    print()
    
    # Resolve search criteria (query preferred)
    query_node = None
    search_blocks = None
    query_str_for_report = None
    if getattr(args, "query_file", None):
        if parse_query is None:
            print("❌ Query mode requested but query parser is unavailable")
            sys.exit(1)
        query_str = load_query_string(Path(args.query_file))
        if not query_str:
            sys.exit(1)
        try:
            query_node = parse_query(query_str)
            query_str_for_report = query_str
            if pretty_print:
                print(" Using query:")
                print(pretty_print(query_node))
        except Exception as e:
            print(f"❌ Query parse error: {e}")
            sys.exit(1)
        # Deprecation note
        print("⚠️  validation_logic in config is ignored in query mode.")
    else:
        print("⚠️  --search-terms is deprecated; switch to --query-file in the next release.")
        search_blocks = load_and_validate_search_terms(args.search_terms)
        if not search_blocks:
            sys.exit(1)
    
    print()
    
    # Run validation
    results = run_validation(args.input, search_blocks, config, query_node=query_node)
    if not results:
        sys.exit(1)
    
    print()
    
    # Generate outputs
    if not generate_outputs(results, args.output, search_blocks, config, query_string=query_str_for_report):
        sys.exit(1)
    
    print()
    print(" Literature screening completed successfully!")
    print(f" Results available in: {Path(args.output).absolute()}")

if __name__ == "__main__":
    main()
