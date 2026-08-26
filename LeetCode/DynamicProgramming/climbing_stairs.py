"""
File: climbing_stairs.py
Author: Somnath
Date: 19/08/26
Description: 
"""


def climbing_stairs(n):
    one, two = 1 , 1
    for i in range(n-1):
        temp = one
        one = one + two
        two = temp
    return one

if __name__ == '__main__':
    n = 5
    result = climbing_stairs(n)
    print("Result is:", result)
