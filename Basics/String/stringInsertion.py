"""
File: stringInsertion.py
Author: Somnath
Date: 18/07/26
Description: Python function to insert a string in the middle of a string.
"""


def stringInsertion(input_str):
    f_index = input_str.find('WestBengal')
    return input_str[:f_index] + 'state:' + input_str[f_index:]

if __name__ == '__main__':
    input_str = 'City:Kolkata-WestBengal'
    result = stringInsertion(input_str)
    print("Result is:", result)
