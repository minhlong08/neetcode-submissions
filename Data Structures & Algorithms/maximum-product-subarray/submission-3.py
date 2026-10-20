class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1

        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                continue
            
            temp = n * curMax

            # n * curMax for cases where n > 0
            # n * curMin for cases where n < 0
            curMax = max(n * curMax, n * curMin, n)

            # use temp to get the pre-updated curMax value
            curMin = min(temp, n * curMin, n)

            res = max(res, curMax)

        return res