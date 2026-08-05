"""
File: squareNumbers.py
Author: Somnath
Date: 17/07/26
Description: 
"""


def squareNumbers():
    sqr_num = [x**2 for x in range(1,31)]
    return sqr_num

if __name__ == '__main__':
    result = squareNumbers()
    print("Result is:", result)
