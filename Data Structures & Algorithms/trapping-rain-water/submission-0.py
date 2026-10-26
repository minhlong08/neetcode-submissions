class Solution:
    def trap(self, height: List[int]) -> int:
        # maxLeft keep track of the maximum elevation to the left
        # maxRight keep track of the maximum elevation to the right
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)

        curMaxLeft = height[0]
        for i in range(1, len(height)):
            maxLeft[i] = curMaxLeft
            curMaxLeft = max(curMaxLeft, height[i])
        
        curMaxRight = height[-1]
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = curMaxRight
            curMaxRight = max(curMaxRight, height[i])

        # calculate the total trap number
        # at index i, the trap water amount is min(maxLeft, maxRight) - height[i] (negative is set to 0)
        res = 0
        for i in range(len(height)):
            res += max(min(maxLeft[i], maxRight[i]) - height[i], 0)
        
        return res
