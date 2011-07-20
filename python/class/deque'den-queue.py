from deque import *

class dQueue(Deque):
        def __init__(self):
                Deque.__init__(self)

        def enqueue(self, item):
                Deque.addRear(self, item)

        def dequeue(self):
                return Deque.removeFront(self)

