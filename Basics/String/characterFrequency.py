"""
File: characterFrequency.py
Author: Somnath
Date: 03-05-2026
Description: Python program to count the number of characters (character frequency) in a string.
"""


def main():
    string = 'google.com'
    d = {}

    for i in string:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1

    print("Newly created dictionary is:", d)

    #using get
    s = {}
    for ch in string:
        s[ch] = s.get(ch, 0) + 1

    print(s)
if __name__ == '__main__':
    main()
