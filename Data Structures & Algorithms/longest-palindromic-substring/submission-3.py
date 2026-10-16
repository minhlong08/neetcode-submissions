class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] be if from index i to j (s[i:j+1]) is a palindrome
        resIdx, resLen = 0,0
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n-1, -1, -1):
            for j in range(i,n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if j - i + 1 > resLen:
                        resLen = j - i + 1
                        resIdx = i

        return s[resIdx: resIdx + resLen]