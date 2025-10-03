"""
Report Generator Module

Generates reports and sorts PDF files based on validation results.
"""

import json
import shutil
import os
from pathlib import Path
from datetime import datetime

def generate_reports(validation_results, search_blocks, input_pdf_dir, output_dir, query_string: str | None = None, failed_pdfs: list | None = None):
    """Generate all reports and sort files.
    
    Args:
        validation_results: List of validation results for successfully processed PDFs
        search_blocks: Search blocks used for validation (legacy)
        input_pdf_dir: Directory containing input PDFs
        output_dir: Directory for output files
        query_string: Query string used for validation (if available)
        failed_pdfs: List of dicts with 'filename', 'error_code', 'error_message' for failed extractions
    """
    
    # Create output directories
    os.makedirs(f"{output_dir}/sorted_pdfs/include", exist_ok=True)
    os.makedirs(f"{output_dir}/sorted_pdfs/exclude", exist_ok=True)
    
    # Save validation results
    results_path = f"{output_dir}/validation_results.json"
    with open(results_path, "w", encoding="utf-8") as f:
        json.dump(validation_results, f, ensure_ascii=False, indent=2)
    
    # Sort PDF files
    sort_pdf_files(validation_results, input_pdf_dir, output_dir)
    
    # Generate HTML report
    generate_html_report(validation_results, search_blocks, output_dir, query_string=query_string, failed_pdfs=failed_pdfs)
    
    # Generate summary statistics
    generate_summary_stats(validation_results, output_dir, failed_pdfs=failed_pdfs)

def sort_pdf_files(validation_results, input_dir, output_dir):
    """Sort PDF files into include/exclude folders."""
    
    # Ensure destination folders exist
    include_dir = Path(output_dir) / "sorted_pdfs" / "include"
    exclude_dir = Path(output_dir) / "sorted_pdfs" / "exclude"
    include_dir.mkdir(parents=True, exist_ok=True)
    exclude_dir.mkdir(parents=True, exist_ok=True)

    included_count = 0
    excluded_count = 0
    missing_count = 0
    
    for result in validation_results:
        filename = result["filename"]
        source_path = Path(input_dir) / filename
        
        if not source_path.exists():
            print(f"Warning: PDF file not found: {filename}")
            missing_count += 1
            continue
        
        if result["overall_result"]:
            dest_path = include_dir / filename
            included_count += 1
        else:
            dest_path = exclude_dir / filename
            excluded_count += 1
        
        try:
            shutil.copy2(source_path, dest_path)
        except Exception as e:
            print(f"Error copying {filename}: {e}")
    
    print(f"Files sorted: {included_count} included, {excluded_count} excluded")
    if missing_count > 0:
        print(f"Warning: {missing_count} PDF files were missing")

