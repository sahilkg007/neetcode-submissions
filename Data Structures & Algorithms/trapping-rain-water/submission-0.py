class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        res = 0

        leftmax, rightmax = height[l], height[r]
        while l<r:
            leftmax = max(leftmax,height[l])
            rightmax = max(rightmax, height[r])
            res += max(0,(leftmax - height[l]))
            res += max(0,(rightmax - height[r]))
            
            if height[l]>height[r]:
                r-=1
            else:
                l+=1
            


        return res