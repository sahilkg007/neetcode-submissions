class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    
        while val in nums:
                nums.remove(val)

        count = 0
        for i in nums:
            count+=1
        return count