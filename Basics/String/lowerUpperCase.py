"""
File: lowerUpperCase.py
Author: Somnath
Date: 18/07/26
Description: 
"""


def lowerUpperCase(word):
    word_upper_case = word.upper()
    word_lower_case = word.lower()
    return word_lower_case, word_upper_case

if __name__ == '__main__':
    word_list = "What's your favorite language?"
    result = lowerUpperCase(word_list)
    print("Result is:", result)
