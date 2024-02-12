class Stack:
    def __init__(self, length):
        self.length = length
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def is_full(self):
        return len(self.stack) == self.length
    
    def push(self, data):
        if not self.is_full():
            self.stack.append(data)
        else:
            print("can not add. stack is full (stack overflow error)")
    
    def pop(self):
        if not self.is_empty():
            self.stack.pop(len(self.stack)-1)
        else:
            print("can not remove from an empty stack")
    
    def peek(self):
        return self.stack[len(self.stack)-1]

    def size(self):
        return len(self.stack)
    
stack = Stack(3)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.peek())
stack.pop()
print(stack.stack)
