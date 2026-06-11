# define a function to input - read the file path
import string


def get_file_path():
    return input("Enter the file path: ")

# count number of characters - read() - len()
def count_characters(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return len(content)
    
# count number of lines - readlines() - len()
def count_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return len(lines)

# count number of words - readlines() - for each line split() - len() - add()
def count_words(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        word_count = 0
        for line in lines:
            words = line.split()
            word_count += len(words)
        return word_count

# count number of punctuations - read() - for each char - string.punctuation
# count number of digits - read() - for each char - string.digits
def count_digits(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        digit_count = 0
        for char in content:
            if char in string.digits:
                digit_count += 1
        return digit_count

# Define vowels - do same as above
def count_vowels(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        vowel_count = 0
        vowels = "aeiouAEIOU"
        for char in content:
            if char in vowels:
                vowel_count += 1
        return vowel_count