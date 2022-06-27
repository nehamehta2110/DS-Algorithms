class MyStack:

    def __init__(self):
        obj = MyQueue()
        self.q1 = obj
        

    def push(self, x: int) -> None:
        self.q1.qpush(x)
        size = self.q1.qsize()
        
        for i in range(0,size-1):
            self.q1.qpush(self.q1.qtop())
            self.q1.qpop()
        

    def pop(self) -> int:
        return self.q1.qpop()
        

    def top(self) -> int:
        return self.q1.qtop()

    def empty(self) -> bool:
        size = self.q1.qsize()
        if size <= 0:
            return True
        return False
        
class MyQueue:
    def __init__(self):
        
        self.capacity = 100000
        self.count = 0
        self.arr = [None]*self.capacity
        self.front = 0
        self.rear = 0
        
    def qgetter(self):
        return self.arr
        
    def qpush(self, x):
        if self.count == self.capacity:
            return -1
        self.arr[self.rear % self.capacity] = x
        self.rear+=1
        self.count+=1
        
    def qpop(self):
        if self.count == 0:
            return -1
        pop_el = self.arr[self.front % self.capacity]
        self.arr[self.front % self.capacity] = -1
        self.front+=1
        self.count-=1
        return pop_el
        
    def qtop(self):
        if self.count == 0:
            return -1
        return self.arr[self.front % self.capacity]
    
    def qsize(self):
        return self.count
            

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()