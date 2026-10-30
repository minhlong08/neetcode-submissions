class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # kth closest point -> use maxHeap
        # if heap size > k -> pop an element
        maxHeap = []
        for x, y in points:
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(maxHeap, (dist * -1, (x,y)))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        res = []
        for element in maxHeap:
            res.append([element[1][0], element[1][1]])
        
        return res
