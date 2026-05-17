"""
File: firstLastElement.py
Author: Somnath
Date: 12/05/26
Description: Find First and Last Position of Element in Sorted Array
"""


def firstLastElement(nums, target):
        left = -1
        right = -1
        start, end = 0, len(nums) - 1

        while(start <= end):
            mid = (start + end) // 2

            if nums[mid] == target:
                left = mid
                end = mid - 1

            elif nums[mid] < target:
                start = mid + 1

            else:
                end = mid - 1

        start, end = 0, len(nums) - 1

        while (start <= end):
            mid = (start + end) // 2

            if nums[mid] == target:
                right = mid
                start = mid + 1

            elif nums[mid] < target:
                start = mid + 1

            else:
                end = mid - 1
        return [left, right]

if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    result = firstLastElement(nums, target)
    print("First and Last Position of Element in Sorted Array is:", result)
