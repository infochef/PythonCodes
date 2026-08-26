"""
File: valid_anagram.py
Author: Somnath
Date: 25/08/26
Description: 242. Valid Anagram
"""

def valid_anagram(s, t):
    char = {}
    if len(s) != len(t):
        return False

    for ch in s:
        char[ch] = char.get(ch, 0) + 1
    for ch in t:
        if ch not in char:
            return False
        elif char[ch] == 0:
            return False
        else:
            char[ch] -= 1
    return True



if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    result = valid_anagram(s, t)
    print("Result is:", result)
