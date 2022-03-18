#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        num1s, num2s = 0, 0
        for i in range(n):
            if arr[i]==1:
                num1s+=1
            if arr[i]==2:
                num2s+=1
        
        for i in range(n):
            if i<(n-num1s-num2s):
                arr[i]=0
            elif i<(n-num2s):
                arr[i] = 1
            else:
                arr[i] = 2
                
                


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends