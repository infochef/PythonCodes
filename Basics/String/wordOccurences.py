"""
File: wordOccurences.py
Author: Somnath
Date: 18/07/26
Description: Python program to count the occurrences of each word in a given sentence.
"""


def wordOccurences(word_list):
    word_split = word_list.split()
    count = 1
    word_dic = {}

    for word in word_split:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1

    return word_dic

if __name__ == '__main__':
    word_count = 'the quick brown brown fox jumps over the lazy dog.'
    result = wordOccurences(word_count)
    print("Result is:", result)
