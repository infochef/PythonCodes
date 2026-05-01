"""
File: removeContent.py
Author: Somnath
Date: 01-05-2026
Description: Python program to remove item(s) from a given set.
"""


def main():
    num_set = set([0, 1, 3, 4, 5])
    print("Remove an item from num_set using pop method:", num_set.pop())
    print("After removing an item from set final set is:", num_set)
    print("Remove an item from num_set using remove method:", num_set.remove(1))
    print("After removing an item from set final set is:", num_set)


if __name__ == '__main__':
    main()
