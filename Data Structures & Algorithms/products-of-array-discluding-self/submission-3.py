class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []

        prod = 1
        prefix.append(1)
        for i in range(1, len(nums)):
            prod *= nums[i - 1]
            prefix.append(prod)

        prod = 1
        suffix.append(1)
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i + 1]
            suffix.append(prod)

        suffix.reverse()

        res = [prefix[i] * suffix[i] for i in range(len(nums))]
        return res