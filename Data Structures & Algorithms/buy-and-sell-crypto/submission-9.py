class Solution:
    def maxProfit(self, prices: List[int]) -> int: #[3, 4, 1, 3]
        mini = prices[0] # 10 > 1
        profit = 0 # max - mini
        for i in range(len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            elif prices[i] > mini:
                current = prices[i] - mini
                profit = max(current, profit)
        return profit
            
                
         
            
        



