"""
File: Palingdrome.py
Author: Somnath
Date: 19/07/26
Description: Python program to check if a number is palingdrome or not
"""


def Palingdrome(num):
    arr = list(num)
    size = len(arr)
    start = 0
    end = size - 1

    while start <= end :
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    reversed_num = ''.join(arr)
    if num == reversed_num:
        return f"{num} is palingdrome"
    else:
        return f"{num} is not a palingdrome"

if __name__ == '__main__':
    num = '101'
    result = Palingdrome(num)
    print("Result is:", result)
