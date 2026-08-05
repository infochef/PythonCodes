"""
File: stringIdentification.py
Author: Somnath
Date: 20/07/26
Description: Python program to gives two Output: “abcde”, “ABCDE” for the Input String Str = “aBACbcEDed”
"""


def stringIdentification(string):
    lower_case = []
    upper_case = []

    for i in string:
        if i.islower():
            lower_case.append(i)
        elif i.isupper():
            upper_case.append(i)

    return ''.join(lower_case), ''.join(sorted(upper_case))


if __name__ == '__main__':
    string = 'aBACbcEDed'
    result = stringIdentification(string)
    print("Result is:", result)
