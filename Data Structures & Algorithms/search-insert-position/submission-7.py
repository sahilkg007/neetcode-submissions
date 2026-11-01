class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        
        
        mid = l+((r-l)//2)
        while l<r:
            mid = l+((r-l)//2)

            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                r=mid-1
            if target > nums[mid]:
                l=mid+1
        if target > nums[mid-1]:
            return l
        if target < nums[mid+1]:
            return l+1


