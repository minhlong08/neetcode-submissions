"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: (x.start,x.end))
        prevEnd = intervals[0].end

        for ind in range(1, len(intervals)):
            curInterval = intervals[ind]

            if curInterval.start < prevEnd:
                return False
            else:
                prevEnd = curInterval.end

        return True