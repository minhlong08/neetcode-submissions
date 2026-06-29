class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while (n):
            if n & 0x01:
                count += 1
            n = n >> 1

        return count
        