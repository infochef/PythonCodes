"""
File: linearSearch.py
Author: Somnath
Date: 01/05/26
Description: Python program to perform linear search in an array
"""

def main():
    linear_search = [3, 7, 2, 5]
    target = 2
    size = len(linear_search)

    for index in range(0, size):
        if linear_search[index] == target:
            return index
    return -1


if __name__ == '__main__':
    result = main()
    print(result)