class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        maxf = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]]) # optimise the process of finding the highest frequent letter
            
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l = l + 1

            res = max(r - l + 1, res)


        return res