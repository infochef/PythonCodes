"""
File: checkRemoveContent.py
Author: Somnath
Date: 01-05-2026
Description: Python program to remove an item from a set if it is present in the set.
"""


def main():
    num_set = set([0, 1, 2, 3, 4, 5])
    print("Removing an item from the num_set using discard method:", num_set.discard(6))
    print("Final set:", num_set)
    print("Removing an item from the num_set using discard method:", num_set.discard(3))
    print("Final set:", num_set)

    num_set2 = set([6,7,8,9,10])
    if 8 in num_set2:
        num_set2.discard(90)
    else:
        print("num_set does not contain the said element for removal")
    print("Final set after removal of element using for loop:", num_set2)


if __name__ == '__main__':
    main()
