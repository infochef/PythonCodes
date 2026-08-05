"""
File: evenIndexedChar.py
Author: Somnath
Date: 20/07/26
Description: Python program to print even indexed characters
"""


def evenIndexedChar(input_string):
    li = []
    for i, j in enumerate(input_string):
        if i % 2 == 0:
            li.append(j)
    return ''.join(li)



if __name__ == '__main__':
    input_string = 'Automation'
    result = evenIndexedChar(input_string)
    print("Result is:", result)
