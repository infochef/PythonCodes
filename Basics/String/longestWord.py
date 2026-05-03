"""
File: longestWord.py
Author: Somnath
Date: 03-05-2026
Description: Python function that takes a list of words and return the longest word and the length of the longest one.
"""

def main():
    sample_string = "PHP,Exercises,Backend"
    sample = str(sample_string).split(',')
    result = []
    for i in sample:
        result.append((i, len(i)))
    sorted_result = sorted(result, key=lambda x:x[1])
    print("Longest word:", sorted_result[-1][0])
    print("Length of longest word:", sorted_result[-1][1])


if __name__ == '__main__':
    main()
