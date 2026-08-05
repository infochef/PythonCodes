"""
File: Factorial.py
Author: Somnath
Date: 19/07/26
Description: Python program to find factorial of number
"""


def Factorial(n):

    p = 1
    for i in range(1, n+1):
        p *= i

    return p

if __name__ == '__main__':
    n = 5
    result = Factorial(n)
    print("Result is:", result)
