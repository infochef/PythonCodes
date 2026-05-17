"""
File: matrixSearch.py
Author: Somnath
Date: 14/05/26
Description: Search a 2D Matrix
"""


def matrixSearch(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    start, end = 0, rows * cols - 1

    while start <= end:
        mid = (start + end) // 2
        row = mid // cols
        col = mid % cols

        if matrix[row][col] == target:
            return True

        elif matrix[row][col] < target:
            start = mid + 1

        elif matrix[row][col] > target:
            end = end - 1
    return False


if __name__ == '__main__':
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 5
    result = matrixSearch(matrix, target)
    print("Search a 2D Matrix:", result)

