"""
File: largestNum.py
Author: Somnath
Date: 01-05-2026
Description: Python program to get the largest number from a list.
"""


def main():
    num = list(map(int, input("Enter the contents of list: ").split()))
    biggest_num = int(num[0])

    for i in num:
        if int(i) > biggest_num:
            biggest_num = int(i)

    ma_result = max(num)
    print("Max result is:", ma_result)
    return biggest_num


if __name__ == '__main__':
    result = main()
    print("Biggest number is:", result)