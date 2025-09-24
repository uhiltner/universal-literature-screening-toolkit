# Quick Start Guide for the Universal Literature Screening Toolkit

Welcome! This guide will walk you through using the toolkit to automatically screen your research papers. No advanced computer skills are needed—just follow these simple steps.

## 🎯 What This Tool Does

This toolkit reads through a folder of PDF articles and automatically sorts them based on keywords that you provide. It's designed to save you hundreds of hours on your literature review.

---

## 🚀 Getting Started: A Step-by-Step Guide

Follow these six steps to get up and running in about 5-10 minutes.

### Step 1: Make Sure You Have Python

The toolkit is written in Python, a popular programming language. If you don't have it, you can download it for free.

*   Go to the official Python website: [python.org](https://www.python.org/downloads/)
*   Download the latest version (3.8 or newer).
*   During installation, **make sure to check the box that says "Add Python to PATH"**. This is very important!

### Step 2: Prepare the Toolkit's Workspace

Next, we need to set up a clean, private workspace for the toolkit. This ensures it won't interfere with any other programs on your computer. You'll only need to do this once.

1.  **Open a Terminal (Command Prompt):**
    *   **On Windows:** Click the Start menu and type `cmd` or `PowerShell`, then press Enter.
    *   **On Mac:** Open the "Terminal" app (you can find it in Applications > Utilities).
    *   **On Linux:** Open your distribution's Terminal application.

2.  **Navigate to the Toolkit Folder:**
    In the terminal, you need to move into the toolkit's directory. Use the `cd` (change directory) command. For example:
    ```
    cd path/to/your/universal-literature-screening-toolkit
    ```
    *(You can drag and drop the folder onto the terminal window to get the correct path!)*

3.  **Run the Setup Commands:**
    Copy and paste the following commands into your terminal one by one.

    *   This first command creates a private "virtual space" for the toolkit.
        ```bash
        python -m venv venv
        ```

    *   This next command "activates" that private space.
        *   **On Windows:**
          ```bash
          venv\Scripts\activate
          ```
        *   **On Mac or Linux:**
          ```bash
          source venv/bin/activate
          ```
        *(You'll know it worked if you see `(venv)` appear at the start of your terminal prompt.)*

    *   This final command installs the helper tools the toolkit needs to read PDFs and create reports.
        ```bash
        pip install -r requirements.txt
        ```

### Step 3: Add Your PDF Files

This is where you put the papers you want to screen.

1.  Find the folder named `input_pdfs` inside the toolkit's main directory.
2.  Copy and paste all of your PDF files directly into this `input_pdfs` folder.

**Important:** Please do not rename or move the `input_pdfs` folder. The toolkit is programmed to look for your files right there.

### Step 4: Define Your Search Keywords

Now, tell the toolkit what to look for.

1.  Open the file named `search_terms.txt` with any simple text editor (like Notepad or TextEdit).
2.  Define your keywords in groups called "BLOCKS". The tool will search for these terms in the title, abstract, and keywords of each paper.

    *Example for a study on climate change impacts:*
    ```
    BLOCK 1: Core Concept
    climate change, global warming, greenhouse effect

    BLOCK 2: Impact
    impact, effect, consequence

    BLOCK 3: Location
    forest, marine, arctic
    ```
    *You can use `*` as a wildcard (e.g., `forest*` finds "forest," "forestry," "forests") and `" "` for exact phrases (e.g., `"climate change"`).*

**Pro Tip:** We've included templates! You can copy the contents from one of the files in the `examples/` folder (e.g., `medical_literature_terms.txt`) and paste them into your `search_terms.txt` to get started quickly.

### Step 5: Run the Screening!

You're ready to go! Run the main command to start the process.

*   Go back to your terminal (make sure it still has `(venv)` at the prompt).
*   Copy and paste the following command and press Enter:
    ```bash
    python run_screening.py --input input_pdfs --output results --search-terms search_terms.txt
    ```
This command tells the program to:
*   **`--input`**: Look for PDFs in the `input_pdfs` folder.
*   **`--output`**: Save the results in a new folder called `results`.
*   **`--search-terms`**: Use your keywords from `search_terms.txt`.

The toolkit will now start processing your files. It may take a few minutes if you have many PDFs.

### Step 6: View Your Results

Once the tool is finished, a new folder named `results` will appear. Inside, you will find:

*   `validation_report.html`: A user-friendly visual report. **Open this file in a web browser** (like Chrome, Firefox, or Edge) to see a summary of the screening.
*   `validation_results.json`: A data file for advanced users who might want to do further analysis.
*   **Organized PDF Folders**: The toolkit also creates sub-folders and sorts your original PDFs into `included` and `excluded` piles for you (if it can find the original PDF files).

---

## 🆘 Need More Help?

*   For more advanced settings, check the `README.md` file.
*   If you run into any issues, feel free to open an issue on the project's GitHub page.

**You are now ready to automate your literature review!** 🚀
