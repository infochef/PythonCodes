"""
File: Rotated_Sorted_Array.py
Author: Somnath
Date: 18/08/26
Description: 33. Search in Rotated Sorted Array
"""


def Rotated_Sorted_Array(arr, target):
    size = len(arr)
    start, end = 0, size - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] <= arr[end]:
            if arr[mid] <= target <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
        elif arr[start] <= arr[mid]:
            if arr[start] <= target <= arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
    return -1

if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    result = Rotated_Sorted_Array(nums, target)
    print("Result is:", result)
