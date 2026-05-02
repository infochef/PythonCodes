"""
File: summation.py
Author: Somnath
Date: 02-05-2026
Description: Python program to sum all the items in a dictionary.
"""


def main():
    my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
    result = 0
    for key, values in my_dict.items():
        result += values

    print(result)


if __name__ == '__main__':
    main()
