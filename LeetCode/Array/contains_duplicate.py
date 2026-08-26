"""
File: contains_duplicate.py
Author: Somnath
Date: 17/08/26
Description: 217. Contains Duplicate
"""


def contains_duplicate(arr):
    s = set()

    for i in arr:
        if i not in s:
            s.add(i)
        else:
            return True
    return False

if __name__ == '__main__':
    arr = [1, 2, 3, 1]
    result = contains_duplicate(arr)
    print("Result is:", result)
