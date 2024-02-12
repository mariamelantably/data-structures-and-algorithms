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
            self.queue[self.length - 1] = None
            self.rear -= 1
        else:
            print("The queue is empty. We can not dequeue anymore")

q1 = Queue(4) #q1 is our main queue that we add data on to
q2 = Queue(4) #q2 is used for popping

def push(data):
    global q1
    q1.enqueue(data)

def pop():
    global q1, q2
    for i in range(q1.rear - 1):
        q2.enqueue(q1.queue[i])
    q1, q2 = q2, q1
    q2 = Queue(4)

push("A")
push("B")
push("C")
push("D")
pop()
pop()
pop()
print(q1)

