"""
File: cloning.py
Author: Somnath
Date: 02-05-2026
Description: Python program to create the colon of a tuple.
"""
import copy
from copy import deepcopy

def main():
    tuplex = ("HELLO", 5, [], True)
    t1 = tuplex
    print(t1)

    t2 = copy.deepcopy(tuplex)
    print(t2)

if __name__ == '__main__':
    main()
