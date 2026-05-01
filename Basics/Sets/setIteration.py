"""
File: setIteration.py
Author: Somnath
Date: 01-05-2026
Description: Python program to iterate over sets.
"""


def main():
    num_set = set([0, 1, 2, 3, 4, 5])
    for i in num_set:
        print("num_set:", i)

    char_set = set("w3resource")
    for i in char_set:
        print("char_set:", i)

if __name__ == '__main__':
    main()
