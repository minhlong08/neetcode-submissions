class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = set(nums)
        res = 0
        for num in nums:
            if num - 1 in s:
                continue
            seq = 1
            next_num = num + 1
            while next_num in s:
                next_num += 1
                seq += 1
            res = max(res,seq)

        return res
