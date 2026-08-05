"""
File: reverseString.py
Author: Somnath
Date: 20/07/26
Description: Python program to reverse a string
"""


def reverseString(string):

    arr = [x for x in string]
    size = len(arr)
    start = 0
    end = size - 1

    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return ''.join(arr)


if __name__ == '__main__':
    string = 'hello'
    result = reverseString(string)
    print("Result is:", result)
