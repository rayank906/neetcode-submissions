class Twitter:

    def __init__(self):
        self.timestamp = 0
        self.tweets = defaultdict(list) # usr -> tweets
        self.following = defaultdict(set) # usr -> following


    def postTweet(self, userId: int, tweetId: int) -> None:
        """
            1. add tweet to user tweets
        """
        self.tweets[userId].append([self.timestamp, tweetId])
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
            1. add userId to following
            2. grab last tweets for all users userId is following
            3. Add to max heap (ts, tweet, usrId, index - 1)
            4. Add to res and visit next indices until res == 10
        """
        self.following[userId].add(userId)
        maxHeap = []
        res = []

        for usrId in self.following[userId]:
            if usrId in self.tweets:
                index = len(self.tweets[usrId]) - 1
                ts, tweetId = self.tweets[usrId][index]
                maxHeap.append([ts, tweetId, usrId, index - 1])
        
        heapq.heapify_max(maxHeap)

        while maxHeap and len(res) < 10:
            ts, tweetId, usrId, index = heapq.heappop_max(maxHeap)
            res.append(tweetId)
            if index >= 0:
                ts, tweetId = self.tweets[usrId][index]
                heapq.heappush_max(maxHeap, [ts, tweetId, usrId, index - 1])
        
        return res
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        """
            1. add followeeId to followerId hashmap
        """
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
            1. remove followeeId from followerId hashmap
        """
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
