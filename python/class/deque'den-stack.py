from deque import *

class dStack(Deque):
    
    def __init__(self):
        Deque.__init__(self)

    def push(self, item):
        Deque.addRear(self, item)

    def pop(self):
        return Deque.removeRear(self)

    def peek(self):
        self.items.insert(0,self.items[0])
        return Deque.removeRear(self)
        
