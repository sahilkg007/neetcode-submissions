class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r =  max(weights), sum(weights)
        
        while l<=r:
            res = cap = (l+r)//2
            ships = 0
            for w in weights:
                if cap - w < 0:
                    ships += 1
                    cap = res
                cap -= w
            
            if ships <= days:
                r = res - 1
            else:
                l = res + 1
        
        return res

