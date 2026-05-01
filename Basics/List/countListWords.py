"""
File: countListWords.py
Author: Somnath
Date: 01-05-2026
Description:  Python program to find the list of words that are longer than n from a given list of words.
"""


def main():
    li = ['quick', 'brown', 'jumps', 'over', 'lazy']
    n = 4
    new_list = []

    for i in li:
        if len(i) > n:
            new_list.append(i)

    print("New list is:", new_list)


if __name__ == '__main__':
    main()
