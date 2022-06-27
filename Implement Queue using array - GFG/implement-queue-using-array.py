#User function Template for python3

class MyQueue:
    
    #Function to push an element x in a queue.
    def __init__(self):
        self.capacity = 100000
        self.arr = [None]*self.capacity
        self.count = 0
        self.front = 0
        self.rear = 0
    def push(self, x):
        if self.count==self.capacity:
            return -1
            
        self.arr[self.rear%self.capacity] = x
        self.rear+=1
        self.count+=1
         
         #add code here
     
    #Function to pop an element from queue and return that element.
    def pop(self): 
        
        if self.count == 0:
            return -1
            
        pop_el = self.arr[self.front%self.capacity]
        self.arr[self.front%self.capacity] =-1
        self.front+=1
        self.count-=1
        return pop_el
        
         # add code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   

# } Driver Code Ends