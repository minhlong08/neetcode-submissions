class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = deque() # (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                pastIndex, pastHeight = stack.pop()
                possibleArea = (i - pastIndex) * pastHeight
                res = max(res, possibleArea)

                # the current height can be extend backward
                start = pastIndex        
            stack.append((start, h))

        for i, h in stack:
            res = max(res, h * (len(heights) - i))

        return res