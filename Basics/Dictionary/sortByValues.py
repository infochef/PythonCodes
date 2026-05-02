"""
File: sortByValues.py
Author: Somnath
Date: 02-05-2026
Description: Python program to sort (ascending and descending) a dictionary by value.
"""


def main():
    d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

    items = list(d.items())  # [(key, value), ...]

    # Bubble sort based on value
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j][1] > items[j + 1][1]:  # compare values
                items[j], items[j + 1] = items[j + 1], items[j]

    for k, v in items:
        print("k:", k, "v:", v)

# ===============================================

    d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

    sorted_items = sorted(d.items(), key=lambda x: x[1])

    for k, v in sorted_items:
        print("k:", k, "v:", v)


if __name__ == '__main__':
    main()