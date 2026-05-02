"""
File: insertionSort.py
Author: Somnath
Date: 02/05/26
Description: Python program to perform insertion sort in an array
"""


def main(arr):
    n = len(arr)

    for current in range(1, n):
        currentCard = arr[current]
        correctPosition = current - 1  # It will go from i-1 to 0
        while correctPosition >= 0:
            if (arr[correctPosition] < currentCard):
                break
            else:
                arr[correctPosition + 1] = arr[correctPosition]
                correctPosition -= 1
            arr[correctPosition + 1] = currentCard

    return arr


if __name__ == '__main__':
    unsorted_list = [12, 25, 11, 34, 90, 22]
    sorted_list = main(unsorted_list)
    print("After performing insertion sort final array is:", sorted_list)
