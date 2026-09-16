class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # for i in range(len(trips)):
        if trips[0][2] > trips[1][1]:
            if trips[0][0] + trips[1][0] > capacity:
                return False
        else:
            if trips[0][0] > capacity or trips[1][0] > capacity:
                return False  
            else:
                return True              
