class Solution:
    def maxProfit(self, prices: List[int]) -> int: #[3, 4, 1, 3]
        mini = prices[0]
        profit = 0
        for i in range(len(prices)):
            if prices[i] < mini:
                mini = prices[i]
            elif prices[i] > mini:
                profit = max((prices[i] - mini), profit)
        return profit
                
         
            
        



