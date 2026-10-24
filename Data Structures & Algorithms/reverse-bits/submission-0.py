class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        count = 0
        while n and count <= 31:
            curBit = n & 1
            res = res | (curBit << (31 - count))
            count += 1
            n = n >> 1

        return res