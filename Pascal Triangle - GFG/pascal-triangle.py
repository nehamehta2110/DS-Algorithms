#User function Template for python3

#User function Template for python3
class Solution:

	def nthRowOfPascalTriangle(self,n):
	    # code here
	    
        m = []
	    
	    for i in range(n):
	        r = []
	        for j in range(i+1):
	            if j==0 or j==i:
	                r.append(1)
	            else:
	                r.append((m[i-1][j-1] + m[i-1][j])%1000000007)
	                
	        m.append(r)
	    return m[n-1]
	                
	                
	                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    ob = Solution()
	    ans=ob.nthRowOfPascalTriangle(n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends