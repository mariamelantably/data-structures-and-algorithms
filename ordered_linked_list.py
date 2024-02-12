class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#this is for a linked list ordered in ascending order
class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None
    
    def display(self):
        string = "HEAD --> "
        current = self.head
        while current is not None:
            string += "[" + str(current.data) + "] -->"
            current = current.next
        string += "NONE"
        print(string)
    
    def insert(self, data):
        new_node = Node(data)
        current = self.head
        #1st case - list is empty
        if self.is_empty():
            self.head = new_node
        elif current.data > data:#2nd case - data is smaller than current head
            new_node.next = self.head
            self.head = new_node
        else:
            while current.next is not None and current.next.data < data:
                current = current.next
            new_node.next = current.next
            current.next = new_node
    
    def delete(self, data):
        current = self.head
        if current.data == data:
            self.head = self.head.next
        else:
            while current.next.data != data:
                current = current.next
            current.next = current.next.next


l = LinkedList()
l.insert(2)
l.insert(4)
l.insert(5)
l.insert(3)
l.insert(7)
l.insert(6)
l.delete(4)
l.display() 