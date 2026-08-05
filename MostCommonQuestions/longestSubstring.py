"""
File: longestSubstring.py
Author: Somnath
Date: 20/07/26
Description: Python program to find the longest without repeating characters
"""


def longestSubstring(s):
    charSet = set()
    left = 0
    result = 0

    for right in range(len(s)):
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
        result = max(result, right - left + 1)
    return result

if __name__ == '__main__':
    s = "abcabcbb"
    result = longestSubstring(s)
    print("Result is:", result)
