"""
File: shuffle.py
Author: Somnath
Date: 17/07/26
Description: 
"""

from random import shuffle

def shuffle_color(color):
    shuffle(color)
    return color

if __name__ == '__main__':
    color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    result = shuffle_color(color)
    print("Result is:", result)
