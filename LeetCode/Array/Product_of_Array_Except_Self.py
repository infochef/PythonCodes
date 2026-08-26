"""
File: Product_of_Array_Except_Self.py
Author: Somnath
Date: 17/08/26
Description: 238. Product of Array Except Self
"""


def Product_of_Array_Except_Self(arr):
    res = [1] * (len(arr))
    prefix = 1
    for i in range(len(arr)):
        res[i] = prefix
        prefix *= arr[i]
    postfix = 1
    for i in range(len(arr) -1, -1, -1):
        res[i] *= postfix
        postfix *= arr[i]
    return res


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    result = Product_of_Array_Except_Self(nums)
    print("Result is:", result)
