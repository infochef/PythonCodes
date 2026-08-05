"""
File: uniqueCharacters.py
Author: Somnath
Date: 20/07/26
Description:  Python program to print unqiue characters
"""


def uniqueCharacters(input_string):
    li = []

    for i in input_string:
        if i not in li:
            li.append(i)

    return ' '.join(li)

if __name__ == '__main__':
    input_string = 'Java Automation'
    result = uniqueCharacters(input_string)
    print("Result is:", result)
