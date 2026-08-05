"""
File: reverseEachWord.py
Author: Somnath
Date: 20/07/26
Description: Python program to reverse each word of a given string
"""


def reverseEachWord(input_string):
    arr = input_string.split()
    k = []

    for i in arr:
        arr_lst = [x for x in i]

        start = 0
        end = len(arr_lst) - 1

        while start < end:
            arr_lst[start], arr_lst[end] = arr_lst[end], arr_lst[start]
            start += 1
            end -= 1

        k.append(''.join(arr_lst))

    return ' '.join(k)


if __name__ == '__main__':
    input_string = "Java is good programming langauges"
    result = reverseEachWord(input_string)
    print(result)