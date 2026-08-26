"""
File: container_with_most_water.py
Author: Somnath
Date: 18/08/26
Description: 11. Container With Most Water
"""


def container_with_most_water(height):
    res = 0
    l, r = 0, len(height) - 1
    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res

if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    result = container_with_most_water(height)
    print("Result is:", result)
