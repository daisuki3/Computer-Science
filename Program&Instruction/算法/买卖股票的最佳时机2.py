'''
可以进行无数论买卖
还是贪心
因为可以有无数笔
所以最佳卖出时机是递增的最高点
注意边界处理，即最后一天是递增最高点的情况，ans + turn
'''
class Solution:
    def maxProfit(self, prices) -> int:
        ans = 0
        buy_price = prices[0]
        turn = 0
        for p in prices:
            if p - buy_price > turn:
                turn = p - buy_price
            else:
                ans += turn
                buy_price = p
                turn = 0
                
        return ans + turn