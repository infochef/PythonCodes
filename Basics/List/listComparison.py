"""
File: listComparison.py
Author: Somnath
Date: 17/07/26
Description: 
"""


def listComparison(l1, l2):
    for i in l1:
        if i in l2:
            return True
    return False

    # return not set(l1).isdisjoint(l2)


if __name__ == '__main__':
    list1 = [1, 2, 3]
    list2 = [9, 4, 5]
    result = listComparison(list1, list2)
    print("Result is :", result)

