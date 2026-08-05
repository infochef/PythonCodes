"""
File: missingNumber.py
Author: Somnath
Date: 20/07/26
Description: 
"""


def missingNumber(arr):

    for i in range(arr[0], len(arr)):
        if i not in arr:
            return i
    return -1

if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6,8]
    result = missingNumber(arr)
    print("Result is:", result)
