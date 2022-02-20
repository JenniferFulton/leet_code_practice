class Node():
    def __init__(self, value):
        self.value = value
        self.next = None 

class sll():
    def __init__(self, nodeValue):
        self.head = Node(nodeValue)
        
# SLL Utilities:
# Add a method contains(value) to your SLL class, which is given a value as a parameter.  Return a boolean (true/false); true, if the list possesses a node that contains the provided value.


# Length:
# Create a new SLL method length() that returns number of nodes in that list.


# Display:
# Create display() that returns a string containing all list values. Build what you wish console.log(myList) did!


# Move:
# SList: Move Min to Front
# Create a standalone function that locates the minimum value in a linked list, and moves that node to the front of the list. Return the new list, with all nodes still present, and all (except for the new head node) in their original order.


# SList: Move Max to Back
# Create a standalone function that locates the maximum value in a linked list, and moves that node to the back of the list. Return the new list, with all nodes still present, and all in their original order except for the node you moved to the end of the singly linked list.