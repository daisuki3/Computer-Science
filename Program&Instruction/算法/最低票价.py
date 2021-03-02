'''
思考最低票价的获得，在买票时，考虑以后几天会不会出游，来购买1天，7天，或者30天票。
所以很明显是动态规划。
但是怎么规划？每次去找之后几天的出游计划？太笨了！

dp数组从后往前遍历，dp[i]表示从第i天到第365天需要多少钱。
dp[i] = min(dp[i + duration] + cost for duration, cost in zip(durations, costs))

边界处理：在365时可能会用到更靠后的天数信息，所以开一个大一点的dp数组，再后面的取0就行了。
''' 
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (366 + 30) 
        dayset = set(days)
        durations = [1, 7, 30]

        for i in range(365, 0, -1):
            if i in dayset:
                dp[i] = min(dp[i + duration] + cost for duration, cost in zip(durations, costs))
                '''
                minV = dp[i + 1] + costs[0]
                minV = min(minV, dp[i + 7] + costs[1])
                minV = min(minV, dp[i + 30] + costs[2])    
                dp[i] = minV
                '''
            else:
                dp[i] = dp[i + 1]
        
        return dp[1]