class Solution:
    def rob(self, nums: List[int]) -> int:
        # let dp[i] be the maximum amount of money can rob up to and including house[i]
        # break up the circle by using 2 array
        # array1: include the 1st house but remove the last
        # array2: remove the 1st house but include the last
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])

        
        dp1 = [0] * (len(nums) - 1)
        dp2 = [0] * (len(nums) - 1)

        # house from index 0 to index n - 2
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])

        # house from index 1 to index n - 1
        dp2[0] = nums[1]
        dp2[1] = max(nums[1], nums[2])

        for i in range(2, len(nums) - 1):
            dp1[i] = max(nums[i] + dp1[i-2], dp1[i-1])

        for i in range(2, len(nums) - 1):
            dp2[i] = max(nums[i + 1] + dp2[i-2], dp2[i-1])

        return max(dp1[-1],dp2[-1])
        