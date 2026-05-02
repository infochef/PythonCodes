"""
File: conditionalPrinting.py
Author: Somnath
Date: 02-05-2026
Description: Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
"""


def main():
    sample_dic = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
    new_dict = {}

    for key, value in sample_dic.items():
        if key in range(1,16):
            new_dict[key] = key ** 2

    print("The new dictionary after creation is:", new_dict)

if __name__ == '__main__':
    main()
