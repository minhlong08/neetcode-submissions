class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        max_profit = 0
        l = 0
        r = l + 1
        while r < len(prices):
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)
            if prices[r] < prices[l]:
                l = r
            r = r + 1
        return max_profit 