class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        for i in range(len(trips)-1):
            if trips[i][2] > trips[i+1][1]:
                if trips[i][0] + trips[i+1][0] > capacity:
                    return False
            else:
                if trips[i][0] > capacity or trips[i+1][0] > capacity:
                    return False  
                else:
                    return True              
