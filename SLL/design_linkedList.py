class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  

class MyLinkedList:
    def __init__(self):
        self.head = None

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
        
        #make sure indec is not out of range
        if index > current_index:
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
            while runner != None:
                runner = runner.next
            runner.next =  Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        current_index = 0
        runner = self.head
        while runner != None:
            if current_index == index:
                temp = runner
                runner = Node(val)
                runner.next = temp
            current_index += 1
            runner = runner.next
        
        # if index equals the length of the list append to the end of the list
        if index == current_index + 1:
            runner.next = Node(val)

    def deleteAtIndex(self, index: int) -> None:
        pass


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)