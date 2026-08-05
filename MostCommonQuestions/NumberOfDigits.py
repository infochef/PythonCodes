"""
File: NumberOfDigits.py
Author: Somnath
Date: 19/07/26
Description: Python program to check number of digits
"""


def NumberOfDigits(num):
    count = 0
    for _ in num:
        count += 1
    return count

if __name__ == '__main__':
    num = '14345'
    result = NumberOfDigits(num)
    print("Result is:", result)
