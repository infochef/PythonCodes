"""
File: keyBasedRemoval.py
Author: Somnath
Date: 17/07/26
Description: 
"""


def keyBasedRemoval(dic):
    del dic['c']
    return dic

if __name__ == '__main__':
    myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    result = keyBasedRemoval(myDict)
    print("Result is:", result)
