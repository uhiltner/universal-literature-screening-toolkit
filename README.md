# Universal Literature Screening Toolkit (ULST)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17063676.svg)](https://doi.org/10.5281/zenodo.17063676)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![JOSS Status](https://joss.theoj.org/papers/10.21105/joss.XXXXX/status.svg)](https://joss.theoj.org/papers/10.21105/joss.XXXXX)
[![PyPI version](https://badge.fury.io/py/universal-literature-screening-toolkit.svg)](https://badge.fury.io/py/universal-literature-screening-toolkit)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

The Universal Literature Screening Toolkit (ULST) is a configurable, cross-platform Python application designed to automate the initial screening phase of systematic literature reviews. It provides a domain-agnostic framework for processing large volumes of research papers against user-defined criteria, significantly accelerating evidence synthesis while maintaining methodological rigor.

## Statement of Need

Systematic reviews, particularly those involving gray literature from sources with limited or basic search functionalities, present a significant challenge. Researchers often retrieve a broad collection of documents with no way to apply a complex, rigorous, and reproducible screening methodology. This manual screening process is not only a time-consuming bottleneck but is also prone to inconsistency and subjectivity, undermining the robustness of the research.

The ULST is engineered to solve this problem. It empowers researchers to apply a sophisticated, multi-lingual search strategy to a local collection of PDFs, ensuring that every document is evaluated against the exact same criteria. This is especially critical for gray literature where initial retrieval cannot be precise. The toolkit transforms a subjective manual task into a transparent, auditable, and reproducible scientific workflow, drastically reducing screening time while enhancing methodological rigor.

## Core Functionality

- **Domain-Agnostic by Design**: The toolkit is not bound to any specific field. Its screening logic is defined by simple text files, allowing for complete customization for any research domain (e.g., medicine, environmental science, social sciences).
- **Configurable Boolean Logic**: Researchers can define complex inclusion and exclusion criteria using `BLOCK`-based search terms with `AND`/`OR` operators, mirroring the logic of advanced database searches.
- **Multi-Language Content Processing**: The tool seamlessly processes and analyzes content in multiple languages, including English, German, and French, by leveraging case-insensitive and wildcard-enabled pattern matching.
- **Robust PDF Text Extraction**: A dual-library approach (PyMuPDF and pdfplumber) ensures reliable extraction of text from a wide variety of PDF formats and qualities.
- **Reproducible, Auditable Outputs**: The toolkit generates a professional HTML report, a `results.json` file for data analysis, and automatically sorts the source PDFs into `include` and `exclude` folders, ensuring a fully documented and reproducible workflow.

## Application Example: Screening Gray Literature in Environmental Science

To illustrate its core strength, consider a review of regional environmental impact reports—a classic form of gray literature. These reports are often sourced from various governmental and non-governmental websites that lack advanced search capabilities. A researcher might download hundreds of PDF reports based on simple title searches. The challenge is to then screen this diverse collection against a precise, multi-faceted search string to ensure every included report meets the specific criteria for the review.

**1. Defining the Search Criteria**

The researcher establishes a robust search strategy in `dss4es_search_terms.txt`, defining the essential concepts for inclusion:

```
BLOCK 1: Modeling Context
model*, simulation, "decision support system", optimi*

BLOCK 2: Forest Context
forest*, wald, forst, forêt, woodland, silvicultur*

BLOCK 3: Management Context
management, plan*, bewirtschaftung, gestion, aménagement

BLOCK 4: Biodiversity & Ecosystem Services (BES)
biodiversity*, "ecosystem service*", ökosystemleistung*, schutzwald
```

**2. Automated, Reproducible Screening**

The toolkit processes the entire collection of PDF reports. For a German-language report like `Hiltner_NaiS_Steinschlagprofil_Bericht_update_final.pdf`, the process is objective and reproducible:
- The tool extracts all text from the PDF.
- It systematically validates the content against the four search blocks using strict `AND` logic.
- The paper is confirmed to contain terms matching all four blocks: "modell" (BLOCK 1), "wald" and "forst" (BLOCK 2), "bewirtschaftung" (BLOCK 3), and "schutzwald" (a term for protection forests, conceptually linked to ecosystem services, in BLOCK 4).

**3. Objective and Auditable Outcome**

The toolkit classifies the paper as `include` and moves the PDF to the `results/sorted_pdfs/include` directory. The specific keywords found are logged as evidence in the final HTML and JSON reports. This process eliminates the subjectivity of manual screening and creates a fully auditable trail, ensuring the final selection of literature is robust and reproducible.

## Quick Start

For a gentle introduction, please see the [**QUICK_START.md**](QUICK_START.md). For advanced users:

1.  **Setup Environment**:
    ```bash
    # For Windows (PowerShell)
    .\scripts\setup_windows.ps1

    # For macOS/Linux
    ./scripts/setup_unix.sh
    ```

2.  **Run Screening**:
    ```bash
    # Execute the tool with your data
    python run_screening.py --input /path/to/your/pdfs --output /path/to/results --search-terms your_search_terms.txt
    ```

## Citation

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
  url          = {https://doi.org/10.5281/zenodo.17063676}
}
```

## Contributing

We welcome contributions. Please read [CONTRIBUTING.md](CONTRIBUTING.md) and our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
