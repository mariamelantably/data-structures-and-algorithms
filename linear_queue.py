class Queue:
    def __init__(self, length):
        self.length = length
        self.queue = [None]*length
        self.rear = 0
    
    def __str__(self):
        stri = ""
        for i in self.queue:
            stri += str(i) + " "
        return stri

    def is_empty(self):
        return self.rear == 0
    
    def is_full(self):
        return self.rear >= self.length
    
    def enqueue(self, data):
        if not self.is_full():
            self.queue[self.rear] = data
            self.rear += 1
        else:
            print("The queue is full. We can not enqueue anymore")
    
    def dequeue(self):
        if not self.is_empty():
            for i in range(1, self.length):
                self.queue[i-1] = self.queue[i]
            #self.queue[self.length - 1] = None
            self.rear -= 1
        else:
            print("The queue is empty. We can not dequeue anymore")

q = Queue(4)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q)
q.dequeue()
print(q)

