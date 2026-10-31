class Twitter:
    def __init__(self):
        self.time = 0
        # userId -> list of [timestamp, tweetIds], larger timestamp -> more recent
        self.tweetMap = defaultdict(list)
        # userId -> hashset of followeeId
        self.followmap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        curTimeStamp = self.time
        self.tweetMap[userId].append((curTimeStamp, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = []
        # the larger the timestamp the more recent the post -> use maxHeap
        maxHeap = []

        # add the user to be following themself
        self.followmap[userId].add(userId)
        for followeeId in self.followmap[userId]:
            # check if the people userId is following has tweets
            if followeeId in self.tweetMap:
                # get the last post in the list which is the most recent post
                index = len(self.tweetMap[followeeId]) - 1
                timestamp, tweetId = self.tweetMap[followeeId][index]

                # timestamp for the heap to keep track of the most recent post
                # index - 1 is the next most recent post of followeeId since the list is sorted
                maxHeap.append((-timestamp, tweetId, followeeId, index - 1))
        heapq.heapify(maxHeap)

        # fetch the post
        while maxHeap and len(posts) < 10:
            timestamp, tweetId, followeeId, index = heapq.heappop(maxHeap)
            timestamp = timestamp * -1 # get the original timestamp value

            posts.append(tweetId)
            if index >= 0:
                nextTimestamp, nextTweet = self.tweetMap[followeeId][index]
                heapq.heappush(maxHeap, (-nextTimestamp, nextTweet, followeeId, index - 1))

        return posts

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
