class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[x][y] be the number of way to reach cell (x,y)

        dp = [[0] * n for _ in range(m)]

        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if 0 <= r - 1 < m:
                    dp[r][c] += dp[r-1][c]

                if 0 <= c - 1 < n:
                    dp[r][c] += dp[r][c-1]

        return dp[m-1][n-1]
        