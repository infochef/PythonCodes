"""
File: binarySearch.py
Author: Somnath
Date: 02/05/26
Description: Python program to perform binary search in an array
"""


def main(arr, target):

    size = len(arr)
    start = 0
    end = size - 1

    while(start <= end):
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid # found target value

        elif arr[mid] > target:
            end = mid - 1 # if middle element is greater than target element then change the end position

        elif arr[mid] < target:
            start = mid + 1 # if middle element is less than target element then change the start position

    return -1 # if the element is not present in the array

if __name__ == '__main__':
    sorted_list = [10, 23, 35, 45, 50, 70, 85]
    target = 50
    result = main(sorted_list, target)
    print("Result for binary search operation is:", result)
