"""
File: maximum_subarray.py
Author: Somnath
Date: 17/08/26
Description: 53. Maximum Subarray
"""


def maximum_subarray(arr):
    size = len(nums)
    maxi = float('-inf')
    total = 0

    for i in range(0, size):
        total += arr[i]
        maxi = max(maxi, total)
        if total < 0:
            total = 0
    return maxi


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = maximum_subarray(nums)
    print("Result is:", result)
