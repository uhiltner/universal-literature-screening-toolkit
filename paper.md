---
title: 'Universal Literature Screening Toolkit: A Domain-Agnostic Tool for Automated, Reproducible Literature Screening'
doi: 10.5281/zenodo.17063676
tags:
  - Python
  - systematic review
  - literature screening
  - meta-analysis
  - research automation
  - PDF processing
  - multi-language
  - open science
authors:
  - name: Ulrike Hiltner
    orcid: 0000-0001-5663-7068
    equal-contrib: true
    affiliation: "1"
affiliations:
 - name: Forest Ecology, Institute of Terrestrial Ecosystems, Department of Environmental Systems Science, ETH Zurich, Zurich, Switzerland
   index: 1
date: 25 September 2025
bibliography: paper.bib
---

# Summary

The Universal Literature Screening Toolkit (ULST) is a configurable, cross-platform Python application designed to automate the initial screening phase of systematic literature reviews. It provides a domain-agnostic framework for processing large volumes of research papers against user-defined criteria, significantly accelerating evidence synthesis while maintaining methodological rigor. The tool operates on local PDF collections, applying complex, multi-lingual search logic that overcomes the limitations of many institutional search platforms. By generating auditable reports and organizing documents, the ULST makes the screening process faster, more consistent, and fully reproducible, thereby addressing a critical bottleneck in evidence-based research.

# Statement of Need

The manual screening of literature, particularly gray literature sourced from platforms with rudimentary search capabilities, is a well-documented bottleneck in systematic reviews. This process is not only labor-intensive but is also fraught with subjectivity and inconsistency, which can compromise the reproducibility and robustness of the scientific findings [@page2021prisma]. Researchers often assemble a broad corpus of documents with no effective means to apply a uniform, complex set of inclusion and exclusion criteria. This challenge is magnified when dealing with multi-lingual gray literature, where manual evaluation is exceptionally demanding.

The ULST is engineered to directly address this methodological gap. It provides a lightweight, standalone tool that empowers researchers to apply a precise, complex, and reproducible Boolean search strategy to a local corpus of documents. This capability is most critical when the initial data acquisition from databases or websites yields a large, noisy dataset that requires rigorous and objective filtering. By automating this screening process, the ULST eliminates reviewer subjectivity, ensures that every document is evaluated against the identical criteria, and produces a fully auditable and reproducible workflow. It thus provides a critical bridge between the limitations of data sources and the high standards of systematic, evidence-based science.

# Key Functionality

- **Domain-Agnostic and Configurable**: The ULST's screening logic is entirely driven by user-defined text files. Researchers specify search terms in thematic `BLOCK`s, which can be combined using Boolean `AND`/`OR` logic. This design ensures applicability across any research field.
- **Multi-Language Pattern Matching**: The toolkit effectively processes documents in any language that can be represented in UTF-8. It uses a case-insensitive matching engine with support for wildcards (`*`) and exact phrases (`"..."`), allowing for nuanced and comprehensive searches across international literature.
- **Robust PDF Text Extraction**: To maximize data recovery from diverse document formats, the ULST implements a dual-library extraction strategy, using PyMuPDF as the primary engine and falling back to pdfplumber for problematic files. This ensures high reliability in content extraction.
- **Auditable and Reproducible Outputs**: The toolkit produces a clear, actionable set of outputs for each run: an HTML report detailing the screening results and keyword evidence, a `validation_results.json` file for computational analysis, and the source PDFs automatically sorted into `include` and `exclude` subdirectories. This workflow ensures full transparency and reproducibility.
- **Cross-Platform and Dependency-Light**: As a pure Python application with minimal dependencies, the ULST runs consistently on Windows, macOS, and Linux. Setup is streamlined via simple shell and PowerShell scripts, making it accessible to researchers with limited command-line experience.

# Implementation and Architecture

The ULST is built on a modular, functional pipeline that ensures clarity and maintainability. The core components are:
- `pdf_extractor.py`: Manages the file-by-file text extraction process.
- `search_parser.py`: Reads and interprets the user's `search_terms.txt` file, compiling the raw text into a structured, searchable format.
- `validator.py`: Executes the core screening logic, applying the defined Boolean criteria to the extracted text of each document.
- `report_generator.py`: Consolidates the results and generates the final HTML and JSON outputs.

This decoupled architecture allows for straightforward testing and future extension of each component without altering the overall workflow. The program is executed via a single command-line entry point, `run_screening.py`, which orchestrates the flow of data through the pipeline.

# Illustrative Use Case: Ensuring Robustness in Gray Literature Reviews

A primary application of the ULST is to impose rigor and reproducibility on the screening of gray literature, where source platforms often lack sophisticated search tools. Consider a researcher tasked with reviewing environmental impact assessments from various regional authorities. The initial collection of several hundred PDF reports is gathered using basic keyword searches on disparate websites. The resulting corpus is heterogeneous, and manual screening would be highly subjective.

The ULST transforms this challenge into a robust, systematic process:
1.  **Corpus Assembly**: The researcher downloads all potentially relevant PDFs into a single directory.
2.  **Define a Precise Search Protocol**: A multi-faceted search strategy is codified in the `search_terms.txt` file. This protocol defines the exact, non-negotiable criteria for a document's inclusion, including multi-language terms for concepts like `modeling`, `forest management`, and `biodiversity`.
3.  **Automated, Objective Execution**: The researcher executes the toolkit. The ULST systematically processes each PDF, applying the exact same Boolean logic to every document. This removes all human subjectivity from the screening decision.
4.  **Auditable Outcome**: The output is a cleanly partitioned set of documents in `include` and `exclude` folders, accompanied by an HTML report that serves as an audit trail, detailing which keywords were found in each included document.

This workflow ensures that the final selection of literature is the product of a documented, reproducible, and entirely objective methodology. It elevates the scientific credibility of reviews that rely on gray literature by making the screening process as rigorous as that for peer-reviewed articles from indexed databases.

# Acknowledgements

We acknowledge the developers of the PyMuPDF and pdfplumber libraries, whose work provides the foundation for the robust PDF processing capabilities of this toolkit.

# References
