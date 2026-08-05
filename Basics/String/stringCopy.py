"""
File: stringCopy.py
Author: Somnath
Date: 18/07/26
Description: Python function to get a string made of 4 copies of the last two characters of a specified string
"""


def stringCopy(input_str):

    emty_str = ''
    if len(input_str) < 2:
        return f'{input_str} length is less than 2'

    last_two_char = input_str[-2:]
    four_occurence = last_two_char * 4
    print(four_occurence)
    for i in four_occurence:
        emty_str += i

    return emty_str

if __name__ == '__main__':
    input_str = 'Exercises'
    result = stringCopy(input_str)
    print("Result is:", result)
