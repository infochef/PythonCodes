"""
File: numberManupulation.py
Author: Somnath
Date: 20/07/26
Description: Python program to gives Output: “32412120000” for the Input String Str = “32400121200”
"""


def numberManupulation(input_string):
    zero = []
    num = []
    for i in input_string:
        if i == '0':
            zero.append(i)
        else:
            num.append(i)

    final_result = ''.join(num) + ''.join(zero)

    return final_result

if __name__ == '__main__':
    input_string = '32400121200'
    result = numberManupulation(input_string)
    print("Result is:", result)
