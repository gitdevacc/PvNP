
class Queue:
    def __init__(self):
        self.queue=[]
    def isEmpty(self):
        if len(self.queue)==0:
            return None
        else:
            return False
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        return self.queue.pop(0)
    def front(self):
        return self.queue[0]
    def size(self):
        return len(self.queue)
    def __str__(self):
        return self.queue
        