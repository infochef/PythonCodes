"""
File: jsonConverstion.py
Author: Somnath
Date: 18/07/26
Description: Write a Python program to convert JSON data to Python object
"""

import json

def jsonConverstion(obj):
    result = json.loads(obj)
    print(type(result))
    return result


if __name__ == '__main__':
    json_obj = '{ "Name":"David", "Class":"I", "Age":6 }'
    result = jsonConverstion(json_obj)
    print("Result is:", result)
