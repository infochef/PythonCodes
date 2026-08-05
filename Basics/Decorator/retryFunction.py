"""
File: retryFunction.py
Author: Somnath
Date: 18/07/26
Description: Python program that implements a decorator to retry a function multiple times in case of failure.
"""

import time

def retryFunction(max_attempts):
    def retry(func):
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)

                except Exception as e:
                    print(f"Attempt {attempt} failed: {e}")
                    if attempt == max_attempts:
                        print("Maximum retries reached.")
                        raise
                    print("Retrying...")
                    time.sleep(1)

        return wrapper
    return retry

@retryFunction(3)
def divide(a, b):
    return a/b


if __name__ == '__main__':
    result = divide(10, 10)
    print("Result is:", result)
