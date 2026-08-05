"""
File: arraySort.py
Author: Somnath
Date: 20/07/26
Description: Sort an array without using in-built method
"""


def arraySort(array):

    if len(array) <= 1:
        return array

    pivot = array[len(array) // 2]
    left = [x for x in array if x < pivot]
    mid = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    return arraySort(left) + mid  + arraySort(right)

if __name__ == '__main__':
    array = [5,2,9,1,6]
    result = arraySort(array)
    print("Result is:", result)
