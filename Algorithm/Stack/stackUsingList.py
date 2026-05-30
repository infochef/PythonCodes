"""
File: stackUsingList.py
Author: Somnath
Date: 25/05/26
Description: Perform stack operations using list
"""

class stackUsingList():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)
        return print(f"pushed {data} into stack")

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def top(self):
        if(self.is_empty()):
            print("stack is empty")
            return None
        return self.stack[len(self.stack) - 1]

    def pop(self):
        if (self.is_empty()):
            print("stack is empty")
            return None
        return self.stack.pop()

myStack = stackUsingList()

print(myStack.is_empty())

myStack.push(10)
myStack.push(20)
myStack.push(30)
myStack.push(40)

print(myStack.is_empty())

print(myStack.pop())
print(myStack.pop())

print(myStack.size())

print(myStack.top())

print(dir(myStack))