"""
File: splitTextSentence.py
Author: Somnath
Date: 23/05/26
Description: Python NLTK program to split the text sentence/paragraph into a list of words.
"""
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

def splitTextSentence(text):
    print("\nOriginal Text")
    print(text)

    token_text = sent_tokenize(text)
    print("\nSentence-tokenized copy in a list:")
    print(token_text)
    print("\nRead the list:")
    for s in token_text:
        print(s)
    return token_text


if __name__ == '__main__':
    text = '''
    Joe waited for the train. The train was late. 
    Mary and Samantha took the bus. 
    I looked for Mary and Samantha at the bus station.
    '''
    result = splitTextSentence(text)
    print("Splitted text or sentence after using NLTK is:", result)