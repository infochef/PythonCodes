"""
File: vowelsConstants.py
Author: Somnath
Date: 20/07/26
Description: Python program to Count Vowels and Consonants in a given string
"""


def vowelsConstants(input_string, vowels_list):
    vowels = 0
    constants = 0

    for i in input_string:
        if i != ' ':
            if i in vowels_list:
                vowels += 1
            else:
                constants += 1

    return f"In the given string total number of vowels: {vowels} and constants: {constants}"

if __name__ == '__main__':
    vowels_list = ['a','e','i','o','u']
    input_string = "Hello World";
    result = vowelsConstants(input_string, vowels_list)
    print("Result is:", result)
