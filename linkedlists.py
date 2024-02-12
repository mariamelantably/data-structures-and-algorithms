class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def display(self):
        string = "HEAD -->"
        current = self.head
        while current is not None:
            string += "[" + str(current.data) + "] --> "
            current = current.next
        string += "NONE"
        print(string)

    def addToHead(self, data):
        new_Node = Node(data)
        new_Node.next = self.head
        self.head = new_Node
    
    def addToEnd(self, data):
        new_node = Node(data)
        current = self.head
        if self.head != None:
            while current.next != None:
                current = current.next
            current.next = new_node
        else:
            self.addToHead(data)
    
    def addAfterNode(self, search_node_data, insert_data):
        current = self.head
        while current is not None and current.data != search_node_data:
            current = current.next
        
        if current is None:
            print("Node with data", search_node_data, "not found.")
            return
    
        new_node = Node(insert_data)
        new_node.next = current.next
        current.next = new_node

    def deleteNode(self, data):
        if self.head == None:
            return False
        
        if self.head.data == data:
            self.head = self.head.next
            return True
        
        current = self.head
        while current != None and current.next != None:
            if current.next.data == data:
                current.next = current.next.next
                return True
            
            current = current.next
        return False
    
    def replaceData(self, oldData, newData):
        current = self.head
        while current != None:
            if current.data == oldData: 
                current.data = newData
                return
            current = current.next
    
    def replaceAllData(self, oldData, newData):
        current = self.head
        while current != None:
            if current.data == oldData:
                current.data = newData
            current = current.next

    def indexOf(self, data):
        index = 0
        current = self.head
        while current != None:
            if current.data == data:
                return index 
            
            current = current.next
            index += 1
        return "Not Found"

list = LinkedList()
list.addToEnd(10)
list.addToHead(5)
list.addToEnd(15)
list.addToHead(20)
list.addAfterNode(5, 7)
list.display()
