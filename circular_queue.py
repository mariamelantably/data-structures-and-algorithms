class Queue:
    def __init__(self, length):
        self.length = length + 1
        self.queue = [""]*self.length
        self.front = 0
        self.rear = 0
    
    def __str__(self):
        return " ".join(self.queue) + " , " + str(self.front) + " , " + str(self.rear)

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.front ==(self.rear + 1)%self.length

    def dequeue(self):
        if not self.is_empty():
            self.front = (self.front + 1)%(self.length)
    
    def enqueue(self, data):
        if not self.is_full():
            self.queue[self.rear] = data
            self.rear = (self.rear + 1)%self.length

q = Queue(4)
q.enqueue('0')
q.enqueue('1')
q.enqueue('2')
q.enqueue('3')
q.enqueue('4')
q.dequeue()
q.enqueue('5')
q.enqueue('6')
print(q)