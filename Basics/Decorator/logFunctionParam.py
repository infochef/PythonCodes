"""
File: logFunctionParam.py
Author: Somnath
Date: 18/07/26
Description: Python program to create a decorator that logs the arguments and return value of a function
"""


def logFunctionParam(func):

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")

        result = func(*args, **kwargs)

        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


@logFunctionParam
def add(a, b):
    return a + b


if __name__ == "__main__":
    result = add(10, 20)
    print("Result is:", result)

