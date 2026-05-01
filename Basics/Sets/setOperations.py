"""
File: setOperations.py
Author: Somnath
Date: 01-05-2026
Description: Python program to create an intersection, union, difference & symmetric of sets.
"""


def main():
    setx = set(["green", "blue"])
    sety = set(["blue", "yellow"])

    print("Create intersection of set using operator:", setx & sety)
    print("Create intersection of set using method:", setx.intersection(sety))
    print("Create union of set using operator:", setx | sety)
    print("Create union of set using method:", setx.union(sety))
    print("Create difference of set using operator:", setx-sety)
    print("Create difference of set using method:", setx.difference(sety))
    print("Create symmetric of set using operator:", setx ^ sety)
    print("Create symmetric of set using method:", setx.symmetric_difference(sety))

if __name__ == '__main__':
    main()
