"""
File: sortDictionary.py
Author: Somnath
Date: 18/07/26
Description: Sort Dictionary by Key
"""


def sortDictionary(color_dict):

    sortedByKey = {k: v for k, v in sorted(color_dict.items())}
    sortedByValue = {k: v for k, v in sorted(color_dict.items(), key= lambda v: v[1])}
    sortedByDesc = {k: v for k, v in sorted(color_dict.items(), key= lambda v: v[1], reverse=True)}
    return sortedByKey, sortedByValue, sortedByDesc


if __name__ == '__main__':
    color_dict = {
        'red': '#FF0000',
        'green': '#008000',
        'black': '#000000',
        'white': '#FFFFFF'
    }
    result = sortDictionary(color_dict)
    print("Result is:", result)
