class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        for i, height1 in enumerate(heights):
            for j, height2 in enumerate(heights):
                if i == j:
                    continue
                
                area = abs(i - j) * min(height1, height2)
                max_area = max(area, max_area)
        
        return max_area
        