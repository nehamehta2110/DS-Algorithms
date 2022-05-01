class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    idx = i-1
                    while idx>=0:
                        if matrix[idx][j]!=0:
                            matrix[idx][j] =-999
                        idx = idx-1
                    
                    idx = i+1
                    while idx<m:
                        if matrix[idx][j]!=0:
                            matrix[idx][j] =-999
                        idx = idx+1
                    
                    idx = j-1
                    while idx>=0:
                        if matrix[i][idx]!=0:
                            matrix[i][idx] =-999
                        idx = idx-1
                    
                    idx = j+1
                    while idx<n:
                        if matrix[i][idx]!=0:
                            matrix[i][idx] =-999
                        idx = idx+1
                        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==-999:
                    matrix[i][j] = 0
                    
        return matrix
                    
                        
                    
                        
                        
                    
                
        