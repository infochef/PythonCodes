"""
File: removeSpecificElements.py
Author: Somnath
Date: 17/07/26
Description: 
"""


def removeSpecificElements(color):
    color = [x for(i,x) in enumerate(color) if i not in (0,4,5)]
    return color


if __name__ == '__main__':
    color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    result = removeSpecificElements(color)
    print("Result is:", result)
