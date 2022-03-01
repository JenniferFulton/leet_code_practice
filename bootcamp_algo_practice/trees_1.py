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



# BST: Min
# Create a min() method on the BST class that returns the smallest value found in the BST.



# BST: Max
# Create a max() BST method that returns the largest value contained in the binary search tree.



# BONUS: BST: Size 
# Write a size() method that returns the number of nodes (values) contained in the tree.



# BONUS: BST: Is Empty
# Create an isEmpty() method to return whether the BST is empty (whether it contains no values).

my_tree = B_Tree(6)
my_tree.add_node(4)
print(my_tree.root.left.value)



