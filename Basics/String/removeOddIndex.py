"""
File: removeOddIndex.py
Author: Somnath
Date: 18/07/26
Description: Remove odd index chars from a string.
"""


def removeOddIndex(c):

    result = [x for i, x in enumerate(c) if i%2 == 0]
    return ''.join(result)

if __name__ == '__main__':
    char_str = 'python'
    result = removeOddIndex(char_str)
    print("Result is:", result)
