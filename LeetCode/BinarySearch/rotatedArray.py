"""
File: rotatedArray.py
Author: Somnath
Date: 12/05/26
Description: Search in Rotated Sorted Array
"""


def rotatedArray(nums, target):
    start, end = 0, len(nums) - 1

    while start <= end:

        mid = (start + end) // 2

        if nums[mid] == target:
            return mid

        # LEFT HALF SORTED
        if nums[start] <= nums[mid]:

            # target lies inside left half
            if nums[start] <= target < nums[mid]:
                end = mid - 1

            else:
                start = mid + 1

        # RIGHT HALF SORTED
        else:

            # target lies inside right half
            if nums[mid] < target <= nums[end]:
                start = mid + 1

            else:
                end = mid - 1

    return -1

if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    result = rotatedArray(nums, target)
    print("Search in Rotated Sorted Array:", result)