class Node:
    def __init__(self, valueInput):
        self.value = valueInput
        self.left = None
        self.right = None

class B_Tree:
    def __init__(self, valueInput):
        self.root = Node(valueInput)

# BST: Add
# Create an add(val) method on the BST object to add new value to the tree. 
# This entails creating a BTNode with this value and connecting it at the appropriate place in the tree. 
# Unless specified otherwise, BSTs can contain duplicate values.

    def add_node(self, valueInput):
        new_node = Node(valueInput)
        runner = self.root
        while runner:
            if new_node.value < runner.value:
                if runner.left == None:
                    runner.left = new_node
                    return self
                else:
                    runner = runner.left
            else:
                if runner.right == None:
                    runner.right = new_node
                    return self
                else:
                    runner = runner.right

# BST: Contains
# Create a contains(val) method on BST that returns whether the tree contains a given value. 
# Take advantage of the BST structure to make this a much more rapid operation than SList.contains() would be.

    def contains(self, valueInput):
        runner = self.root
        while runner:
            if valueInput == runner.value:
                return True
            else:
                if valueInput < runner.value:
                    if runner.left == None:
                        return False
                    else:
                        runner = runner.left
                else:
                    if runner.right == None:
                        return False
                    else:
                        runner = runner.right
        return self

# BST: Min
# Create a min() method on the BST class that returns the smallest value found in the BST.

    def min_value(self):
        runner = self.root
        while runner:
            if runner.left == None:
                return runner.value
            else:
                runner = runner.left
        return self

# BST: Max
# Create a max() BST method that returns the largest value contained in the binary search tree.

    def max_value(self):
        runner = self.root
        while runner:
            if runner.right == None:
                return runner.value
                
            else:
                runner = runner.right
        return self

# BONUS: BST: Size 
# Write a size() method that returns the number of nodes (values) contained in the tree.
    
    def size(self):
        if self.root == None:
            return 0
        leftSide = B_Tree(self.root.left)
        rightSide = B_Tree(self.root.right)
        return 1 + leftSide.size() + rightSide.size()
        

# BONUS: BST: Is Empty
# Create an isEmpty() method to return whether the BST is empty (whether it contains no values).
    
    def emptyTree(self):
        if self.root == None:
            print('Tree is Empty')
            return False
        else:
            print('This tree has nodes')
            return True
        
        

my_tree = B_Tree(6)
print(my_tree.add_node(4).add_node(10).add_node(30).add_node(1).contains(4))
print(my_tree.emptyTree())




