class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        if len(s) == 1:
            return 1
    
        res = 0

        # left and right pointer
        l = 0
        r = l + 1

        seen = set()
        seen.add(s[l])
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l = l + 1

            res = max(res, r - l + 1)
            seen.add(s[r])
            r = r + 1

        return res

