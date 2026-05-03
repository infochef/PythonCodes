"""
File: stringAddition.py
Author: Somnath
Date: 03-05-2026
Description: Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
"""


def main():
    sample_string = input("Enter the samplestring for manupulation:")

    if len(sample_string) < 3:
        return sample_string
    elif sample_string[len(sample_string)-3: len(sample_string)] == 'ing':
        result = sample_string + 'ly'
        return result
    else:
        result2 = sample_string + 'ing'
        return result2

if __name__ == '__main__':
    output = main()
    print(output)