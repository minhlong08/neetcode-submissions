class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        lowest_buy = prices[0]

        for p in prices:
            profit = p - lowest_buy
            
            if profit > max_profit:
                max_profit = profit
            
            if p < lowest_buy:
                lowest_buy = p
        return max_profit