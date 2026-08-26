"""
File: longest_increasing_subsequence.py
Author: Somnath
Date: 24/08/26
Description: 300. Longest Increasing Subsequence
"""


def longest_increasing_subsequence(nums):
    lis = [1] * len(nums)
    for i in range(len(nums) -1, -1, -1):
       for j in range(i+1, len(nums)):
           if nums[i] < nums[j]:
              lis[i] = max(lis[i], 1 + lis[j])
    return max(lis)

if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    result = longest_increasing_subsequence(nums)
    print("Result is:", result)
