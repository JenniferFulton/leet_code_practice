from dataclasses import dataclass


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None 

class sll():
    def __init__(self, nodeValue):
        self.head = Node(nodeValue)
        
# 1. FRONT
# Write a method to return the value (not the node) at the head of the list. If the list is empty, return null.
    def display_head(self):
        print(self.head.data)
        return self
        
# 2. REMOVE FRONT
# Write a method to remove the head node and return the new list head node. If the list is empty, return null.
    def remove_head(self):
        if self.head == None:
            print (None)
        else:
            removed = self.head
            self.head = removed.next
            print(self.head)
        return self

# 3. ADD FRONT
# Write a method that accepts a value and create a new node, assign it to the list head, and return a pointer to the new head node.
    def add_front(self, val):
        self.next = self.head
        self.head = val
        print(self.head)
        return self



new_list = sll(7)
new_list.add_front(5).display_head()