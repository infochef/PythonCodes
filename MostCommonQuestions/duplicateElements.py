"""
File: duplicateElements.py
Author: Somnath
Date: 20/07/26
Description: Python program to find duplicate characters in a string
"""


def duplicateElements(string):
    dic = {}
    dic2 = {}
    arr = string.split()

    for i in arr:
        for j in i:
            if j not in dic:
                dic[j] = 1
            else:
                dic[j] += 1

    for k, l in dic.items():
        if l > 1:
            dic2[k] = l
    return dic2

if __name__ == '__main__':
    string = "Learn Java Programming"
    result = duplicateElements(string)
    print("Result is:", result)
