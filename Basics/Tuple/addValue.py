"""
File: addValue.py
Author: Somnath
Date: 02-05-2026
Description: Python program to add an item to a tuple.
"""


def main():
    t = (1, 2, 3)

    lst = list(t)
    lst.append(4)
    tup = tuple(lst)

    print(tup)

    t1 = t + (4,)
    print(t1)
if __name__ == '__main__':
    main()
