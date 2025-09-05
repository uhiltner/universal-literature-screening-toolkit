"""
Report Generator Module

Generates reports and sorts PDF files based on validation results.
"""

import json
import shutil
import os
from pathlib import Path
from datetime import datetime

def generate_reports(validation_results, search_blocks, input_pdf_dir, output_dir):
    """Generate all reports and sort files."""
    
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
    generate_html_report(validation_results, search_blocks, output_dir)
    
    # Generate summary statistics
    generate_summary_stats(validation_results, output_dir)

def sort_pdf_files(validation_results, input_dir, output_dir):
    """Sort PDF files into include/exclude folders."""
    
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
            dest_path = Path(output_dir) / "sorted_pdfs" / "include" / filename
            included_count += 1
        else:
            dest_path = Path(output_dir) / "sorted_pdfs" / "exclude" / filename
            excluded_count += 1
        
        try:
            shutil.copy2(source_path, dest_path)
        except Exception as e:
            print(f"Error copying {filename}: {e}")
    
    print(f"Files sorted: {included_count} included, {excluded_count} excluded")
    if missing_count > 0:
        print(f"Warning: {missing_count} PDF files were missing")

def generate_html_report(validation_results, search_blocks, output_dir):
    """Generate HTML report with detailed results."""
    
    total_papers = len(validation_results)
    included_papers = sum(1 for r in validation_results if r["overall_result"])
    excluded_papers = total_papers - included_papers
    
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <title>Literature Screening Results</title>
    <meta charset="UTF-8">
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
        .header {{ background: #f0f8ff; padding: 20px; border-radius: 10px; margin-bottom: 20px; }}
        .summary {{ background: #f9f9f9; padding: 15px; margin: 20px 0; border-radius: 5px; }}
        .block {{ margin: 10px 0; padding: 10px; border-left: 4px solid #007acc; background: #fafafa; }}
        .included {{ color: green; font-weight: bold; }}
        .excluded {{ color: red; font-weight: bold; }}
        table {{ border-collapse: collapse; width: 100%; margin-top: 20px; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; font-weight: bold; }}
        .criteria-list {{ list-style-type: none; padding: 0; }}
        .criteria-list li {{ padding: 2px 0; }}
        .pass {{ color: green; }}
        .fail {{ color: red; }}
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
        <p><strong>Total Papers Analyzed:</strong> {total_papers}</p>
        <p><strong>Papers Included:</strong> <span class="included">{included_papers} ({included_papers/total_papers*100:.1f}%)</span></p>
        <p><strong>Papers Excluded:</strong> <span class="excluded">{excluded_papers} ({excluded_papers/total_papers*100:.1f}%)</span></p>
    </div>
    
    <div class="block">
        <h2>🔍 Search Criteria Applied</h2>
        <p><strong>Validation Logic:</strong> Boolean AND (all blocks must pass)</p>
        <ul class="criteria-list">"""
    
    for i, block in enumerate(search_blocks, 1):
        html_content += f"<li><strong>Block {i}:</strong> {block['name']} ({len(block['terms'])} terms)</li>"
    
    html_content += """        </ul>
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
    
    with open(f"{output_dir}/final_report.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"HTML report generated: {output_dir}/final_report.html")

def generate_summary_stats(validation_results, output_dir):
    """Generate summary statistics file."""
    
    total = len(validation_results)
    included = sum(1 for r in validation_results if r["overall_result"])
    excluded = total - included
    
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
    
    summary = {
        "screening_date": datetime.now().isoformat(),
        "total_papers": total,
        "included_papers": included,
        "excluded_papers": excluded,
        "inclusion_rate": round(included/total*100, 1) if total > 0 else 0,
        "block_statistics": block_stats
    }
    
    with open(f"{output_dir}/summary_statistics.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    
    print(f"Summary statistics saved: {output_dir}/summary_statistics.json")
