# 🚀 Quick Start Guide — Universal Literature Screening Toolkit

Beginner-friendly steps to run your first screening in ~10 minutes.

Tip: Need more depth? See the full USER_GUIDE.md.

## What you’ll do

- Put your PDFs into a folder (default: input_pdfs)
- Write one Boolean query (query.txt)
- Run the tool and review a clean HTML report

## 1) Install and verify

Windows (PowerShell):

```powershell
Set-ExecutionPolicy Bypass -Scope Process
./scripts/setup_windows.ps1
./scripts/run_tests.ps1
```

macOS/Linux:

```bash
chmod +x scripts/setup_unix.sh scripts/run_tool.sh
./scripts/setup_unix.sh
python -m pytest tests -q
```

## 2) Prepare your data

- Create a folder named input_pdfs next to this file.
- Copy your PDFs into input_pdfs/ (flat — no subfolders for the first run).

Project layout example:

```
your_project/
├─ input_pdfs/
│  ├─ paper1.pdf
│  └─ paper2.pdf
└─ query.txt
```

## 3) Write your query (recommended)

Create query.txt and paste one Boolean query. Lines starting with # are comments and ignored.

Example:

```
# Forest decision-support focus with ES and management context; exclude economics
((forest* OR wood*) AND (management OR planning)) AND ("ecosystem service*" OR biodiversity) AND NOT (economics)
```

Quick syntax tips:

- Operators: NOT > AND > OR (use parentheses to group)
- Quotes for phrases: "ecosystem service"
- Wildcards: model* matches model, models, modeling, modelling

## 4) Run the tool

Windows (PowerShell):

```powershell
./scripts/run_tool.ps1 -InputPath "input_pdfs" -OutputPath "results" -QueryFile "query.txt"
```

macOS/Linux:

```bash
./scripts/run_tool.sh --input "input_pdfs" --output "results" --query-file "query.txt"
```

Or run the Python entry point directly:

```bash
python run_screening.py --input input_pdfs --output results --query-file query.txt
```

Outputs appear in results/:

```
results/
├─ validation_report.html   # Open in a browser
├─ validation_results.json  # Machine-readable
└─ sorted_pdfs/
   ├─ include/
   └─ exclude/
```

## 5) Example you can try now

We ship an example query at examples/query.txt.

Windows:

```powershell
./scripts/run_tool.ps1 -InputPath "input_pdfs" -OutputPath "example_results" -QueryFile "examples/query.txt"
```

macOS/Linux:

```bash
./scripts/run_tool.sh --input "input_pdfs" --output "example_results" --query-file "examples/query.txt"
```

## Troubleshooting (plain language)

- “Python not found”: Install from python.org; on Windows try `py -V`.
- Script blocked: `Set-ExecutionPolicy Bypass -Scope Process` (Windows).
- No PDFs found: Check files are in input_pdfs and have .pdf extension.
- No matches: Loosen your query (add OR synonyms, use wildcards).

Deprecation note: The older block-based --search-terms flow is still available for one transition release but will be removed. Prefer --query-file. In query mode, validation_logic in config.json is ignored.