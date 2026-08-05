"""
File: mapList.py
Author: Somnath
Date: 17/07/26
Description: 
"""


def mapList(k, v):
    result = dict(zip(k, v))
    return result

    # result = {}
    # for i in range(len(k)):
    #     result[k[i]] = v[i]
    # return result

if __name__ == '__main__':
    keys = ['red', 'green', 'blue']
    values = ['#FF0000', '#008000', '#0000FF']
    result = mapList(keys, values)
    print("Result is:", result)
