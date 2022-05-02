class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_s= nums[0]
        s = 0
        
        
        for i in range(len(nums)):
            s+=nums[i]
            max_s = max(s, max_s)
            if s<0:
                s = 0
                
        return max_s
            
        