"""
File: sorting.py
Author: Somnath
Date: 19/07/26
Description: 
"""


def sorting(arr):
    size = len(arr)

    for passes in range(size):
        for j in range(0, size - 1 - passes):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    lst = [64, 34, 25, 12, 22, 11, 90]
    result = sorting(lst)
    print("Result is:", result)
