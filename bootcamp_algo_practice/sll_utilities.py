class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

class sll:
    def __init__(self, nodeValue):
        self.head = Node(nodeValue)
    
    def add_back(self, value):
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = Node(value)
        return self

# SLL Utilities:
# Add a method contains(value) to your SLL class, which is given a value as a parameter.  Return a boolean (true/false); true, if the list possesses a node that contains the provided value.
    def find_val(self, val):
        runner = self.head
        while runner != None:
            if runner.value == val:
                return True
            runner = runner.next
        #Would like it to print ('Value is not in the list') if True is not returned
        return self

# Length:
# Create a new SLL method length() that returns number of nodes in that list.
    def length(self):
        length = 0
        runner = self.head
        while runner != None:
            length += 1
            runner = runner.next
        print(f'This list has {length} nodes')
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
        runner = self.head
        minimum = self.head.value
        while runner != None:
            if runner.value < minimum:
                minimum = runner
            runner = runner.next
        self.head = minimum
        return(self)

# SList: Move Max to Back
# Create a standalone function that locates the maximum value in a linked list, and moves that node to the back of the list. 
# Return the new list, with all nodes still present, and all in their original order except for the node you moved to the end of the singly linked list.
    def mxn_toBack(self):
        runner = self.head
        max = self.head.value
        while runner != None:
            if runner.value > max:
                max = runner
            runner = runner.next
        runner.next = max
        return(self)

# new_list = sll(7)
# new_list.add_back(5).add_back(17).display().find_val(5).length()
moving_list = sll(17)
moving_list.add_back(6).add_back(20).add_back(14).add_back(199).min_toFront().display()