def generate_html_report(validation_results, search_blocks, output_dir, query_string: str | None = None, failed_pdfs: list | None = None):
    """Generate HTML report with detailed results.

    When query_string is provided, it will be displayed instead of legacy block list.
    Failed PDFs section is included if failed_pdfs is provided.
    """
    
    total_papers = len(validation_results)
    included_papers = sum(1 for r in validation_results if r["overall_result"])
    excluded_papers = total_papers - included_papers
    failed_count = len(failed_pdfs) if failed_pdfs else 0
    
    # Error code recommendations
    ERROR_RECOMMENDATIONS = {
        'PDF_ENCRYPTED': 'Remove password protection or use a PDF decryption tool before screening.',
        'PDF_CORRUPTED': 'Try opening the PDF in Adobe Reader and re-saving it, or obtain a fresh copy.',
        'NO_TEXT_CONTENT': 'This PDF contains no extractable text (likely a scanned image). Use OCR software to convert to searchable PDF.',
        'LIBRARY_MISSING': 'Install PDF extraction libraries: pip install PyMuPDF pdfplumber',
        'FILE_NOT_FOUND': 'Verify that the PDF file exists in the input_pdfs directory.',
        'UNKNOWN_ERROR': 'Contact support or inspect the PDF manually for unusual characteristics.'
    }
    
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Literature Screening Results</title>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
        .header {{ background: #f0f8ff; padding: 20px; border-radius: 10px; margin-bottom: 20px; }}
        .summary {{ background: #f9f9f9; padding: 15px; margin: 20px 0; border-radius: 5px; }}
        .warning {{ background: #fff3cd; padding: 15px; margin: 20px 0; border-radius: 5px; border-left: 4px solid #ff9800; }}
        .block {{ margin: 10px 0; padding: 10px; border-left: 4px solid #007acc; background: #fafafa; }}
        .included {{ color: green; font-weight: bold; }}
        .excluded {{ color: red; font-weight: bold; }}
        .failed {{ color: #d32f2f; font-weight: bold; }}
        table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; font-weight: bold; }}
        .criteria-list {{ list-style-type: none; padding: 0; }}
        .criteria-list li {{ padding: 2px 0; }}
        .pass {{ color: green; }}
        .fail {{ color: red; }}
        .error-cell {{ font-family: monospace; font-size: 0.9em; }}
        .recommendation {{ font-size: 0.9em; color: #555; font-style: italic; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🌲 Literature Screening Results</h1>
        <p><strong>Generated:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        <p><strong>Toolkit Version:</strong> 1.0.0</p>
    </div>
    
    <div class="summary">
        <h2>📊 Summary Statistics</h2>
        <p><strong>Total PDFs Submitted:</strong> {total_papers + failed_count}</p>
        <p><strong>Successfully Processed:</strong> {total_papers}</p>"""
    
    if failed_count > 0:
        html_content += f"""
        <p><strong>Failed to Process:</strong> <span class="failed">{failed_count} PDF(s)</span></p>"""
    
    html_content += f"""
        <hr style="margin: 15px 0;">
        <p><strong>Papers Included:</strong> <span class="included">{included_papers} ({included_papers/total_papers*100:.1f}%)</span></p>
        <p><strong>Papers Excluded:</strong> <span class="excluded">{excluded_papers} ({excluded_papers/total_papers*100:.1f}%)</span></p>
    </div>
    """
    
    # Failed PDFs section
    if failed_pdfs and len(failed_pdfs) > 0:
        html_content += f"""
    <div class="warning">
        <h2>⚠️ PDF Processing Issues</h2>
        <p>The following {len(failed_pdfs)} PDF(s) could not be processed. These files were <strong>not included</strong> in the screening results above.</p>
        
        <table>
            <thead>
                <tr>
                    <th>Filename</th>
                    <th>Issue Type</th>
                    <th>Recommended Action</th>
                </tr>
            </thead>
            <tbody>"""
        
        for failed in failed_pdfs:
            error_code = failed.get('error_code', 'UNKNOWN_ERROR')
            recommendation = ERROR_RECOMMENDATIONS.get(error_code, 'Contact support')
            html_content += f"""
                <tr>
                    <td>{failed['filename']}</td>
                    <td class="error-cell">{failed.get('error_message', 'Unknown error')}</td>
                    <td class="recommendation">{recommendation}</td>
                </tr>"""
        
        html_content += """
            </tbody>
        </table>
        
        <p style="margin-top: 15px;"><strong>Note:</strong> If most PDFs failed with the same error, check the troubleshooting section in the User Guide.</p>
    </div>
    """
    
    html_content += """
    <div class="block">
        <h2>🔍 Search Criteria Applied</h2>
        """
    if query_string:
        html_content += f"<p><strong>Query:</strong> {query_string}</p>"
    else:
        html_content += "<p><strong>Validation Logic:</strong> Boolean AND (all blocks must pass)</p>\n        <ul class=\"criteria-list\">"
        for i, block in enumerate(search_blocks or [], 1):
            html_content += f"<li><strong>Block {i}:</strong> {block['name']} ({len(block['terms'])} terms)</li>"
        html_content += "        </ul>"
    
    html_content += """
    </div>
    
    <h2>📋 Detailed Results by Paper</h2>
    <table>
        <thead>
            <tr>
                <th>Filename</th>
                <th>Overall Result</th>
                <th>Blocks Passed</th>
                <th>Block Details</th>
            </tr>
        </thead>
        <tbody>"""
    
    for result in validation_results:
        status = "INCLUDED" if result["overall_result"] else "EXCLUDED"
        status_class = "included" if result["overall_result"] else "excluded"
        blocks_info = f"{result['blocks_passed']}/{result['total_blocks']}"
        
        html_content += f"""
            <tr>
                <td>{result['filename']}</td>
                <td class="{status_class}">{status}</td>
                <td>{blocks_info}</td>
                <td>"""
        
        for block in result.get("block_results", []):
            status_icon = "✅" if block["passed"] else "❌"
            status_class = "pass" if block["passed"] else "fail"
            html_content += f'<span class="{status_class}">{status_icon} {block["block_name"]}</span><br>'
        
        html_content += """</td>
            </tr>"""
    
    html_content += """        </tbody>
    </table>
    
    <div style="margin-top: 30px; padding: 15px; background: #f0f0f0; border-radius: 5px;">
        <h3>📁 Output Files</h3>
        <ul>
            <li><strong>results/sorted_pdfs/include/</strong> - Papers meeting all criteria</li>
            <li><strong>results/sorted_pdfs/exclude/</strong> - Papers missing one or more criteria</li>
            <li><strong>results/validation_results.json</strong> - Raw validation data</li>
            <li><strong>results/summary_statistics.json</strong> - Summary statistics</li>
        </ul>
    </div>
</body>
</html>"""
    
    # Align with run_screening messaging and common expectations
    with open(f"{output_dir}/validation_report.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"HTML report generated: {output_dir}/validation_report.html")

def generate_summary_stats(validation_results, output_dir, failed_pdfs: list | None = None):
    """Generate summary statistics file."""
    
    total = len(validation_results)
    included = sum(1 for r in validation_results if r["overall_result"])
    excluded = total - included
    failed_count = len(failed_pdfs) if failed_pdfs else 0
    
    # Calculate block-level statistics
    block_stats = {}
    if validation_results and validation_results[0].get("block_results"):
        for result in validation_results:
            for block in result.get("block_results", []):
                block_name = block["block_name"]
                if block_name not in block_stats:
                    block_stats[block_name] = {"passed": 0, "total": 0}
                block_stats[block_name]["total"] += 1
                if block["passed"]:
                    block_stats[block_name]["passed"] += 1
    
    # Error breakdown for failed PDFs
    error_breakdown = {}
    if failed_pdfs:
        for failed in failed_pdfs:
            error_code = failed.get('error_code', 'UNKNOWN_ERROR')
            error_breakdown[error_code] = error_breakdown.get(error_code, 0) + 1
    
    summary = {
        "screening_date": datetime.now().isoformat(),
        "total_pdfs_submitted": total + failed_count,
        "successfully_processed": total,
        "failed_extraction": failed_count,
        "included_papers": included,
        "excluded_papers": excluded,
        "inclusion_rate": round(included/total*100, 1) if total > 0 else 0,
        "block_statistics": block_stats,
        "extraction_error_breakdown": error_breakdown if error_breakdown else None
    }
    
    with open(f"{output_dir}/summary_statistics.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    print(f"Summary statistics saved: {output_dir}/summary_statistics.json")
