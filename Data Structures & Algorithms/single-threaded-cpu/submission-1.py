class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        available = []
        pending = []
        for i, (enqt,proctime) in enumerate(tasks):
            heapq.heappush(pending,(enqt, proctime, i))
        
        time = 0
        res = []
        
        while pending or available:
            while pending and pending[0][0] <= time :
                enqt, proctime , i = heapq.heappop(pending)
                heapq.heappush(available,(proctime,i))
            
            if not available:
                time = pending[0][0]
                continue
            
            proctime , i = heapq.heappop(available)
            time+= proctime
            res.append(i)
        return res



            

        
        


