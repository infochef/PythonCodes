"""
File: differentDataTypes.py
Author: Somnath
Date: 02-05-2026
Description: Python program to create a tuple with different data types.
"""


def main():
    t = (1, "string", 1.35, True)
    print(type(t))
    s = tuple([1, "string", 1.35, True])
    print(type(s))

if __name__ == '__main__':
    main()
