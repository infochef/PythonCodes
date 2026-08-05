"""
File: primeNumber.py
Author: Somnath
Date: 19/07/26
Description: Python programm to check is a number is prime number or not
"""


def primeNumber():
    num = int(input("Enter the number to verify: "))

    if num <= 1:
        return f"{num} is not a prime number"

    for i in range(2, num):
        if num % i == 0:
            return f"{num} is not a prime number"
    return f"{num} is a prime number"

if __name__ == '__main__':
    result = primeNumber()
    print("Result is:", result)
