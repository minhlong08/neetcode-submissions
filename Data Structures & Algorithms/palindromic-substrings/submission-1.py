class Solution:
    def countSubstrings(self, s: str) -> int:
        # 2 pointers approach
        res = 0

        for i in range(len(s)):
            # odd length palindrome
            l, r = i, i
            while l >=0 and r < len(s) and s[l] == s[r]:
                res += 1 # increase the count
                l = l - 1
                r = r + 1

            # even length palindrome
            l, r = i, i + 1
            while l >=0 and r < len(s) and s[l] == s[r]:
                res += 1 # increase the count
                l = l - 1
                r = r + 1

        return res
