class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums,target,True)
        right = self.binarySearch(nums,target,False)
        return [left,right]
        
        def binarySearch(self,nums,target, leftBias):
            l,r = 0, len(nums)
            i = -1
            while l<=r:
                mid = (l+r)//2
                
                if target<nums[mid]:
                    r = mid - 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    i = mid
                    if leftBias:
                        r = mid - 1
                    else:
                        l = m + 1

                    
            return res
                
            
