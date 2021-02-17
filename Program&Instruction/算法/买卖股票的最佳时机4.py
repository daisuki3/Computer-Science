class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        if len(prices) == 0:
            return 0

        dp = [0] + [-prices[0], 0] * k
        i = 1
        while i < len(prices):

            for j in range(1, len(dp)):
                # buy
                if j % 2 == 1:
                   dp[j] = max(dp[j], dp[j - 1] - prices[i])
                # sell
                else:
                    dp[j] = max(dp[j], dp[j - 1] + prices[i])
            
            i += 1
        
        return dp[-1]