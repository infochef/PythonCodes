"""
File: copyList.py
Author: Somnath
Date: 01-05-2026
Description: Python program to clone or copy a list.
"""


def main():
    original = [1, 2, 3]
    new_list = original.copy()
    li = []
    print(new_list)

    for i in original:
        li.append(i)

    print("li: ", li)

if __name__ == '__main__':
    main()
