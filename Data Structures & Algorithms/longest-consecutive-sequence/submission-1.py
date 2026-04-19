class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        maxc = 0
        for i in nums:
           
            while i+1 in nums:
                count+=1
                
                i+=1
            
            maxc = max(count,maxc)
            if i != len(nums)-1:
                count = 1
            
            
        return maxc