'''
                上一天买的        今天才买
buy[i][j] = max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i]) 
在第i天恰好第j次买入的最大利润
                上一天卖的          今天才卖
sell[i][j] = max(sell[i - 1][j], buy[i - 1][j] + prices[i]) 
在第i天恰好第j次卖出的最大利润

边界：
如何处理第一维的i - 1 给i == 0单独设置值 buy[0][i] = -prices[0] sell[0][i] = 0
如何处理第二维的j - 1 给j == 0单独设置值 buy and sell[i][0]都设置为0
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n == 0:
            return 0
        buy = [[0] * (k + 1) for _ in range(n)]
        sell = [[0] * (k + 1) for _ in range(n)]

        for i in range(k + 1):
            buy[0][i] = -prices[0]
            sell[0][i] = 0

        i = 1
        while i < n:
            buy[i][0] = 0
            sell[i][0] = 0
            j = 1
            while j <= k:
                buy[i][j] = max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i])
                sell[i][j] = max(sell[i - 1][j], buy[i - 1][j] + prices[i])
                j +=1
        
            i += 1

        return max(sell[n - 1])
'''
'''
如何把dp数组从二维降到一维？    
        
buy[j] = max(buy[j], sell[j - 1] - prices[i])
       = max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i], buy[i - 1][j - 1])
       = max(buy[i - 1][j], sell[i - 1][j - 1] - prices[i])
       
sell[j] = max(sell[j], buy[j] + prices[i])
        = max(sell[i - 1][j], buy[i - 1][j] + prices[i], 
        sell[i - 1][j - 1] - prices[i] + prices[i])
'''
class Solution:
    def maxProfit(self, k: int, prices) -> int:
        
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