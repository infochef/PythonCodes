"""
File: sqrt.py
Author: Somnath
Date: 13/05/26
Description: Sqrt(x)
"""


def sqrt(x):

    start, end = 0, x
    while(start <= end):
        mid = (start + end) // 2

        if  mid * mid <=  x:
            start = mid + 1
        else:
            end = mid - 1

    return end


if __name__ == '__main__':
    x = 4
    result = sqrt(x)
    print("Square root of Element in Sorted Array is:", result)

