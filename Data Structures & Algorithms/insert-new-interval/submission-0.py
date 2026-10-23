class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # the newInterval comes before the curInterval
            # newInterval end < curInterval start
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # the newInterval comes after the curInterval
            # newInterval start > curInterval end
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else: # overlapping
                newStart = min(newInterval[0], intervals[i][0])
                newEnd = max(newInterval[1], intervals[i][1])

                # update the new interval but don't add to result yet since it might overlap with the remaining intervals
                newInterval = [newStart, newEnd]

        # Handle edge cases, make sure newInterval is always added
        res.append(newInterval)
        return res

        