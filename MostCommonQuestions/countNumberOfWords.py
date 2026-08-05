"""
File: countNumberOfWords.py
Author: Somnath
Date: 20/07/26
Description: Python program to count the number of words in a string
"""


def countNumberOfWords(string):
    arr = string.split()
    count = 0
    for _ in arr:
        count += 1
    return count

if __name__ == '__main__':
    string = 'Welcome to Java World'
    result = countNumberOfWords(string)
    print("Result is:", result)
