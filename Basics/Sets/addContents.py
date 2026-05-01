"""
File: addContents.py
Author: Somnath
Date: 01-05-2026
Description: Python program to add member(s) to a set.
"""


def main():
    create_set = set()
    print("Add 1 content to an empty_set")
    create_set.add(1)
    print("printing set after adding 1 content:", create_set)
    print("Add multiple items to the empty set")
    create_set.update([2,3])
    print("Final set:", create_set)


if __name__ == '__main__':
    main()
