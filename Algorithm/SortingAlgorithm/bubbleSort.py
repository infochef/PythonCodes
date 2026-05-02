"""
File: bubbleSort.py
Author: Somnath
Date: 02/05/26
Description: Python program to perform bubble sort in an array
"""


def main(arr):
    size = len(arr)

    for passes in range(size):
        for j in range(0, size-1-passes):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    lst = [64, 34, 25, 12, 22, 11, 90]
    lst1 = [5, 4, 3, 2, 1]
    result = main(lst)
    print("After performing bubble sort final sorted array is:", result)
