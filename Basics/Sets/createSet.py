"""
File: createSet.py
Author: Somnath
Date: 01-05-2026
Description: Python program to create a set.
"""


def main():
    my_set = {1,2,3}
    print(type(my_set))

    empty_set = set()
    print(type(empty_set))

    set_creation = set([1,2,3,4])
    print(type(set_creation))

    li = [1,2,2,3,4,2,3,4,5]
    print(set(li))

if __name__ == '__main__':
    main()
