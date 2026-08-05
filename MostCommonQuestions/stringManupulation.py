"""
File: stringManupulation.py
Author: Somnath
Date: 20/07/26
Description: Python program to gives Output: a2b2c3d2 for the Input String Str = “aabbcccdd”
"""


def stringManupulation(input_string):
    dic = {}
    for i in input_string:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    output = []
    for key, value in dic.items():
        output.append(f"{key}{value}")
    return ''.join(output)

if __name__ == '__main__':
    input_string = 'aabbcccdd'
    result = stringManupulation(input_string)
    print("Result is:", result)
