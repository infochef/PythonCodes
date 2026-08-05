"""
File: reverse.py
Author: Somnath
Date: 19/07/26
Description: Python program to reverse a list without built in function
"""


def reverse(arr):
    start = 0
    end = len(arr) - 1

    while start <= end:
        arr[start], arr[end] = arr[end], arr[start]

        start += 1
        end -= 1

    return arr

if __name__ == '__main__':
    lst = [1,2,3,4,5]
    string = 'hello'
    result = reverse(string)
    print("Result is:", result)
