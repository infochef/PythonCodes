"""
File: binarySearch.py
Author: Somnath
Date: 19/07/26
Description: Python program for binary search.
"""


def binarySearch(arr, target):
    size = len(arr)
    start = 0
    end = size - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True, mid
        elif arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid - 1

    return False





if __name__ == '__main__':
    list1 = [1, 2, 3, 5, 8] # False
    target1 = 6
    list2 = [1, 2, 3, 5, 8] # True
    target2 = 5
    result = binarySearch(list2, target2)
    print("Result is:", result)
