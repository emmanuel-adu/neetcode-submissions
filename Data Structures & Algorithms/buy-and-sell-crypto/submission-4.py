class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max profit = buy low, sell high
        max_profit = 0
        n = len(prices)

        # i = [7,1,5,3,6,4]
        # j = [1,5,3,6,4]
        for i in range(n):
            profit = 0
            for j in range(i + 1, n):
                profit = prices[j] - prices[i] 
                max_profit = max(profit, max_profit)
        return max_profit