"""
File: addKey.py
Author: Somnath
Date: 02-05-2026
Description:  Python script to add a key to a dictionary.
"""


def main():
    d = {0: 10, 1: 20}
    d.update({2:3})

    print("Final dictionary after adding values:", d)


if __name__ == '__main__':
    main()
