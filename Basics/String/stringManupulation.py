"""
File: stringManupulation.py
Author: Somnath
Date: 03-05-2026
Description: Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
"""


def main():
    sample_string = input("Enter the string for manupulation:")
    s = sample_string[0]
    result = s

    for i in range(1, len(sample_string)):
        if sample_string[i] == s:
           result += '$'
        else:
            result += sample_string[i]

    print(result)


if __name__ == '__main__':
    main()
