class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        
        maxProfit = 0
        l = 0
        for r in range(1, len(prices)):
            profit = prices[r] - prices[l]
            maxProfit = max(maxProfit, profit)

            if prices[r] < prices[l]:
                l = r
        
        return maxProfit
        