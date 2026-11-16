class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            d[num] = i

        for i, num in enumerate(nums):
            remain = target - num

            if remain in d and d[remain] != i:
                return [i,d[remain]]

        return []