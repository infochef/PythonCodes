"""
File: search.py
Author: Somnath
Date: 02-05-2026
Description:  Check Whether an Element Exists Within a Tuple
"""


def main():
    tuplex = 2, 4, 5, 6, 2, 3, 4, 4, 7
    print(tuplex.index(5))
    print(2 in tuplex)

if __name__ == '__main__':
    main()
