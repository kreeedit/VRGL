import os
import re
from fuzzywuzzy import fuzz
from tqdm import tqdm

def fuzzy_search(text, keyword, threshold):
    """
    Performs a fuzzy search within a given text for a specific keyword.

    Args:
        text (str): The text to search within.
        keyword (str): The keyword to search for.
        threshold (int): The minimum similarity ratio required for a match (0-100).

    Returns:
        bool: True if a match is found, False otherwise.
    """
    words = text.split()
    for word in words:
        if fuzz.ratio(word.lower(), keyword.lower()) >= threshold:
            return True
    return False

def search_files(directory, file_ending, keywords, output_file, search_part='all', threshold=80):
    """
    Searches for files within a directory and its subdirectories, looking for specific keywords.

    Args:
        directory (str): The path to the directory to search.
        file_ending (str): The file extension to filter files by (e.g., ".txt").
        keywords (list): A list of keywords to search for.
        output_file (str): The name of the file to write the search results to.
        search_part (str, optional): The part of the file to search in ('beginning', 'middle', 'end', or 'all'). Defaults to 'all'.
        threshold (int, optional): The minimum similarity ratio required for a keyword match (0-100). Defaults to 80.
    """
    with open(output_file, 'w', encoding='utf-8') as out_file:
        total_files = sum(1 for root, _, files in os.walk(directory) for file in files if file.endswith(file_ending))

        with tqdm(total=total_files, desc="Searching files", unit="file") as pbar:
            for root, _, files in os.walk(directory):
                for file in files:
                    if file.endswith(file_ending):
                        file_path = os.path.join(root, file)
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                content = f.read()

                                total_length = len(content)
                                part_length = total_length // 3  # Divide into three roughly equal parts
                                beginning = content[:part_length]
                                middle = content[part_length:2*part_length]
                                end = content[2*part_length:]

                                if search_part == 'beginning':
                                    search_content = beginning
                                elif search_part == 'middle':
                                    search_content = middle
                                elif search_part == 'end':
                                    search_content = end
                                else:  # 'all' or any other value
                                    search_content = content

                                all_keywords_present = all(fuzzy_search(search_content, keyword, threshold) for keyword in keywords)
                                if all_keywords_present:
                                    result = f"File: {file_path}\n"
                                    result += f"Searched in: {search_part}\n"
                                    result += "Keywords found:\n"
                                    for keyword in keywords:
                                        matches = re.finditer(r'\b\w+\b', search_content)
                                        for match in matches:
                                            word = match.group()
                                            if fuzz.ratio(word.lower(), keyword.lower()) >= threshold:
                                                result += f"- {keyword} (matched as '{word}')\n"
                                                result += f"  Position: {match.start()}\n"
                                                result += f"  Context: ...{search_content[max(0, match.start()-50):match.end()+50]}...\n"
                                    result += "\n"
                                    out_file.write(result)
                        except Exception as e:
                            print(f"Error reading file {file_path}: {str(e)}")
                        finally:
                            pbar.update(1)

def main():
    """
    Get user input and initiate the file search.
    """
    directory = input("Enter the directory path to search: ")
    file_ending = input("Enter the file ending to search for (e.g., .txt, .pdf): ")
    keywords = input("Enter keywords to search for (comma-separated): ").split(',')
    keywords = [keyword.strip() for keyword in keywords]
    output_file = input("Enter the output file name: ")
    search_part = input("Enter the part of the document to search (beginning/middle/end/all): ").lower()

    while True:
        try:
            threshold = int(input("Enter the fuzzy search threshold (0-100, default is 80): ") or "80")
            if 0 <= threshold <= 100:
                break
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

    search_files(directory, file_ending, keywords, output_file, search_part, threshold)
    print(f"Search complete. Results written to {output_file}")

if __name__ == "__main__":
    main()

