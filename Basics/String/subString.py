"""
File: subString.py
Author: Somnath
Date: 18/07/26
Description: Python program to get the last part of a string before a specified character.
"""


def subString(input_str):
    sb_string = input_str.split('-', 1)[0]
    return sb_string


if __name__ == '__main__':
    input_str = 'https://www.w3resource.com/python-exercises'
    result = subString(input_str)
    print("Result is:", result)
