"""
File: createNewFile.py
Author: Somnath
Date: 18/07/26
Description: 
"""

import json

def createNewFile():

    with open('new_state.json') as f:
        data = json.load(f)
        print(data)

    with open('new_state2.json', 'w') as f:
        json.dump(data, f)

if __name__ == '__main__':
    result = createNewFile()
    print("Result is:", result)
