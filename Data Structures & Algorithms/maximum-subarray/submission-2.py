class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curSum, maxSum = 0, nums[0]

        for num in nums:
            # if curSum < 0, start fresh new subarray at the position
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSum = max(maxSum, curSum)

        return maxSum