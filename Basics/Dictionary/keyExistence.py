"""
File: keyExistence.py
Author: Somnath
Date: 02-05-2026
Description: Python script to check whether a given key already exists in a dictionary.
"""


def main():
    n = input("Enter the value to be searched:")
    d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

    for key, value in d.items():
        if key == int(n):
            print("The key that you were searching in the dictionary is present:", key, ":", value)

if __name__ == '__main__':
    main()
