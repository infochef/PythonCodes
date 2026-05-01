"""
File: minNumber.py
Author: Somnath
Date: 01-05-2026
Description: Python program to get the smallest number from a list.
"""


def main():
    num = list(map(int,input("Enter the contents of list:").split()))
    smallest_num = num[0]

    for i in num:
        if i < smallest_num:
            smallest_num = i

    min_num = min(num)
    print("Smallest number in the list is:", min_num)
    return smallest_num

if __name__ == '__main__':
    result = main()
    print("Smallest integer number in the list is:", result)