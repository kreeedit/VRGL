# VRGL: Versatile Regex & Keyword Guided Locator within Charters

This small Python script performs a powerful fuzzy keyword search within files located in a specified directory and its subdirectories. It utilizes the `fuzzywuzzy` library for flexible matching and provides detailed search results, including file paths, matched keywords, and their context within the files.

## Features

* **Fuzzy Matching:** Finds keywords even with slight variations or misspellings.
* **Customizable Search:** 
    * Filter files by extension.
    * Specify the part of the file to search (beginning, middle, end, or all).
    * Adjust the fuzzy matching threshold.

## Installation

1. Make sure you have Python installed on your system. You can download it from [https://www.python.org/](https://www.python.org/).

2. Install the required libraries using `pip`:

   ```bash
   pip install fuzzywuzzy tqdm
   ```

## How to Use

1. **Save the Script**

2. **Run the Script:** Open your terminal or command prompt and navigate to the directory where you saved the script. Then execute it:

   ```bash
   python fuzzy_search.py
   ```

3. **Provide Input:** The script will prompt you to enter the following information:

    * **Directory Path:** The path to the directory you want to search.
    * **File Ending:** The file extension to filter by (e.g., `.txt`, `.pdf` or 'tenor.txt" if you use Georg's extractor).
    * **Keywords:** A comma-separated list of keywords to search for.
    * **Output File Name:** The name of the file where the search results will be saved.
    * **Search Part:** The part of the file to search in ('beginning', 'middle', 'end', or 'all').
    * **Threshold:** The minimum similarity ratio for a keyword match (0-100).

4. **View Results:** Once the search is complete, the results will be written to the specified output file.

## Example

```bash
Enter the directory path to search: /path/to/your/documents
Enter the file ending to search for (e.g., .txt, .pdf): .txt
Enter keywords to search for (comma-separated): data analysis, machine learning, python
Enter the output file name: search_results.txt
Enter the part of the document to search (beginning/middle/end/all): all
Enter the fuzzy search threshold (0-100, default is 80): 
Search complete. Results written to search_results.txt
```

**Note:** The script handles potential errors when reading files and provides informative messages in case of issues.

