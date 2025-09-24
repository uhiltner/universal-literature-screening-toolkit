# Universal Literature Screening Toolkit v2.0# Universal Literature Screening Toolkit v2.0# Universal Literature Screening Toolkit v2.0



[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17063676.svg)](https://doi.org/10.5281/zenodo.17063676)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![JOSS Status](https://joss.theoj.org/papers/10.21105/joss.XXXXX/status.svg)](https://joss.theoj.org/papers/10.21105/joss.XXXXX)[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17063676.svg)](https://doi.org/10.5281/zenodo.17063676)[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17063676.svg)](https://doi.org/10.5281/zenodo.17063676)

[![PyPI version](https://badge.fury.io/py/universal-literature-screening-toolkit.svg)](https://badge.fury.io/py/universal-literature-screening-toolkit)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![License: MIT]( https##  Contributing



A configurable, cross-platform tool for systematic literature review and automated paper screening. This toolkit can be adapted for any research domain and supports multiple languages.[![JOSS Status](https://joss.theoj.org/papers/10.21105/joss.XXXXX/status.svg)](https://joss.theoj.org/papers/10.21105/joss.XXXXX)



> **Accelerate your systematic reviews**: Process hundreds of papers in minutes instead of days while maintaining research rigor.[![PyPI version](https://badge.fury.io/py/universal-literature-screening-toolkit.svg)](https://badge.fury.io/py/universal-literature-screening-toolkit)We welcome contributions from researchers and developers alike! See our [Contributing Guidelines](CONTRIBUTING.md) for details on how to participate.



## 📖 Citation[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)



If you use this toolkit in your research, please cite it as:This toolkit is designed to be extended and customized:



```bibtexA configurable, cross-platform tool for systematic literature review and automated paper screening. This toolkit can be adapted for any research domain and supports multiple languages.

@software{hiltner2025universal,

  author       = {Hiltner, Ulrike},1. **Add new output formats** in `report_generator.py`

  title        = {Universal Literature Screening Toolkit},

  month        = sep,> **Accelerate your systematic reviews**: Process hundreds of papers in minutes instead of days while maintaining research rigor.2. **Enhance language support** in `search_parser.py`

  year         = 2025,

  publisher    = {Zenodo},3. **Implement new validation logic** in `validator.py`

  version      = {2.0.0},

  doi          = {10.5281/zenodo.17063676},## 📖 Citation4. **Create domain templates** in additional configuration files

  url          = {https://doi.org/10.5281/zenodo.17063676}

}

```

If you use this toolkit in your research, please cite it as:Please see our [Code of Conduct](CODE_OF_CONDUCT.md) for community guidelines.adge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

See [CITATION.cff](CITATION.cff) for other citation formats.

[![JOSS Status](https://joss.theoj.org/papers/10.21105/joss.XXXXX/status.svg)](https://joss.theoj.org/papers/10.21105/joss.XXXXX)

## ✨ Key Features

```bibtex[![PyPI version](https://badge.fury.io/py/universal-literature-screening-toolkit.svg)](https://badge.fury.io/py/universal-literature-screening-toolkit)

- **Domain Agnostic**: Works with any research field and search criteria

- **Multi-language Support**: Handles Unicode text in any language@software{hiltner2025universal,[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

- **Configurable Logic**: Choose AND/OR validation logic per your needs

- **Cross-platform**: Runs on Windows, macOS, and Linux  author       = {Hiltner, Ulrike},

- **Professional Reports**: Generates HTML reports and organizes PDFs

- **Easy Customization**: Simple text-based configuration files  title        = {Universal Literature Screening Toolkit},A configurable, cross-platform tool for systematic literature review and automated paper screening. This toolkit can be adapted for any research domain and supports multiple languages.



## 🚀 Quick Start  month        = sep,



**New to Python or command-line tools?** 👉 See [QUICK_START.md](QUICK_START.md) for a detailed beginner's guide!  year         = 2025,> **Accelerate your systematic reviews**: Process hundreds of papers in minutes instead of days while maintaining research rigor.



### Experienced Users - Fast Track:  publisher    = {Zenodo},



```bash  version      = {2.0.0},## 📖 Citation

# 1. Setup (automated)

./scripts/setup_unix.sh        # Linux/Mac  doi          = {10.5281/zenodo.17063676},

# OR

.\scripts\setup_windows.ps1    # Windows  url          = {https://doi.org/10.5281/zenodo.17063676}If you use this toolkit in your research, please cite it as:



# 2. Run with example data}

./scripts/run_tool.sh --input input_pdfs --output results --search-terms examples/search_terms_dss4es.txt

``````bibtex

# 3. Use your own data  

./scripts/run_tool.sh --input /path/to/your/pdfs --output /path/to/results --search-terms your_search_terms.txt@software{hiltner2025universal,

```

See [CITATION.cff](CITATION.cff) for other citation formats.  author       = {Hiltner, Ulrike},

## ⚙️ Configuration

  title        = {Universal Literature Screening Toolkit},

### Search Terms Format (search_terms.txt)

```## ✨ Key Features  month        = sep,

# Define your search blocks

BLOCK 1: Primary Concept  year         = 2025,

keyword1*, keyword2, "exact phrase", concept*

- **Domain Agnostic**: Works with any research field and search criteria  publisher    = {Zenodo},

BLOCK 2: Secondary Concept  

term1, term2*, "another exact phrase"- **Multi-language Support**: Handles Unicode text in any language  version      = {2.0.0},



BLOCK 3: Context- **Configurable Logic**: Choose AND/OR validation logic per your needs  doi          = {10.5281/zenodo.17063676},

context1*, environment*, domain*

```- **Cross-platform**: Runs on Windows, macOS, and Linux  url          = https://doi.org/10.5281/zenodo.17063676}



### Configuration File (config.json)- **Professional Reports**: Generates HTML reports and organizes PDFs}

```json

{- **Easy Customization**: Simple text-based configuration files```

  "validation_logic": {

    "default_operator": "AND",

    "block_combinations": {

      "blocks": ["3A", "3B"],## 🚀 Quick StartSee [CITATION.cff](CITATION.cff) for other citation formats or [PUBLICATION.md](PUBLICATION.md) for publication details.

      "operator": "AND", 

      "combined_name": "Combined Block Name"

    }

  },### 1. Setup##  Key Features

  "domain_info": {

    "research_area": "Your Research Domain",```bash

    "description": "Description of your review"

  }# Create Python virtual environment- **Domain Agnostic**: Works with any research field and search criteria

}

```python -m venv venv- **Multi-language Support**: Handles Unicode text in any language



## 🌐 Language Support- **Configurable Logic**: Choose AND/OR validation logic per your needs



The toolkit automatically handles:# Activate environment (Windows)- **Cross-platform**: Runs on Windows, macOS, and Linux

- **Unicode text** (UTF-8 encoding)

- **Case-insensitive matching**venv\Scripts\activate- **Professional Reports**: Generates HTML reports and organizes PDFs

- **Wildcard patterns** (*)

- **Exact phrases** ("quotes")# OR Activate environment (macOS/Linux)- **Easy Customization**: Simple text-based configuration files

- **Multi-language content**

source venv/bin/activate

## 📊 Output

##  Quick Start

The toolkit generates:

- **HTML Report**: Professional validation report with statistics# Install dependencies

- **JSON Results**: Machine-readable validation data

- **Organized PDFs**: Sorted into include/exclude folders (if PDFs available)pip install -r requirements.txt### 1. Setup



## 🎯 Customization Examples````ash



### Medical Literature Review

```

BLOCK 1: Medical Condition### 2. Prepare Your Data# Create Python virtual environment

diabetes*, "type 2 diabetes", "diabetes mellitus"

```python -m venv venv

BLOCK 2: Treatment

treatment*, therapy*, intervention*, medication*your_project/



BLOCK 3: Study Type├── input_pdfs/          # JSON files extracted from PDFs# Activate environment (Windows)

"randomized controlled trial", "clinical trial", "systematic review"

```├── search_terms.txt     # Your search criteriavenv\Scripts\activate



### Environmental Science├── config.json          # Validation settings (optional)# OR Activate environment (macOS/Linux)

```

BLOCK 1: Environmental Context└── results/             # Output directory (created automatically)source venv/bin/activate

climate*, environment*, ecosystem*, biodiversity*

```

BLOCK 2: Impact Assessment

impact*, effect*, consequence*, change*# Install dependencies



BLOCK 3: Methodology### 3. Run Screeningpip install -r requirements.txt

model*, simulation*, analysis*, "remote sensing"

``````bash`



### Social Sciencepython run_screening.py --input input_pdfs --output results --search-terms search_terms.txt

```

BLOCK 1: Population```### 2. Prepare Your Data

adolescent*, teenager*, youth*, "young adult*"

`

BLOCK 2: Behavior

behavior*, behaviour*, attitude*, perception*## ⚙️ Configurationyour_project/



BLOCK 3: Method input_pdfs/          # JSON files extracted from PDFs

survey*, interview*, questionnaire*, "mixed method*"

```### Search Terms Format (search_terms.txt) search_terms.txt     # Your search criteria



## 📁 Project Structure``` config.json          # Validation settings (optional)



```# Define your search blocks results/             # Output directory (created automatically)

universal-literature-screening-toolkit/

├── run_screening.py         # Main entry pointBLOCK 1: Primary Concept`

├── config.json             # Configuration settings

├── search_terms.txt         # Search criteria templatekeyword1*, keyword2, "exact phrase", concept*

├── requirements.txt         # Python dependencies

├── scripts/                 # Core modules### 3. Run Screening

│   ├── search_parser.py     # Search term processing

│   ├── validator.py         # Validation logicBLOCK 2: Secondary Concept  `ash

│   ├── pdf_extractor.py     # Content extraction

│   └── report_generator.py  # Output generationterm1, term2*, "another exact phrase"python run_screening.py --input input_pdfs --output results --search-terms search_terms.txt

├── tests/                   # Test suite

├── examples/                # Example configurations`

├── input_pdfs/             # Sample input data

├── CITATION.cff            # Citation informationBLOCK 3: Context

├── LICENSE                 # MIT License

├── CODE_OF_CONDUCT.md      # Community guidelinescontext1*, environment*, domain*##  Configuration

└── CONTRIBUTING.md         # Contribution guidelines

``````



## 🧪 Testing### Search Terms Format (search_terms.txt)



Run the comprehensive test suite:### Configuration File (config.json)`



```bash```json# Define your search blocks

# Install testing dependencies (if not already installed)

pip install pytest{BLOCK 1: Primary Concept



# Run all tests  "validation_logic": {keyword1*, keyword2, "exact phrase", concept*

pytest tests/ -v

    "default_operator": "AND",

# Run specific test modules

pytest tests/test_search_parser.py -v    "block_combinations": {BLOCK 2: Secondary Concept  

```

      "blocks": ["3A", "3B"],term1, term2*, "another exact phrase"

## 🤝 Contributing

      "operator": "AND", 

We welcome contributions from researchers and developers alike! See our [Contributing Guidelines](CONTRIBUTING.md) for details on how to participate.

      "combined_name": "Combined Block Name"BLOCK 3: Context

This toolkit is designed to be extended and customized:

    }context1*, environment*, domain*

1. **Add new output formats** in `report_generator.py`

2. **Enhance language support** in `search_parser.py`  },`

3. **Implement new validation logic** in `validator.py`

4. **Create domain templates** in additional configuration files  "domain_info": {



Please see our [Code of Conduct](CODE_OF_CONDUCT.md) for community guidelines.    "research_area": "Your Research Domain",### Configuration File (config.json)



## 📄 License    "description": "Description of your review"`json



This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.  }{



## 💬 Support}  "validation_logic": {



For questions, issues, or feature requests:```    "default_operator": "AND",

1. **Beginners**: Start with [QUICK_START.md](QUICK_START.md)

2. **Detailed docs**: Check the [USER_GUIDE.md](USER_GUIDE.md)    "block_combinations": {

3. **Examples**: Review configurations in the `examples/` directory

4. **Issues**: Open an issue on GitHub## 🌐 Language Support      "blocks": ["3A", "3B"],

5. **Contact**: Reach out to the development team

      "operator": "AND", 

---

The toolkit automatically handles:      "combined_name": "Combined Block Name"

**Made for researchers, by researchers** 🔬
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
