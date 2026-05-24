"""
File: longest_substring.py
Author: Somnath
Date: 23/05/26
Description: 
"""


def longest_substring(s):
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        res = max(res, r - l + 1)
    return res

if __name__ == '__main__':
    s = "abcabcbb"
    result = longest_substring(s)
    print("Longest substring from the given substring is:", result)
