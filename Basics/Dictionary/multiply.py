"""
File: multiply.py
Author: Somnath
Date: 02-05-2026
Description: Python program to multiply all the items in a dictionary.
"""


def main():
    my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
    pro = 1

    for value in my_dict.values():
        pro *= value

    print(pro)

if __name__ == '__main__':
    main()
