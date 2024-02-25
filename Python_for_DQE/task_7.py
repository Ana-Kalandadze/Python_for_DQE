# Calculate number of words and letters from previous Homeworks 5/6 output test file.
# Create two csv:
# 1.word-count (all words are preprocessed in lowercase)
# 2.letter, cout_all, count_uppercase, percentage (add header, spacecharacters are not included)
# CSVs should be recreated each time new record added.

import csv
from collections import Counter
import re

class WordCounter:
    def __init__(self, file_path):
        self.file_path = file_path

    def compute_counts(self):
        with open(self.file_path, 'r') as file:
            data = file.read().replace('\n', ' ')
        data = re.sub(r'[^\w\s]', '', data).lower()
        words = data.split()
        word_count = Counter(words)
        return word_count

    def write_to_csv(self, counts, output_file='word_counts.csv'):
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Word', 'Count'])
            for key, value in counts.items():
                writer.writerow([key, value])



class LetterCounter:
    def __init__(self, file_path):
        self.file_path = file_path

    def compute_counts(self):
        with open(self.file_path, 'r') as file:
            data = file.read().replace('\n', '')
        
        letters_only = re.sub(r'[^a-zA-Z]', '', data)
        all_counts = Counter(letters_only.lower())
        uppercase_counts = Counter(c for c in letters_only if c.isupper())
        return all_counts, uppercase_counts

    def write_to_csv(self, all_counts, uppercase_counts, output_file='letter_counts.csv'):
        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Letter', 'Count All', 'Count Uppercase'])
            for letter, count_all in all_counts.items():
                count_uppercase = uppercase_counts.get(letter.upper(), 0)
                writer.writerow([letter, count_all, count_uppercase])



