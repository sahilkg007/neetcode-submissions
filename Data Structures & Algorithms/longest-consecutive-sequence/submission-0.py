class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        maxc = 0
        for i in nums:
            k = i
            while k+1 in nums:
                count+=1
                print(k, count)
                k+=1
            
            maxc = max(count,maxc)
            if i != len(nums)-1:
                count = 1
            
            
        return maxc