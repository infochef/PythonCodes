"""
File: stringNumberManupulation.py
Author: Somnath
Date: 20/07/26
Description: Python program to gives two Output: “Subburaj”, “123” for the Input String Str = “Subbu123raj”
"""


def stringNumberManupulation(string):
    num = []
    char = []

    for i in string:
        if i.isnumeric():
            num.append(i)
        else:
            char.append(i)
    number = ''.join(num)
    character = ''.join(char)

    return number, character
if __name__ == '__main__':
    string = 'Subbu123raj'
    result = stringNumberManupulation(string)
    print("Result is:", result)
