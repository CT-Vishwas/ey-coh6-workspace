from dataclasses import dataclass
import string
from datetime import datetime as dt

SUMMARY_LOG_FILE = "file_summary_log.txt"

@dataclass
class FileSummary:
    fname: str
    summary_timestamp: str
    num_lines: int
    num_words: int
    num_characters: int
    num_punctuations: int
    num_vowels: int
    num_digits: int


def main():
    file_path = input("Enter the path of the file to summarize: ")
    summary = FileSummary('','',0,0,0,0,0,0)
    try:
        with open(file_path, 'r') as fh:
            data = fh.read()
            # summary.fname =
            summary.summary_timestamp = dt.now().strftime("%Y-%m-%d %I:%M %p")
            summary.num_characters = len(data)
            for char in data:
                if char in 'aeiouAEIOU':
                    summary.num_vowels += 1
                if char.isdigit():
                    summary.num_digits += 1
                if char in string.punctuation:
                    summary.num_punctuations += 1

        with open(file_path,'r') as fh:
            data = fh.readlines()
            summary.num_lines = len(data)
            for line in data:
                summary.num_words += len(line.split())
        print(summary)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    
    with open(SUMMARY_LOG_FILE, 'a') as log_fh:
        log_fh.write(f"{summary}\n")

if __name__ == "__main__":
    main()