
class Stack:
    def __init__(self): 
            self.nodes=[]
    def isEmpty(self):
        if self.size()==0:
            return True
        else:
            return False
    def push(self, data):
        self.nodes.append(data)
        return self.nodes
    def pop(self):
        if self.isEmpty!=True:
            return self.nodes.pop()
        else: 
            raise Exception("Cannot pop from an empty stack.")
    def peek(self):
        return self.nodes[-1]
    def size(self):
        return len(self.nodes)
    def __str__(self):
        a=[]
        b=self.nodes
        while b.pop()==True:
            a.append(b.pop())
        return str(a)
    
