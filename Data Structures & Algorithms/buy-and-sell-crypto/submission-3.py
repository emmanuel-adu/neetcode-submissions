class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        right = 1

        while right < len(prices):
            # goal we want to buy low sell
# You've discovered a better day to buy.

# Instead of moving left by one position, think about which index already points to that cheaper price.

# That's the index that should become your new buying day.
            if prices[left] > prices[right]:
                # avoid negative profit
                left += 1
                # right += 1
            else:
                # positive profit
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
                right += 1
        
        return max_profit
