"""
File: evenOdd.py
Author: Somnath
Date: 19/07/26
Description: Python program to Find Odd or Even number
"""


def evenOdd():
    num = int(input("Enter the number to verify: "))
    if num % 2 == 0:
        return f"{num} is even number"
    else:
        return f"{num} is odd number"


if __name__ == '__main__':
    result = evenOdd()
    print("Result is:", result)
