class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """Concatenate, 
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # temp = nums[n-k:] + nums[:n-k]
        i = 0
        while k>0:
            nums[k-1],nums[n-1-i] = nums[n-1-i],nums[k-1]
            k-=1
            i+=1
        
        
