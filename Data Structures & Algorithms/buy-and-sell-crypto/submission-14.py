class Solution:
    def maxProfit(self, prices: List[int]) -> int: #[3, 4, 1, 3]
        maxP = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[r] - prices[l] <= 0:
                l += 1
                if maxP != 0:
                    l = r
                continue
            else:
                maxP = max(maxP, prices[r] - prices[l])
        return maxP
                
         
            
        



