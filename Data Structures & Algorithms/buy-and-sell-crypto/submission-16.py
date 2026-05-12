class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_p = 0
        for i in range(0, len(prices)):
            k = prices[i]
            for j in range(i+1, len(prices)):
                if (prices[j] - k) > max_p:
                    max_p = prices[j] - k

        return max_p   
        