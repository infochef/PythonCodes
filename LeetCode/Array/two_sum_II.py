"""
File: two_sum_II.py
Author: Somnath
Date: 18/08/26
Description: 167. Two Sum II - Input Array Is Sorted
"""


def two_sum_II(numbers, target):
    l, r = 0, len(numbers) - 1

    while l < r:
        currSum = numbers[l] + numbers[r]
        if currSum > target:
            r -= 1
        elif currSum < target:
            l -= 1
        else:
            return [l+1, r+1]
    return []

if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    result = two_sum_II(numbers, target)
    print("Result is:", result)
