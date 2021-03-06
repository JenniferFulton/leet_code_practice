# Implement the MyLinkedList class:
# MyLinkedList() Initializes the MyLinkedList object.
# get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# addAtTail(int val) Append a node of value val as the last element of the linked list.
# addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
# deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  

class MyLinkedList:
    def __init__(self):
        self.head = None
    
    def view(self):
        #if the list is empty make the input value the head of the list
        if self.head == None:
            return None
        else:
            runner = self.head
            while runner != None:
                print(runner.value)
                runner = runner.next

    def get(self, index: int) -> int:
        #if index given is a negative number
        if index < 0:
            return -1
        
        #if index is greater than 0
        current_index = 0
        runner = self.head
        while runner != None:
            if current_index == index:
                return runner.value
            current_index += 1
            runner = runner.next
        print(current_index)
        
        #make sure indec is not out of range
        if index >= current_index:
            return -1
        

    def addAtHead(self, val: int) -> None:
        #if the list is empty make the input value the head of the list
        if self.head == None:
            self.head = Node(val)
        
        #make the input value the new head of this list
        else:
            new_head = Node(val)
            new_head.next = self.head
            self.head = new_head
        

    def addAtTail(self, val: int) -> None:
        #if the list is empty make the input value the head of the list
        if self.head == None:
            self.head = Node(val)
        
        #add the value to the end of the list
        else:    
            runner = self.head
            while runner.next != None:
                runner = runner.next
            runner.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        #if trying to add at index 0, essentially creating a new head
        if index == 0:
            new_head = Node(val)
            new_head.next = self.head
            self.head = new_head
        
        #index other than 0
        else:    
            current_index = 0
            runner = self.head
            while runner != None:
                if current_index == index:
                    previous_node.next = Node(val)
                    previous_node.next.next = runner
                current_index += 1
                previous_node = runner
                runner = runner.next
        
            # if index equals the length of the list append to the end of the list
            if index == current_index:
                runner = self.head
                while runner.next != None:
                    runner = runner.next
                runner.next = Node(val) 

    def deleteAtIndex(self, index: int) -> None:
        #if index is zero, create a new head with next node
        if index == 0:
            self.head = self.head.next
            
        else:
            current_index = 0
            runner = self.head
            while runner != None:
                if current_index == index:
                    previous_node.next = runner.next
                current_index += 1
                previous_node = runner
                runner = runner.next


# Your MyLinkedList object will be instantiated and called as such:
myLinkedList = MyLinkedList()
myLinkedList.addAtHead(4)
# myLinkedList.addAtHead(5)
# myLinkedList.addAtHead(3)
# myLinkedList.addAtHead(1)
# myLinkedList.view()   
print(myLinkedList.get(1))
# print(myLinkedList.get(3))
# print(myLinkedList.get(5))
# print(myLinkedList.get(-2))          
# myLinkedList.deleteAtIndex(0)
# myLinkedList.deleteAtIndex(5)
# myLinkedList.view()
# myLinkedList.addAtTail(9)
# myLinkedList.addAtIndex(1, 2)
# myLinkedList.addAtIndex(0,20) 
# myLinkedList.addAtIndex(5,12) 
myLinkedList.view()   
