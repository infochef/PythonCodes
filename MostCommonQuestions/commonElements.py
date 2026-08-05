"""
File: commonElements.py
Author: Somnath
Date: 20/07/26
Description: Find common elements between two arrays
"""


def commonElements(array1, array2):
    common_element = []
    for i in array1:
        for j in array2:
            if i == j:
                common_element.append(j)
    return common_element

if __name__ == '__main__':
    array1 = {1, 2, 3, 4, 5}
    array2 = {4, 5, 6, 7, 8}
    result = commonElements(array1, array2)
    print("Result is:", result)
