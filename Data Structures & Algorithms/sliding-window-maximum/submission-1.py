class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        dq = deque() # indices; their values are in decreasing order

        for i, num in enumerate(nums):
            # frop the front index if it is out of the window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Drop smaller values from the back: they can never be a max again
            while dq and nums[dq[-1]] < num:
                dq.pop()
            
            dq.append(i)

            # edge case check if window is full
            if i >= k - 1:
                res.append(nums[dq[0]])
        
        return res