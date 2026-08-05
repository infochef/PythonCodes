"""
File: search.py
Author: Somnath
Date: 19/07/26
Description: 
"""


def search(arr, tar):
    size = len(arr)
    start = 0
    end = size - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == tar:
            return mid
        elif arr[mid] < tar:
            start = mid + 1
        elif arr[mid] > tar:
            end = mid - 1
    return -1


if __name__ == '__main__':
    sorted_list = [10, 23, 35, 45, 50, 70, 85]
    target = 50
    result = search(sorted_list, target)
    print("Result is:", result)
