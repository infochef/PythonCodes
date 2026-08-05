"""
File: memoryUsage.py
Author: Somnath
Date: 18/07/26
Description: Python program that implements a decorator to measure the memory usage of a function.
"""


import tracemalloc

def measure_memory(func):

    def wrapper(*args, **kwargs):

        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Current Memory Usage: {current / 1024:.2f} KB")
        print(f"Peak Memory Usage: {peak / 1024:.2f} KB")

        return result

    return wrapper


@measure_memory
def create_list(n):
    data = [i for i in range(n)]
    return data

numbers = create_list(100000)

print(len(numbers))