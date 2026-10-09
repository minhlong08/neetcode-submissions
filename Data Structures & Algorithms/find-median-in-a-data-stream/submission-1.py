class MedianFinder:
    def __init__(self):
        self.small = [] # smaller half of the array, store by max-heap
        self.large = [] # larger half of the arrya, store by min-heap

    def addNum(self, num: int) -> None:
        # When we get an element
        # Greater the minimum of min-heap -> push to min-heap
        # else push to max-heap
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, num * -1.0) # push to max-heap soo multiple value with -1

        if len(self.small) > len(self.large) + 1:
            item = heapq.heappop(self.small) * -1.0 # poping from max heap so we need to multiply by -1 to restore the element
            heapq.heappush(self.large, item)

        if len(self.large) > len(self.small) + 1.0:
            item = heapq.heappop(self.large)
            heapq.heappush(self.small, item * -1.0)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else: # same size -> even length list
            return (-1 * self.small[0] + self.large[0]) / 2.0
        
        