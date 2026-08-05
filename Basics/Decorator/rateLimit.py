"""
File: rateLimit.py
Author: Somnath
Date: 18/07/26
Description: Python program that implements a decorator to enforce rate limits on a function.
"""


import time

def rate_limit(max_calls, period):

    def decorator(func):

        call_times = []

        def wrapper(*args, **kwargs):

            current_time = time.time()

            # Remove calls older than the time window
            while call_times and current_time - call_times[0] > period:
                call_times.pop(0)

            if len(call_times) >= max_calls:
                raise Exception("Rate limit exceeded. Please try again later.")

            call_times.append(current_time)

            return func(*args, **kwargs)

        return wrapper

    return decorator


@rate_limit(3, 10)   # Maximum 3 calls every 10 seconds
def greet(name):
    print(f"Hello {name}")


greet("Alice")
greet("Bob")
greet("Charlie")
greet("David")      # Raises Exception
