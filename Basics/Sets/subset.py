"""
File: subset.py
Author: Somnath
Date: 01-05-2026
Description: Python program to check if a set is a subset of another set.
"""


def main():
    setx = set(["apple", "mango"])
    sety = set(["mango"])

    print("Check if sety is subset of setx using operator:", sety <= setx)
    print("Check if sety is subset of setx using operator:", sety.issubset(setx))


if __name__ == '__main__':
    main()
