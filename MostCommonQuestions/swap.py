"""
File: swap.py
Author: Somnath
Date: 19/07/26
Description: Python program to swap two numbers without using third variable
"""


def swap(a, b):
    a = a + b
    b = a - b
    a = a - b

    return a, b

if __name__ == '__main__':
    a, b = 5, 10
    result = swap(a, b)
    print("Result is:", result)
