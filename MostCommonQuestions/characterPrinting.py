"""
File: characterPrinting.py
Author: Somnath
Date: 20/07/26
Description: Python program to print each letter twice from a given string
"""


def characterPrinting(input_string):
    li = []
    arr = [x for x in input_string]
    for i in arr:
        c = i*2
        li.append(c)
    return ''.join(li)

if __name__ == '__main__':
    input_string = 'hello'
    result = characterPrinting(input_string)
    print("Result is:", result)
