class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals = [[0]*i for i in range(1,numRows+1)]
        for i in range(numRows):
            pascals[i][0]=pascals[i][i] = 1
            for j in range(1,i):
                
                pascals[i][j] = pascals[i-1][j-1] + pascals[i-1][j]
                
        return pascals
            
            
        