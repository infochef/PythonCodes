"""
File: changeSentence.py
Author: Somnath
Date: 03-05-2026
Description: Python program to find the first appearance of the substrings 'not' and 'poor' in a given string. If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
"""


def main():
    string = input("Enter the sample string:")

    if 'not' in string and 'poor' in string:
        if string.index('not') < string.index('poor'):
            result = string.replace(string[string.index('not'):string.index('poor')+4], 'good')
            print(result)


if __name__ == '__main__':
    main()
