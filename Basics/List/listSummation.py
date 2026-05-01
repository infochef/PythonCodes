"""
File: listSummation.py
Author: Somnath
Date: 01-05-2026
Description: Python program to sum all the items in a list.
"""


def main():
    colors = input("Enter colors separated by space: ").split()
    sum = 0
    for color in colors:
        sum += int(color)
    print("Sum of colors: ", sum, "")


if __name__ == '__main__':
    main()
