class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # initialise res = len(nums) since the range is from 0 to n
        res = len(nums)
        for i, x in enumerate(nums):
            # idea XOR a ^ a == 0, a ^ 0 = a, (a^b)^c = a^(b^c)
            # -> Since the same number cancel out, XOR every element
            # in nums with the indices from 0 to n, the number with is left
            # out will be in our final res variable
            res ^= i^x
        return res