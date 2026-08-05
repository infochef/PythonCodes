"""
File: evenNumbersRemoval.py
Author: Somnath
Date: 17/07/26
Description: 
"""


def evenNumbersRemoval(num):
    num = [i for i in num if i%2 != 0]
    return num

if __name__ == '__main__':
    num = [7, 8, 120, 25, 44, 20, 27]
    result = evenNumbersRemoval(num)
    print("Result is:", result)
