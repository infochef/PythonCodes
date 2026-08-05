"""
File: removeSpace.py
Author: Somnath
Date: 20/07/26
Description: Python program to remove space from a given string
"""


def removeSpace(input_string):
    li = []
    for i in input_string:
        if i != ' ':
            li.append(i)
    return ''.join(li)


if __name__ == '__main__':
    input_string = 'Welcome to Java World'
    result = removeSpace(input_string)
    print("Result is:", result)
