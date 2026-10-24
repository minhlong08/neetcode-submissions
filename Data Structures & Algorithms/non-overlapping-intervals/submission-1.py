class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prevEnd = intervals[0][1]

        res = 0

        for ind in range(1, len(intervals)):
            curInterval = intervals[ind]

            # check if current interval overlaps with previous one
            if curInterval[0] < prevEnd:
                # set prevEnd to the minimum of the 2
                prevEnd = min(prevEnd, curInterval[1])
                # greedily remove the interval where the end is larger
                res += 1
            else: # non overlapping
                # set the new prevEnd to current interval end
                prevEnd = curInterval[1]
        return res