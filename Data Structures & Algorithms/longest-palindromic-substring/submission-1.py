class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        maxLen = 1
        res = s[0]

        for i in range(len(s)):
            # for each index i assume that it is the center of the palindrome and try to extend outward

            # case 1: odd length palindrome
            l,r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    res = s[l:r+1]
                l = l - 1
                r = r + 1

            #case 2: even length palindrome
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    res = s[l:r+1]
                l = l - 1
                r = r + 1


        return res
