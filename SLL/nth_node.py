# Given the head of a linked list, remove the nth node from the end of the list and return its head.

# EX 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]

# EX 2:
# Input: head = [1], n = 1
# Output: []

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        runner = head
        while runner != None:
            print(runner.val)
            runner = runner.next