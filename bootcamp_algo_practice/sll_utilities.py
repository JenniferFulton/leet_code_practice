class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

class sll:
    def __init__(self, nodeValue):
        self.head = Node(nodeValue)
    
    def add_back(self, value):
        runner = self.head
        while runner != None:
            runner = runner.next
        runner.next = Node(value)
        return self

# SLL Utilities:
# Add a method contains(value) to your SLL class, which is given a value as a parameter.  Return a boolean (true/false); true, if the list possesses a node that contains the provided value.
    def find_val(self, val):
        runner = self.head
        while runner != None:
            if runner.value == val:
                print(True)
            runner = runner.next
        return self

# Length:
# Create a new SLL method length() that returns number of nodes in that list.
    def length(self):
        length = 0
        runner = self.head
        while runner != None:
            length += 1
            runner = runner.next
        print('length is:', length)
        return self

# Display:
# Create display() that returns a string containing all list values. Build what you wish print(myList) did!
    def display(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self

# Move:
# SList: Move Min to Front
# Create a standalone function that locates the minimum value in a linked list, and moves that node to the front of the list. 
# Return the new list, with all nodes still present, and all (except for the new head node) in their original order.
    def min_toFront(self):
        minimum = self.head
        runner = self.head
        while runner != None:
            if runner < minimum:
                minimum = runner
            runner = runner.next
        self.head = min
        return(self)

# SList: Move Max to Back
# Create a standalone function that locates the maximum value in a linked list, and moves that node to the back of the list. 
# Return the new list, with all nodes still present, and all in their original order except for the node you moved to the end of the singly linked list.
    def mxn_toBack(self):
            max = self.head
            runner = self.head
            while runner != None:
                if runner > max:
                    max = runner
                runner = runner.next
            runner.next = max
            return(self)

new_list = sll(7)
new_list.head.next = Node(6)
new_list.head.next.next = Node(3)
new_list.find_val(6).length().display().min_toFront().display()