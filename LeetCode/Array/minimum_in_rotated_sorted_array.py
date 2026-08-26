"""
File: minimum_in_rotated_sorted_array.py
Author: Somnath
Date: 18/08/26
Description: 153. Find Minimum in Rotated Sorted Array
"""


def minimum_in_rotated_sorted_array(nums):
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] <= nums[r]:
             r = mid
        else:
             l = mid + 1
    return nums[l]

if __name__ == '__main__':
    nums = [3, 4, 5, 1, 2]
    result = minimum_in_rotated_sorted_array(nums)
    print("Result is:", result)
