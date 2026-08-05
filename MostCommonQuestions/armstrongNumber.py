"""
File: armstrongNumber.py
Author: Somnath
Date: 19/07/26
Description: Python program to check if a given number is armstrong number or not
"""


def armstrongNumber(num):

    converted_list = [x for x in num]
    print(converted_list)

    size = len(num)
    s = 0
    for i in converted_list:
        s += int(i)**size

    if s == int(num):
        return f'{num} is a armstrong number'
    else:
        return f'{num} is not a armstrong number'


if __name__ == '__main__':
    num = '153'
    result = armstrongNumber(num)
    print("Result is:", result)
