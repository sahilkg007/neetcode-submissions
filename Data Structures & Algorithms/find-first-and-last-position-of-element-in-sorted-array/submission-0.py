class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums)
        res = [-1,-1]
        while l<r:
            mid = (l+r)//2
            
            if target<nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            if nums[mid] == target:
                if res[0] is -1:
                    res[0] = res[1] = mid
                    l += 1
                else:
                    res[1] = mid
                    l += 1
            
        return res
            
            
