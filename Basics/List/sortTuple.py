"""
File: sortTuple.py
Author: Somnath
Date: 01-05-2026
Description: Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
"""


def main():
    list1= [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

    def get_last_element(tup):
        return tup[-1]


    sorted_list = sorted(list1, key=get_last_element)
    print(sorted_list)

if __name__ == '__main__':
    main()
