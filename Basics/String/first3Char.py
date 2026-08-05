"""
File: first3Char.py
Author: Somnath
Date: 18/07/26
Description: Python function to get a string made of the first three characters of a specified string. If the length of the string is less than 3, return the original string.
"""


def first3Char(string):
    new_string = string[:3]
    return new_string


if __name__ == '__main__':
    input_str = 'python'
    result = first3Char(input_str)
    print("Result is:", result)
