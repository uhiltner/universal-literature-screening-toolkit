# Universal Literature Screening Toolkit v2.0

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17063676.svg)](https://doi.org/10.5281/zenodo.17063676)
[![License: MIT]( https##  Contributing

We welcome contributions from researchers and developers alike! See our [Contributing Guidelines](CONTRIBUTING.md) for details on how to participate.

This toolkit is designed to be extended and customized:

1. **Add new output formats** in `report_generator.py`
2. **Enhance language support** in `search_parser.py`
3. **Implement new validation logic** in `validator.py`
4. **Create domain templates** in additional configuration files

Please see our [Code of Conduct](CODE_OF_CONDUCT.md) for community guidelines.adge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![JOSS Status](https://joss.theoj.org/papers/10.21105/joss.XXXXX/status.svg)](https://joss.theoj.org/papers/10.21105/joss.XXXXX)
[![PyPI version](https://badge.fury.io/py/universal-literature-screening-toolkit.svg)](https://badge.fury.io/py/universal-literature-screening-toolkit)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A configurable, cross-platform tool for systematic literature review and automated paper screening. This toolkit can be adapted for any research domain and supports multiple languages.

> **Accelerate your systematic reviews**: Process hundreds of papers in minutes instead of days while maintaining research rigor.

## 📖 Citation

If you use this toolkit in your research, please cite it as:

```bibtex
@software{hiltner2025universal,
  author       = {Hiltner, Ulrike},
  title        = {Universal Literature Screening Toolkit},
  month        = sep,
  year         = 2025,
  publisher    = {Zenodo},
  version      = {2.0.0},
  doi          = {10.5281/zenodo.17063676},
  url          = https://doi.org/10.5281/zenodo.17063676}
}
```

See [CITATION.cff](CITATION.cff) for other citation formats or [PUBLICATION.md](PUBLICATION.md) for publication details.

##  Key Features

- **Domain Agnostic**: Works with any research field and search criteria
- **Multi-language Support**: Handles Unicode text in any language
- **Configurable Logic**: Choose AND/OR validation logic per your needs
- **Cross-platform**: Runs on Windows, macOS, and Linux
- **Professional Reports**: Generates HTML reports and organizes PDFs
- **Easy Customization**: Simple text-based configuration files

##  Quick Start

### 1. Setup
`ash

# Create Python virtual environment
python -m venv venv

# Activate environment (Windows)
venv\Scripts\activate
# OR Activate environment (macOS/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
`

### 2. Prepare Your Data
`
your_project/
 input_pdfs/          # JSON files extracted from PDFs
 search_terms.txt     # Your search criteria
 config.json          # Validation settings (optional)
 results/             # Output directory (created automatically)
`

### 3. Run Screening
`ash
python run_screening.py --input input_pdfs --output results --search-terms search_terms.txt
`

##  Configuration

### Search Terms Format (search_terms.txt)
`
# Define your search blocks
BLOCK 1: Primary Concept
keyword1*, keyword2, "exact phrase", concept*

BLOCK 2: Secondary Concept  
term1, term2*, "another exact phrase"

BLOCK 3: Context
context1*, environment*, domain*
`

### Configuration File (config.json)
`json
{
  "validation_logic": {
    "default_operator": "AND",
    "block_combinations": {
      "blocks": ["3A", "3B"],
      "operator": "AND", 
      "combined_name": "Combined Block Name"
    }
  },
  "domain_info": {
    "research_area": "Your Research Domain",
    "description": "Description of your review"
  }
}
`

##  Language Support

The toolkit automatically handles:
- **Unicode text** (UTF-8 encoding)
- **Case-insensitive matching**
- **Wildcard patterns** (*)
- **Exact phrases** ("quotes")
- **Multi-language content**

##  Output

The toolkit generates:
- **HTML Report**: Professional validation report with statistics
- **JSON Results**: Machine-readable validation data
- **Organized PDFs**: Sorted into include/exclude folders (if PDFs available)

##  Customization Examples

### Medical Literature Review
`
BLOCK 1: Medical Condition
diabetes*, "type 2 diabetes", "diabetes mellitus"

BLOCK 2: Treatment
treatment*, therapy*, intervention*, medication*

BLOCK 3: Study Type
"randomized controlled trial", "clinical trial", "systematic review"
`

### Environmental Science
`
BLOCK 1: Environmental Context
climate*, environment*, ecosystem*, biodiversity*

BLOCK 2: Impact Assessment
impact*, effect*, consequence*, change*

BLOCK 3: Methodology
model*, simulation*, analysis*, "remote sensing"
`

### Social Science
`
BLOCK 1: Population
adolescent*, teenager*, youth*, "young adult*"

BLOCK 2: Behavior
behavior*, behaviour*, attitude*, perception*

BLOCK 3: Method
survey*, interview*, questionnaire*, "mixed method*"
`

##  Project Structure

`
literature_screening_toolkit/
 run_screening.py         # Main entry point
 config.json             # Configuration settings
 search_terms.txt         # Search criteria template
 requirements.txt         # Python dependencies
 scripts/                 # Core modules
    search_parser.py     # Search term processing
    validator.py         # Validation logic
    pdf_extractor.py     # Content extraction
    report_generator.py  # Output generation
 docs/                    # Documentation
     README.md            # This file
     user_manual.md       # Detailed usage guide
`

##  Contributing

This toolkit is designed to be extended and customized:

1. **Add new output formats** in 
eport_generator.py
2. **Enhance language support** in search_parser.py
3. **Implement new validation logic** in alidator.py
4. **Create domain templates** in additional configuration files

##  Citation

If you use this toolkit in your research, please cite:

`
Universal Literature Screening Toolkit v2.0
Automated systematic literature review tool
https://github.com/your-repo/literature-screening-toolkit
`

##  License

This project is licensed under the MIT License - see the LICENSE file for details.

##  Support

For questions, issues, or feature requests:
1. Check the user manual (user_manual.md)
2. Review example configurations
3. Open an issue on GitHub
4. Contact the development team

---

**Made for researchers, by researchers** 
