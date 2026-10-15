class Solution:
    def rob(self, nums: List[int]) -> int:
        # let dp[i] be the maximum amount of money u can rob up to house i
        if len(nums) < 2:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            # Option 1: rob this house
            opt1 = nums[i] + dp[i - 2]
            # Option 2: don't rob this house
            opt2 = dp[i - 1]

            dp[i] = max(opt1, opt2)

        return dp[len(nums) - 1]