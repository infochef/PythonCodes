"""
File: concatenate.py
Author: Somnath
Date: 02-05-2026
Description: Python script to concatenate the following dictionaries to create a new one.
"""
from collections import Counter


def main():
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}

    add_operator = dic1 | dic2 | dic3
    print("Concatenated 3 dictionaries using | operator:", add_operator)

    unpacking_operator = {**dic1, **dic2, **dic3}
    print("Concatenated 3 dictionaries using unpacking operator:", unpacking_operator)

    counter_function = dict(Counter(dic1) + Counter(dic2) + Counter (dic3))
    print("Concatenated 3 dictionaries using counter function:", counter_function)

if __name__ == '__main__':
    main()
