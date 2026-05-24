"""
File: add_two_numbers.py
Author: Somnath
Date: 23/05/26
Description: 2. Add Two Numbers
"""

def build_linked_list(arr):
    dummy = ListNode()
    cur = dummy

    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next

    return dummy.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        cur = dummy

        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry #15
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


l1 = build_linked_list([2,4,3])
l2 = build_linked_list([5,6,4])

sol = Solution()
result = sol.addTwoNumbers(l1, l2)

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

print_list(result)
print(result)