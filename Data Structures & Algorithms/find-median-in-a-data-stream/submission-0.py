class MedianFinder:
    def __init__(self):
        self.nums = []
        self.length = 0

    def addNum(self, num: int) -> None:
        i = 0
        while i < self.length:
            if self.nums[i] > num:
                break
            i += 1
        self.nums.insert(i, num)
        self.length += 1

    def findMedian(self) -> float:
        if self.length % 2 == 0:
            firstMid = self.length // 2 - 1
            secondMid = (self.length // 2)
            return (self.nums[firstMid] + self.nums[secondMid]) / 2
        else:
            mid = self.length // 2
            return self.nums[mid]
        