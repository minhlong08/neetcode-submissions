class Solution:
    def countOnes(self, n:int) -> int:
        count = 0
        while n:
            if n & 0x01:
                count += 1
            n = n >> 1

        return count

    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(0, n + 1):
            res.append(self.countOnes(i))
        return res