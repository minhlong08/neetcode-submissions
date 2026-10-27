class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def canFinish(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            
            return hours <= h

        # idea: if we can finish with rate k -> we can finish with rate k + 1
        # the maximum rate is the largest pile, the minimum is 1
        # -> use binary search to find the minimum rate k
        res = max(piles)
        while l <= r:
            m = (l + r) // 2

            if canFinish(m):
                r = m - 1
                res = m
            else:
                l = m + 1

        return res