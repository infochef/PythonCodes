"""
File: validateArguments.py
Author: Somnath
Date: 18/07/26
Description: Write a Python program that implements a decorator to validate function arguments based on a given condition.
"""


def validateArguments(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError(f"{arg} is not an integer")

        for kwarg in kwargs:
            if not isinstance(kwarg, int):
                raise TypeError(f"f{kwarg} is now an integer")

        return func(*args, **kwargs)
    return wrapper

@validateArguments
def add(a, b):
    return a + b

if __name__ == '__main__':
    result = add(10, 12)
    print("Result is:", result)
