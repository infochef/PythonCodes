"""
File: selectionSort.py
Author: Somnath
Date: 02/05/26
Description: Python program to perform selection sort in an array
"""


def main(arr):
    size = len(arr)

    for i in range(size):
        min_index = i

        for j in range(i+1, size):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

if __name__ == '__main__':
    unsorted_list = [12, 25, 11, 34, 90, 22]
    sorted_list = main(unsorted_list)
    print("After performing selection sort final array is:", sorted_list)