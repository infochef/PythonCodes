"""
File: maximum_product_subarray.py
Author: Somnath
Date: 17/08/26
Description: 152. Maximum Product Subarray
"""


def maximum_product_subarray(arr):
    size = len(arr)
    maxi = float('-inf')
    pro = 1

    for i in range(0, size):
        pro *= arr[i]
        maxi = max(maxi, pro)
        if pro < 0:
            pro = 1
    return maxi

if __name__ == '__main__':
    arr = [2, 3, -2, 4]
    result = maximum_product_subarray(arr)
    print("Result is:", result)
