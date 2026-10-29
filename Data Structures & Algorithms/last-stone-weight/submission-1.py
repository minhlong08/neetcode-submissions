class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []

        for s in stones:
            # * -1 to be maxHeap
            heapq.heappush(maxHeap, s * -1)

        while len(maxHeap) > 1:
            # get the correct value back
            stoneX = heapq.heappop(maxHeap) * -1
            stoneY = heapq.heappop(maxHeap) * -1

            if stoneX == stoneY:
                continue
            else:
                newStone = stoneX - stoneY
                heapq.heappush(maxHeap, newStone * -1)
        
        return maxHeap[0] * -1 if maxHeap else 0