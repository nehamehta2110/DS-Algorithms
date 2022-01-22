#Sort the array using insertion sort

class Solution:
    def insertionSort(self, alist, n):
        #code here
        for i in range(1,n):
            for j in range(i-1, -1,-1):
                if alist[j]> alist[j+1]:
                    alist[j], alist[j+1] = alist[j+1], alist[j]
                else:
                    break

#{ 
#  Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends