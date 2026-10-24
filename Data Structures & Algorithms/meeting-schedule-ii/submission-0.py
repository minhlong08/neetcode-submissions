"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # the number of rooms required is the maximum number of overlapping
        # meetings at any point on the number line

        startTime = []
        endTime = []

        for interval in intervals:
            startTime.append(interval.start)
            endTime.append(interval.end)

        startTime.sort()
        endTime.sort()
        # Two pointer approach, pointer in startTime moves -> increase count of current meetings, pointer in endTime moves -> decrease the count of current meettings
        count = 0
        maxCount = 0

        p1, p2 = 0, 0
        while p1 < len(startTime) and p2 < len(endTime):
            if startTime[p1] < endTime[p2]:
                count += 1
                maxCount = max(maxCount, count)
                p1 += 1
            else:
                count -= 1
                p2 += 1

        return maxCount