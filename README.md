# VRGL: Versatile Regex (& keyword) Guided Locator

This small Python script performs a powerful fuzzy keyword search within files located in a specified directory and its subdirectories. It utilizes the `fuzzywuzzy` library for flexible matching and provides detailed search results, including file paths, matched keywords, and their context within the specific part (beggining, middle or end) of the files.

## Features

* **Fuzzy Matching:** Finds keywords even with slight variations or misspellings.  It calculates a similarity score between two strings ranging from 0 (completely different) to 100 (perfect match). The algorithm considers various factors like character insertions, deletions, substitutions, and transpositions to determine how closely the strings resemble each other.
   * Threshold = 100 (exact match)
   * Threshold = 90 (allows for very minor variations): Small spelling mistakes, Slight differences in capitalization, Perhaps a single character insertion or deletion
   * Threshold = 80 (more flexibility in matching): More significant spelling errors, Variations in word forms, Potentially even synonyms or closely related term

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
## Example result

```bash
File: /media/folder/folder/folder/b6f491b6385274394257545007dc2adb/fda868c30ee4784a0ac54927f88f7a51/filename.tenor.txt
Searched in: middle
Keywords found:
- postquam (matched as 'postquam')
  Position: 3534
  Context: ...icionen! dictorum doininoriim regis et marchionis postquam nobis de transgressione hujiismodi constiterit le...
- homagcium (matched as 'homagium')
  Position: 1313
  Context: ...udum récépissé ju- ramentum quoque fidelitatis et homagium ipsi regí Boemie et suis heredibus seu successori...
- homagcium (matched as 'homagium')
  Position: 2359
  Context: ...tes finniter qnod regibus ac corone regni Boeinie homagium, fidem et juramenta fidelitatis per ipsos prestit...

File: /media/folder/folder/folder/folder/4a33a5fa9c1a4d9aed6a540d14cda4d1/09a7f900f6588b00c5f464590c192daf/filname.tenor.txt
Searched in: middle
Keywords found:
- postquam (matched as 'postquam')
  Position: 2039
  Context: ...ores suos, dicte ciuitatis Tribuses expugnatores, postquam nobis omagium fidelitatis fecerant, ad pacem nost...
- homagcium (matched as 'omagium')
  Position: 2054
  Context: ...e ciuitatis Tribuses expugnatores, postquam nobis omagium fidelitatis fecerant, ad pacem nostram recipiamus...

```
