'''
贪心法，尽量先用大额钱，可能导致本来能凑齐的无法凑齐。
因为不能无脑取大额，那能不能无脑取小额？
不能，因为要求最小数量。
那就先用尽量多的小额，再用大面额来替代。

dp[i] = min(dp[i - c] + 1, dp[i]) or dp[i - c] + 1
用更大的钱来代替几张小钱
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0 and dp[i - c] != -1:
                    dp[i] = min(dp[i], dp[i - c] + 1) if dp[i] != -1 else dp[i - c ] + 1

        return dp[amount]