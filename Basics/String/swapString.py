"""
File: swapString.py
Author: Somnath
Date: 03-05-2026
Description: Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
"""


def main():
    sample_string = input("Enter the string for manupulation:").split(',')
    first = sample_string[0]
    second = sample_string[1]
    result1 = second[0:2] + first[len(first)-1:]
    result2 = first[0:2] + second[len(second) - 1:]
    print(result1,',',result2)

if __name__ == '__main__':
    main()
