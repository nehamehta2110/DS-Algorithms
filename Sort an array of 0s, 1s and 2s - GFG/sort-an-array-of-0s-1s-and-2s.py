#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        lo, mid = 0, 0
        hi = n-1
        
        while mid<=hi:
            if arr[mid]==0:
                arr[mid], arr[lo] = arr[lo], arr[mid]
                mid+=1
                lo+=1
            elif arr[mid]==1:
                mid+=1
            else:
                arr[mid],arr[hi]=arr[hi],arr[mid]
                hi-=1
                
                


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