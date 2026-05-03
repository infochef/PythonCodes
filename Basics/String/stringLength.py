"""
File: stringLength.py
Author: Somnath
Date: 03-05-2026
Description: Python program to calculate the length of a string.
"""


def main():
    string_length = 'w3resource.com'

    # Using for loop
    char = 0
    for i in string_length:
        char += 1

    print("Total number of characters present in the giver string using for loop is:", char)

    # Using length function

    length_func = len(string_length)

    print("Total number of characters present in the giver string using length function is:", length_func)

if __name__ == '__main__':
    main()
