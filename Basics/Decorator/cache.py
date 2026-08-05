"""
File: cache.py
Author: Somnath
Date: 18/07/26
Description: Write a Python program that implements a decorator to cache the result of a function.
"""


def cache_result(func):

    cache = {}

    def wrapper(*args, **kwargs):

        # Create a unique key from the arguments
        key = (args, tuple(kwargs.items()))

        if key in cache:
            print("Returning result from cache...")
            return cache[key]

        print("Calculating result...")

        result = func(*args, **kwargs)

        cache[key] = result

        return result

    return wrapper


@cache_result
def square(n):
    print("Inside square()")
    return n * n


print(square(10))
print(square(10))
print(square(20))
print(square(20))
