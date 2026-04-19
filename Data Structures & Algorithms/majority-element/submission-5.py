class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = None
        for i in range(len(nums)):
            if count == 0 :
                res = nums[i]

            if nums[i] == res:
                count += 1
            else:
                count -= 1
        
        return res