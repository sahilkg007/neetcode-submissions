class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        l,r = 0,len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                        return True
                        
                        
            if nums[mid]>nums[l]:  # left part sorted 
                if target >= nums[mid] or target < nums[l]: # search on right side
                        l = mid + 1
                else:
                        r = mid - 1

            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            if nums[mid] == nums[l] == nums[r]:
                l+=1
                r-=1
        return False