#LIFO (Last-In, First-Out)
#program that implements a LIFO queue using a list
class LifoQueue:
    def __init__(self):
        self.items = []

    # adding element to queue
    def push(self, item):
        self.items.append(item)
    #removing element from queue
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0
q = LifoQueue()
q.push(1)
q.push(2)
q.push(3)
print(q.pop())  
print(q.pop())  
print(q.pop()) 
print(q.pop())  
