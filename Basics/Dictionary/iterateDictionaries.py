"""
File: iterateDictionaries.py
Author: Somnath
Date: 02-05-2026
Description: Python program to iterate over dictionaries using for loops.
"""


def main():
    d = {'x': 10, 'y': 20, 'z': 30}

    for key, value in d.items():
        print(key, "-->", value)


if __name__ == '__main__':
    main()
