"""
File: duplicateList.py
Author: Somnath
Date: 01-05-2026
Description: Python program to remove duplicates from a list.
"""


def main():
    list1 = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
    li = []

    for i in list1:
        if i not in li:
            li.append(i)

    return li


if __name__ == '__main__':
    result = main()
    print("After removing duplicates new list is:", result, "")
