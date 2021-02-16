class Solution:
    def maxProfit(self, prices) -> int:
        buy_price = prices[0]
        turns = [0] * 2
        '''
        得到两笔最赚的交易
        '''
        turn = 0
        i = 1
        p = 0
        while i <= len(prices):
            if i < len(prices):
                p = prices[i]

            if p - buy_price > turn:
                turn = p - buy_price
            elif p - buy_price <= turn or i == len(prices):
                if turn > turns[0]:
                    index = len(turns)
                    for j in range(1, len(turns)):
                        if turns[j] > turn:
                            index = j
                            break
                    turns.insert(index, turn)
                    turns = turns[1:]
                buy_price = p
                turn = 0
            i += 1
        return sum(turns)