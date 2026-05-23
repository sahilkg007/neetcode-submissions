class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l,r =  max(weights), sum(weights)
        
        while l<r:
            mid =cap = (l+r)//2
            ships = 1
            for w in weights:
                if cap - w < 0:
                    ships += 1
                    cap = mid
                cap -= w
            
            if ships <= days:
                r = mid
            else:
                l = mid + 1
    
        return l

