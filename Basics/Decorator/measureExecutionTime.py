"""
File: measureExecutionTime.py
Author: Somnath
Date: 18/07/26
Description: Python program to create a decorator function to measure the execution time of a function.
"""
import time

def measureExecutionTime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"Calling {func.__name__} with args{args}, {kwargs}")
        result = func(*args, **kwargs)
        end = time.time()
        execution_time = end - start
        print(f"Function {func.__name__} took {execution_time:.6f} seconds to execute")
        return result
    return wrapper

@measureExecutionTime
def pro(a):
    p = 1
    for i in range(1, a+1):
        p *= i
    return p

if __name__ == '__main__':
    result = pro(500)
    print("Result is:", result)
