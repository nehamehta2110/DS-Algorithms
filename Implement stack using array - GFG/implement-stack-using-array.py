#User function Template for python3

class MyStack:
    
    def __init__(self):
        self.arr=[None]*1000
        self.top = -1
    
    #Function to push an integer into the stack.
    def push(self,data):
        #add code here
        self.top+=1
        self.arr[self.top] = data
        
    
    #Function to remove an item from top of the stack.
    def pop(self):
        #add code here
        if self.isEmpty():
            return -1
        else:
            
            popped_el = self.arr[self.top]
            self.top -= 1
            return popped_el
        
    def isEmpty(self):
        if self.top == -1:
            return True
        return False
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyStack()
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