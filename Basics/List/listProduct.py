"""
File: listProduct.py
Author: Somnath
Date: 01-05-2026
Description: Python program to multiply all the items in a list.
"""


def main():
    empty_list = input("Enter the list contents: ").split()
    pro = 1
    for i in empty_list:
        pro *= int(i)
    print("Product of the contents inside the list is:", pro)

if __name__ == '__main__':
    main()
