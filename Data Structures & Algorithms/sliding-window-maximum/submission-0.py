class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        maxHeap = []

        # initialise the maxHeap for the first window
        for i in range(k):
            heapq.heappush(maxHeap, (nums[i] * -1, i))
        
        # append the maximum element to res
        res.append(maxHeap[0][0] * -1)

        # sliding the window forward
        for j in range(k, len(nums)):
            # add the new number to the heap
            heapq.heappush(maxHeap, (nums[j] * -1, j))

            # find the maximum element in the current window by peeking at the top of the heap and checking if the index is in our window
            while maxHeap[0][1] < j - k + 1:
                heapq.heappop(maxHeap)

            # now we know that our max is in the window
            res.append(maxHeap[0][0] * -1)

        return res