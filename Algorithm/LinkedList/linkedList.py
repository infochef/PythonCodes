"""
File: linkedList.py
Author: Somnath
Date: 06/05/26
Description: Python program to create and perform operations on linked list
"""

class Node:
    def __init__(self, data):

        # Store value inside node
        self.data = data

        # Initially node is not connected to anything
        self.next = None


class LinkedList:
    def __init__(self):

        # Initially linked list is empty
        self.head = None

    def insert(self, data):

        # Create new node
        new_node = Node(data)

        # CONDITION:
        # Check if linked list is empty
        if self.head is None:

            # Make new node the first node
            self.head = new_node
            return

        # Start from first node
        temp = self.head

        # CONDITION:
        # Keep moving while next node exists
        while temp.next is not None:

            # Move to next node
            temp = temp.next

        # Connect last node to new node
        temp.next = new_node

    def display(self):

        # Start from head node
        temp = self.head

        # CONDITION:
        # Keep printing while node exists
        while temp is not None:

            print(temp.data, end=" -> ")

            # Move to next node
            temp = temp.next

        print("None")


# ---------------- MAIN PROGRAM ----------------

# Create linked list object
ll = LinkedList()

# Insert values
ll.insert(10)
ll.insert(20)
ll.insert(30)

# Display linked list
ll.display()