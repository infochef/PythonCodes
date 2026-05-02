"""
File: mergeDict.py
Author: Somnath
Date: 02-05-2026
Description: Python script to merge two Python dictionaries.
"""


def main():
    d1 = {'a': 100, 'b': 200}
    d2 = {'x': 300, 'y': 200}

    d = d1.copy()
    d.update(d2)
    print(d)

if __name__ == '__main__':
    main()
