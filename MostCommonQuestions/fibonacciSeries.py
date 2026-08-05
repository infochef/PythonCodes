"""
File: fibonacciSeries.py
Author: Somnath
Date: 19/07/26
Description: Python programm to find Fibonacci series upto a given number range
"""


def fibonacciSeries(ran):
    a = 0
    b = 1

    for i in range(1, ran+1):
        print(a)
        c = a + b # 1, 2, 3
        a = b #1, 1
        b = c #1, 2

if __name__ == '__main__':
    limit = 5
    result = fibonacciSeries(limit)
    print("Result is:", result)
