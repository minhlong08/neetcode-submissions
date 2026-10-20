class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp bottom up approacg
        # dp[i] be the length of the longest subsequence from index i tp the end
        n = len(nums)
        dp = [1] * n

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(1, dp[i], 1 + dp[j])

        return max(dp)