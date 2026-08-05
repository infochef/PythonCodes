"""
File: pythonToJson.py
Author: Somnath
Date: 18/07/26
Description: Convert Python object to JSON data
"""
import json

def pythonToJson(python_obj):
    print(type(python_obj))
    py_conv = json.dumps(python_obj, indent=4)
    py_conv_sep = json.dumps(python_obj, indent=2, separators= (",", "="))
    py_conv_order = json.dumps(python_obj, indent=2, separators= (",", "="), sort_keys=True)
    print(type(py_conv))
    print(repr(py_conv))
    return py_conv, py_conv_sep, py_conv_order

if __name__ == '__main__':
    python_obj = {
        "name": "David",
        "class": "I",
        "age": 6
    }
    result = pythonToJson(python_obj)
    print("Result is:", result)
