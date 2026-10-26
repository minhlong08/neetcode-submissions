class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        # Pointers start on the edges. Edge bars can never hold water,
        # so they only serve as the initial walls.
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        # Stop when the pointers meet. The meeting cell is the tallest bar
        # (the pointer on it never moved because it was the bigger side),
        # and the tallest bar holds no water, so skipping it is safe.
        while l < r:
            # Water level is limited by the smaller of the two maxes.
            # Whichever side is smaller is the bottleneck, so we can settle
            # the next cell on that side without knowing the rest of the array.
            if leftMax < rightMax:
                # Move first, then process the cell we just stepped onto.
                l += 1

                # Update the max to INCLUDE the current bar before computing water.
                # This is safe and replaces max(..., 0):
                #   - If height[l] < old leftMax: leftMax is unchanged,
                #     so water = old leftMax - height[l] (positive, as expected).
                #   - If height[l] >= old leftMax: leftMax becomes height[l],
                #     so water = height[l] - height[l] = 0 (a bar at least as tall
                #     as everything to its left can't hold water).
                # In algebra: max(oldMax, h) - h == max(oldMax - h, 0)
                leftMax = max(leftMax, height[l])

                # Can't be negative, because leftMax >= height[l] after the update.
                res += leftMax - height[l]
            else:
                # Mirror image of the left side.
                r -= 1

                # Including height[r] in rightMax gives 0 water when this bar
                # is the tallest seen from the right, and the normal amount otherwise.
                rightMax = max(rightMax, height[r])

                res += rightMax - height[r]

        return res