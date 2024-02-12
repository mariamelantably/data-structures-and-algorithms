class Queue:
    def __init__(self, length):
        self.length = length
        self.queue = [""]*length
    
    def __str__(self):
        stri = ""
        for i in self.queue:
            stri += str(i)
        return stri

    def is_empty(self):
        return (all(i is None for i in self.queue))

    def is_full(self):
        return (all(i is not None for i in self.queue))
    
    def enqueue(self, data):
        i = 0
        while i <= self.length - 1:
            if self.queue[i] is None:
                self.queue[i] == data
                return
            i += 1
        print("Queue is full. We can not enqueue anymore")
    
    def dequeue(self):
        if not self.is_empty():
            max_pr = -1
            max_index = -1
            for i in range(len(self.queue)):
                if self.queue[i] != None:
                    if self.queue[i][1] > max_pr:
                        max_pr = self.queue[i][1]
                        max_index = i
            retr = self.queue[max_index]
            self.queue[max_index] = None
            return retr
        else:
            print("Queue is empty. We can not dequeue anymore.")
                