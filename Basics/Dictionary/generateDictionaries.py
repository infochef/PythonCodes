"""
File: generateDictionaries.py
Author: Somnath
Date: 02-05-2026
Description: Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
"""


def main():
    n = int(input("Enter the length of the dictionary:"))
    result = {}

    for i in range(1, n):
        result[i] = i ** 2

    print(result)


if __name__ == '__main__':
    main()
