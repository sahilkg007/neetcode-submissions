class Twitter:

    def __init__(self):
        self.count = 0
        self.tweekmap = defaultdict(list)  # userId -> list of [count,tweekIds]
        self.followmap = defaultdict(set)  #userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweekmap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followmap[userId].add(userId)
        for followeeId in self.followmap[userId]:
            if followeeId in self.tweekmap:
                index = len(self.tweekmap[followeeId])-1
                count,tweekId = self.tweekmap[followeeId][index]
                minHeap.append([count, tweekId, followeeId, index-1])
        heapq.heapify(minHeap)
        while minHeap and len(res)<10:
            count, tweekId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweekId)
            if index >= 0:
                count, tweekId = self.tweekmap[followeeId][tweekId]
                heapq.heappush(minHeap, [count, tweekId, followeeId, index-1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
