# Universal Literature Screening Toolkit v2.0# Universal Literature Screening Toolkit v2.0



[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17063676.svg)](https://doi.org/10.5281/zenodo.17063676)[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17063676.svg)](https://doi.org/10.5281/zenodo.17063676)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![License: MIT]( https##  Contributing

[![JOSS Status](https://joss.theoj.org/papers/10.21105/joss.XXXXX/status.svg)](https://joss.theoj.org/papers/10.21105/joss.XXXXX)

[![PyPI version](https://badge.fury.io/py/universal-literature-screening-toolkit.svg)](https://badge.fury.io/py/universal-literature-screening-toolkit)We welcome contributions from researchers and developers alike! See our [Contributing Guidelines](CONTRIBUTING.md) for details on how to participate.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

This toolkit is designed to be extended and customized:

A configurable, cross-platform tool for systematic literature review and automated paper screening. This toolkit can be adapted for any research domain and supports multiple languages.

1. **Add new output formats** in `report_generator.py`

> **Accelerate your systematic reviews**: Process hundreds of papers in minutes instead of days while maintaining research rigor.2. **Enhance language support** in `search_parser.py`

3. **Implement new validation logic** in `validator.py`

## 📖 Citation4. **Create domain templates** in additional configuration files



If you use this toolkit in your research, please cite it as:Please see our [Code of Conduct](CODE_OF_CONDUCT.md) for community guidelines.adge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![JOSS Status](https://joss.theoj.org/papers/10.21105/joss.XXXXX/status.svg)](https://joss.theoj.org/papers/10.21105/joss.XXXXX)

```bibtex[![PyPI version](https://badge.fury.io/py/universal-literature-screening-toolkit.svg)](https://badge.fury.io/py/universal-literature-screening-toolkit)

@software{hiltner2025universal,[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

  author       = {Hiltner, Ulrike},

  title        = {Universal Literature Screening Toolkit},A configurable, cross-platform tool for systematic literature review and automated paper screening. This toolkit can be adapted for any research domain and supports multiple languages.

  month        = sep,

  year         = 2025,> **Accelerate your systematic reviews**: Process hundreds of papers in minutes instead of days while maintaining research rigor.

  publisher    = {Zenodo},

  version      = {2.0.0},## 📖 Citation

  doi          = {10.5281/zenodo.17063676},

  url          = {https://doi.org/10.5281/zenodo.17063676}If you use this toolkit in your research, please cite it as:

}

``````bibtex

@software{hiltner2025universal,

See [CITATION.cff](CITATION.cff) for other citation formats.  author       = {Hiltner, Ulrike},

  title        = {Universal Literature Screening Toolkit},

## ✨ Key Features  month        = sep,

  year         = 2025,

- **Domain Agnostic**: Works with any research field and search criteria  publisher    = {Zenodo},

- **Multi-language Support**: Handles Unicode text in any language  version      = {2.0.0},

- **Configurable Logic**: Choose AND/OR validation logic per your needs  doi          = {10.5281/zenodo.17063676},

- **Cross-platform**: Runs on Windows, macOS, and Linux  url          = https://doi.org/10.5281/zenodo.17063676}

- **Professional Reports**: Generates HTML reports and organizes PDFs}

- **Easy Customization**: Simple text-based configuration files```



## 🚀 Quick StartSee [CITATION.cff](CITATION.cff) for other citation formats or [PUBLICATION.md](PUBLICATION.md) for publication details.



### 1. Setup##  Key Features

```bash

# Create Python virtual environment- **Domain Agnostic**: Works with any research field and search criteria

python -m venv venv- **Multi-language Support**: Handles Unicode text in any language

- **Configurable Logic**: Choose AND/OR validation logic per your needs

# Activate environment (Windows)- **Cross-platform**: Runs on Windows, macOS, and Linux

venv\Scripts\activate- **Professional Reports**: Generates HTML reports and organizes PDFs

# OR Activate environment (macOS/Linux)- **Easy Customization**: Simple text-based configuration files

source venv/bin/activate

##  Quick Start

# Install dependencies

pip install -r requirements.txt### 1. Setup

````ash



### 2. Prepare Your Data# Create Python virtual environment

```python -m venv venv

your_project/

├── input_pdfs/          # JSON files extracted from PDFs# Activate environment (Windows)

├── search_terms.txt     # Your search criteriavenv\Scripts\activate

├── config.json          # Validation settings (optional)# OR Activate environment (macOS/Linux)

└── results/             # Output directory (created automatically)source venv/bin/activate

```

# Install dependencies

### 3. Run Screeningpip install -r requirements.txt

```bash`

python run_screening.py --input input_pdfs --output results --search-terms search_terms.txt

```### 2. Prepare Your Data

`

## ⚙️ Configurationyour_project/

 input_pdfs/          # JSON files extracted from PDFs

### Search Terms Format (search_terms.txt) search_terms.txt     # Your search criteria

``` config.json          # Validation settings (optional)

# Define your search blocks results/             # Output directory (created automatically)

BLOCK 1: Primary Concept`

keyword1*, keyword2, "exact phrase", concept*

### 3. Run Screening

BLOCK 2: Secondary Concept  `ash

term1, term2*, "another exact phrase"python run_screening.py --input input_pdfs --output results --search-terms search_terms.txt

`

BLOCK 3: Context

context1*, environment*, domain*##  Configuration

```

### Search Terms Format (search_terms.txt)

### Configuration File (config.json)`

```json# Define your search blocks

{BLOCK 1: Primary Concept

  "validation_logic": {keyword1*, keyword2, "exact phrase", concept*

    "default_operator": "AND",

    "block_combinations": {BLOCK 2: Secondary Concept  

      "blocks": ["3A", "3B"],term1, term2*, "another exact phrase"

      "operator": "AND", 

      "combined_name": "Combined Block Name"BLOCK 3: Context

    }context1*, environment*, domain*

  },`

  "domain_info": {

    "research_area": "Your Research Domain",### Configuration File (config.json)

    "description": "Description of your review"`json

  }{

}  "validation_logic": {

```    "default_operator": "AND",

    "block_combinations": {

## 🌐 Language Support      "blocks": ["3A", "3B"],

      "operator": "AND", 

The toolkit automatically handles:      "combined_name": "Combined Block Name"

- **Unicode text** (UTF-8 encoding)    }

- **Case-insensitive matching**  },

- **Wildcard patterns** (*)  "domain_info": {

- **Exact phrases** ("quotes")    "research_area": "Your Research Domain",

- **Multi-language content**    "description": "Description of your review"

  }

## 📊 Output}

`

The toolkit generates:

- **HTML Report**: Professional validation report with statistics##  Language Support

- **JSON Results**: Machine-readable validation data

- **Organized PDFs**: Sorted into include/exclude folders (if PDFs available)The toolkit automatically handles:

- **Unicode text** (UTF-8 encoding)

## 🎯 Customization Examples- **Case-insensitive matching**

- **Wildcard patterns** (*)

### Medical Literature Review- **Exact phrases** ("quotes")

```- **Multi-language content**

BLOCK 1: Medical Condition

diabetes*, "type 2 diabetes", "diabetes mellitus"##  Output



BLOCK 2: TreatmentThe toolkit generates:

treatment*, therapy*, intervention*, medication*- **HTML Report**: Professional validation report with statistics

- **JSON Results**: Machine-readable validation data

BLOCK 3: Study Type- **Organized PDFs**: Sorted into include/exclude folders (if PDFs available)

"randomized controlled trial", "clinical trial", "systematic review"

```##  Customization Examples



### Environmental Science### Medical Literature Review

````

BLOCK 1: Environmental ContextBLOCK 1: Medical Condition

climate*, environment*, ecosystem*, biodiversity*diabetes*, "type 2 diabetes", "diabetes mellitus"



BLOCK 2: Impact AssessmentBLOCK 2: Treatment

impact*, effect*, consequence*, change*treatment*, therapy*, intervention*, medication*



BLOCK 3: MethodologyBLOCK 3: Study Type

model*, simulation*, analysis*, "remote sensing""randomized controlled trial", "clinical trial", "systematic review"

````



### Social Science### Environmental Science

````

BLOCK 1: PopulationBLOCK 1: Environmental Context

adolescent*, teenager*, youth*, "young adult*"climate*, environment*, ecosystem*, biodiversity*



BLOCK 2: BehaviorBLOCK 2: Impact Assessment

behavior*, behaviour*, attitude*, perception*impact*, effect*, consequence*, change*



BLOCK 3: MethodBLOCK 3: Methodology

survey*, interview*, questionnaire*, "mixed method*"model*, simulation*, analysis*, "remote sensing"

````



## 📁 Project Structure### Social Science

`

```BLOCK 1: Population

universal-literature-screening-toolkit/adolescent*, teenager*, youth*, "young adult*"

├── run_screening.py         # Main entry point

├── config.json             # Configuration settingsBLOCK 2: Behavior

├── search_terms.txt         # Search criteria templatebehavior*, behaviour*, attitude*, perception*

├── requirements.txt         # Python dependencies

├── scripts/                 # Core modulesBLOCK 3: Method

│   ├── search_parser.py     # Search term processingsurvey*, interview*, questionnaire*, "mixed method*"

│   ├── validator.py         # Validation logic`

│   ├── pdf_extractor.py     # Content extraction

│   └── report_generator.py  # Output generation##  Project Structure

├── tests/                   # Test suite

├── examples/                # Example configurations`

├── input_pdfs/             # Sample input dataliterature_screening_toolkit/

├── CITATION.cff            # Citation information run_screening.py         # Main entry point

├── LICENSE                 # MIT License config.json             # Configuration settings

├── CODE_OF_CONDUCT.md      # Community guidelines search_terms.txt         # Search criteria template

└── CONTRIBUTING.md         # Contribution guidelines requirements.txt         # Python dependencies

``` scripts/                 # Core modules

    search_parser.py     # Search term processing

## 🧪 Testing    validator.py         # Validation logic

    pdf_extractor.py     # Content extraction

Run the comprehensive test suite:    report_generator.py  # Output generation

 docs/                    # Documentation

```bash     README.md            # This file

# Install testing dependencies (if not already installed)     user_manual.md       # Detailed usage guide

pip install pytest`



# Run all tests##  Contributing

pytest tests/ -v

This toolkit is designed to be extended and customized:

# Run specific test modules

pytest tests/test_search_parser.py -v1. **Add new output formats** in 

```eport_generator.py

2. **Enhance language support** in search_parser.py

## 🤝 Contributing3. **Implement new validation logic** in alidator.py

4. **Create domain templates** in additional configuration files

We welcome contributions from researchers and developers alike! See our [Contributing Guidelines](CONTRIBUTING.md) for details on how to participate.

##  Citation

This toolkit is designed to be extended and customized:

If you use this toolkit in your research, please cite:

1. **Add new output formats** in `report_generator.py`

2. **Enhance language support** in `search_parser.py``

3. **Implement new validation logic** in `validator.py`Universal Literature Screening Toolkit v2.0

4. **Create domain templates** in additional configuration filesAutomated systematic literature review tool

https://github.com/your-repo/literature-screening-toolkit

Please see our [Code of Conduct](CODE_OF_CONDUCT.md) for community guidelines.`



## 📄 License##  License



This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.This project is licensed under the MIT License - see the LICENSE file for details.



## 💬 Support##  Support



For questions, issues, or feature requests:For questions, issues, or feature requests:

1. Check the [USER_GUIDE.md](USER_GUIDE.md) for detailed documentation1. Check the user manual (user_manual.md)

2. Review example configurations in the `examples/` directory2. Review example configurations

3. Open an issue on GitHub3. Open an issue on GitHub

4. Contact the development team4. Contact the development team



------



**Made for researchers, by researchers** 🔬**Made for researchers, by researchers** 
