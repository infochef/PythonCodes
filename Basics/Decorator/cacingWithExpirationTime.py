"""
File: cacingWithExpirationTime.py
Author: Somnath
Date: 18/07/26
Description: 
"""


import time

def cache_with_expiry(expiry_time):

    def decorator(func):

        cache = {}

        def wrapper(*args, **kwargs):
            key = (args, tuple(kwargs.items()))
            current_time = time.time()
            if key in cache:
                result, timestamp = cache[key]

                # Check whether cache is still valid
                if current_time - timestamp < expiry_time:
                    print("Returning cached result...")
                    return result

                print("Cache expired.")

            print("Calculating new result...")

            result = func(*args, **kwargs)
            cache[key] = (result, current_time)
            return result

        return wrapper

    return decorator


@cache_with_expiry(5)      # Cache expires after 5 seconds
def square(n):
    print("Inside square()")
    return n * n


print(square(10))
print(square(10))
time.sleep(6)
print(square(10))