"""
File: quickSort.py
Author: Somnath
Date: 03/05/26
Description: Python program to perform quick sort in an array
"""


def main(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return main(left) + middle + main(right)

if __name__ == '__main__':
    unsorted_list = [12, 25, 11, 34, 90, 22]
    sorted_list = main(unsorted_list)
    print("After performing quick sort final array is:", sorted_list)
