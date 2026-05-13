class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        res = float('inf')

        for r in range(len(nums)):
            total += nums[r]
            if total>=target:
                total-=nums[l]
                res = min(r-l+1,res)
                l+=1
        return False if res == float('inf') else res