class Solution:
    def trap(self, height: List[int]) -> int:
        # 0(1) memory solution
        # since we only care about the min(maxLeft, maxRight)
        # -> 2 pointer approach l and r
        # only move forward the smaller pointer since it is the bottleneck

        l, r = 1, len(height) - 2
        leftMax, rightMax = height[0], height[-1]
        res = 0
        while l <= r:
            if leftMax <= rightMax:
                # bottleneck is in left side
                res += max(leftMax - height[l], 0)
                # update the leftMax
                leftMax = max(leftMax, height[l])
                l = l + 1
            else:
                # bottleneck is in right side
                res += max(rightMax - height[r], 0)
                # update right max
                rightMax = max(rightMax, height[r])
                r = r - 1
        
        return res
