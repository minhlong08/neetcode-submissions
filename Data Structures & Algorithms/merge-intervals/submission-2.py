class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval: (interval[0],interval[1]))

        res = []
        newInterval = intervals[0]

        for i in range(1, len(intervals)):
            curInterval = intervals[i]
            # print(f"newInterval: {newInterval}")
            # print(f"curInterval: {curInterval}")
            if newInterval[1] < curInterval[0]:
                res.append(newInterval)
                newInterval = curInterval
            else:
                newStart = min(newInterval[0],curInterval[0])
                newEnd = max(newInterval[1], curInterval[1])
                newInterval = [newStart, newEnd]

        res.append(newInterval)
        return res
