class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for c in nums:
            count[c] = 1+ count.get(c,0)
        
        minheap = [[-c,n] for [n,c] in count.items()]

        heapq.heapify(minheap)
        res = []
        for i in range(k):
            count,num = heapq.heappop(minheap)
            res.append(num)     
        return res
