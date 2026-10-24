class Solution:
    def hammingWeight(self, n: int) -> int:
        mask = 1
        count = 0
        while n:
            if n & mask:
                count += 1
            n = n >> 1

        return count