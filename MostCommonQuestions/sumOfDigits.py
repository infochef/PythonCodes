"""
File: sumOfDigits.py
Author: Somnath
Date: 20/07/26
Description: Python program to check sum of all the digits
"""


def sumOfDigits(num):
    s = 0
    for i in num:
        s += int(i)
    return s



if __name__ == '__main__':
    number = '12345'
    result = sumOfDigits(number)
    print("Result is:", result)
