"""
File: two_sum.py
Author: Somnath
Date: 10/05/26
Description: Python program to solve leet code problem
"""


def main(arr, target):
    li = {}
    for i, n in enumerate(arr):
        diff = target - n
        if diff in li:
            return [li[diff], i]
        li[n] = i
    return


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = main(nums, target)
    print("Result for the two sum problem is:", result)
