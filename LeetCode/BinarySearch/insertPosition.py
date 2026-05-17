"""
File: insertPosition.py
Author: Somnath
Date: 13/05/26
Description: Search Insert Position
"""


def insertPosition(nums, target):
    start, end = 0, len(nums) - 1

    while(start <= end):
        mid = (start + end) // 2

        if target == nums[mid]:
            return mid

        elif target < nums[mid]:
            end = mid - 1

        elif target > nums[mid]:
            start = mid + 1
    return start

if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 2
    result = insertPosition(nums, target)
    print("Insert position of element in the array is:", result)
