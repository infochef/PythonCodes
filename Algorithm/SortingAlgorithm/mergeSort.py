"""
File: mergeSort.py
Author: Somnath
Date: 05/05/26
Description: Python program to perform quick sort in an array
"""


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    empty_list = []
    i = j = 0

    while i < len(left) and j < len (right):
        if left[i] < right[j]:
            empty_list.append(left[i])
            i += 1
        else:
            empty_list.append(right[j])
            j += 1

    empty_list.extend(left[i:])
    empty_list.extend(right[j:])

    return empty_list

if __name__ == '__main__':
    unsorted_array =[38, 27, 43, 3, 9, 82, 10]
    sorted_list = merge_sort(unsorted_array)
    print("After performing merge sort final array is:", sorted_list)
