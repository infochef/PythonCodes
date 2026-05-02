"""
File: stringConversion.py
Author: Somnath
Date: 02-05-2026
Description: Python program to convert a tuple to a string.
"""


def main():
    t = (1, 2, 3)
    string = str(t)
    print(string)
    string_join = ''.join(map(str,t))
    print(string_join)

if __name__ == '__main__':
    main()
