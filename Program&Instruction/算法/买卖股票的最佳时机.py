'''
只能进行一次买卖

这个求最值可以用贪心算法来做
最佳卖出时机是，随着时间迁移，股票价格低于买入价格之前，的最高价格
价格低于买入价格后，开启新一轮贪心
因为只能进行一轮买卖，所以求每一轮贪心的最大值
'''

class Solution:
    def maxProfit(self, prices) -> int:
        ans = 0
        but_price = prices[0]

        for p in prices:
            if p - but_price > ans:
                ans = p -but_price
            elif p < but_price:
                but_price = p

        return ans