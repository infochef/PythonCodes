"""
File: stringCount.py
Author: Somnath
Date: 01-05-2026
Description: Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.
"""


def main():
    list1 = ['abc', 'xyz', 'aba', '1221']
    s = 0

    for i in list1:
        if len(i) > 2 and i[0] == i[-1]:
            s += 1

    return s


if __name__ == '__main__':
    result = main()
    print("Number of strings are:", result)