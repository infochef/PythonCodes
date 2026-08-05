"""
File: sortDistinctWords.py
Author: Somnath
Date: 18/07/26
Description: Python program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically).
"""


def sortDistinctWords(Sample_Words):
    word_split = Sample_Words.split(",")
    print(word_split)
    distint_word = []

    for i in word_split:
        word = i.strip()
        if word not in distint_word:
            distint_word.append(word)

    distint_word.sort()
    return ",".join(distint_word)

if __name__ == '__main__':
    Sample_Words = "red, white, black, red, green, black"
    result = sortDistinctWords(Sample_Words)
    print("Result is:", result)
