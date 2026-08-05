"""
File: others.py
Author: Somnath
Date: 04/08/26
Description: 
"""


def others(nums, tar):
    li = {}

    for i, n in enumerate(nums):
        diff = tar - n
        if diff in li:
            return [li[diff], i]
        li[n] = i

    return

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    result = others(nums, target)
    print("Result for the two sum problem is:", result)

