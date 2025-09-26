---
title: 'Universal Literature Screening Toolkit: A Domain-Agnostic Tool for Automated, Reproducible Literature Screening'
doi: 10.5281/zenodo.17202023
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

The Universal Literature Screening Toolkit (ULST) is a deterministic, cross-platform Python application that automates the screening of research papers against a user-defined search string. Many systematic reviews are hampered by institutional databases or search platforms that do not support complex, multi-term keyword searches. The ULST addresses this by enabling researchers to apply a precise, Boolean logic-based search string—identical to one used on platforms like Web of Science or Scopus—to a local collection of PDF documents. By processing the full text of each paper, the tool provides a simple "include" or "exclude" recommendation based on whether the defined criteria are met. This non-AI, keyword-driven approach removes the subjectivity and time-consuming guesswork of manual screening, enforcing a rigorous, reproducible, and auditable methodology that aligns with PRISMA guidelines and accelerates the evidence synthesis process.

# Statement of Need

A primary challenge in conducting systematic literature reviews is the inconsistent search capabilities of academic databases and digital libraries. While platforms like Scopus and Web of Science support complex, multi-faceted search strings, many institutional repositories, government websites, and other sources of peer-reviewed or gray literature offer only basic keyword search functionality. This limitation forces researchers to either use overly broad search terms, retrieving thousands of irrelevant documents, or to manually screen a large corpus of papers with a subjective and error-prone process. This manual "guesswork" is not only a significant time sink but also compromises the rigor and reproducibility required for high-quality evidence synthesis [@page2021prisma; @higgins2024cochrane].

The challenge of screening literature efficiently while maintaining methodological rigor has been recognized across multiple research domains [@khalil2022tools; @thomas2017living]. Existing automated screening tools are often domain-specific, require substantial technical setup, or lack the flexibility needed for diverse research applications [@marshall2017automating]. Furthermore, many tools rely on cloud-based platforms or require extensive preprocessing, making them unsuitable for researchers working with sensitive data or those with limited technical infrastructure.

The ULST is engineered to solve this specific problem. It decouples the search logic from the source platform, allowing a researcher to apply a sophisticated, pre-defined search string to *any* collection of PDF documents. This ensures that every paper is evaluated against the exact same objective criteria, regardless of where it was sourced. By automating this validation, the ULST eliminates the need for subjective manual checks, speeds up the screening process exponentially, and provides a transparent, auditable record of which papers met the inclusion criteria and why. It empowers researchers to maintain the highest standards of methodological rigor, even when working with documents from sources with limited technical capabilities.

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

This decoupled architecture allows for straightforward testing and future extension of each component without altering the overall workflow. The program is executed via a single command-line entry point, `run_screening.py`, which orchestrates the flow of data through the pipeline. A comprehensive `QUICK_START.md` guide is provided to ensure researchers without prior Python experience can set up and run the tool in minutes.

# Illustrative Use Case: Ensuring Robustness in Gray Literature Reviews

A primary application of the ULST is to impose rigor and reproducibility on the screening of gray literature, where source platforms often lack sophisticated search tools. Consider a researcher tasked with reviewing environmental impact assessments from various regional authorities. The initial collection of several hundred PDF reports is gathered using basic keyword searches on disparate websites. The resulting corpus is heterogeneous, and manual screening would be highly subjective.

The ULST transforms this challenge into a robust, systematic process:
1.  **Corpus Assembly**: The researcher downloads all potentially relevant PDFs into a single directory.
2.  **Define a Precise Search Protocol**: A multi-faceted search strategy is codified in the `search_terms.txt` file. This protocol defines the exact, non-negotiable criteria for a document's inclusion, including multi-language terms for concepts like `modeling`, `forest management`, and `biodiversity`.
3.  **Automated, Objective Execution**: The researcher executes the toolkit. The ULST systematically processes each PDF, applying the exact same Boolean logic to every document. This removes all human subjectivity from the screening decision.
4.  **Auditable Outcome**: The output is a cleanly partitioned set of documents in `include` and `exclude` folders, accompanied by an HTML report that serves as an audit trail, detailing which keywords were found in each included document.

This workflow ensures that the final selection of literature is the product of a documented, reproducible, and entirely objective methodology. It elevates the scientific credibility of reviews that rely on gray literature by making the screening process as rigorous as that for peer-reviewed articles from indexed databases.

# Acknowledgements

I acknowledge the developers of the PyMuPDF and pdfplumber libraries, whose work provides the foundation for the robust PDF processing capabilities of this toolkit.

# Statement on AI-Assisted Development

During the development of this software, I used AI-assisted coding tools (GitHub Copilot) as a development aid for code implementation tasks. However, the research methodology, software architecture design, domain expertise in systematic literature review processes, and the identification of the core research problem addressed by this toolkit represent original scholarly work. All algorithmic logic, validation approaches, and research applications were conceived and designed through domain expertise in systematic review methodology.

# References

Higgins, J. P. T., Thomas, J., Chandler, J., Cumpston, M., Li, T., Page, M. J., & Welch, V. A. (Eds.). (2024). *Cochrane Handbook for Systematic Reviews of Interventions* (6.5 ed.). Cochrane. https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current (Accessed online 2025-09-25)

Khalil, H., Ameen, D., & Zarnegar, A. (2022). Tools to support the automation of systematic reviews: a scoping review. *Journal of Clinical Epidemiology*, 144, 22-42. https://doi.org/10.1016/j.jclinepi.2021.12.005

Marshall, I., Kuiper, J., Banner, E., & Wallace, B. C. (2017). Automating Biomedical Evidence Synthesis: RobotReviewer. In M. Bansal & H. Ji (Eds.), *Proceedings of ACL 2017, System Demonstrations* (pp. 7-12). Association for Computational Linguistics.

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., ... & Moher, D. (2021). The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ*, 372, n71. https://doi.org/10.1136/bmj.n71

Thomas, J., Noel-Storr, A., Marshall, I., Wallace, B., McDonald, S., Mavergames, C., ... & Elliott, J. H. (2017). Living systematic reviews: 2. Combining human and machine effort. *Journal of Clinical Epidemiology*, 91, 31-37. https://doi.org/10.1016/j.jclinepi.2017.08.011
