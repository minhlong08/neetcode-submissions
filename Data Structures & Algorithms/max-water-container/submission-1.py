class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_area = 0
        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            max_area = max(area, max_area)

            # move the pointer of the smaller height value
            # If heights[i] is smaller, any future container will have
            # smaller width but the height is still at most heights[i]
            # so i cannot produce a larger area than the current part
            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r - 1
        
        return max_area
        