class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # let dp[i] be the minimum number of coin picked to reach i amount of money
        # Initialise to amount + 1 to identify if amount can be reach
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    # Number of way to reach a mount
                    # = number of way to reach a - c amount + 1
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return dp[amount] if dp[amount] != amount + 1 else -1