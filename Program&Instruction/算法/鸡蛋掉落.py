'''
dp[i][j] = 1 + min( m:1 ~ i max(dp[m - 1][j - 1], dp[i - m][j]) )
i j 固定时
dp[m - 1][j - 1] 随m递增
dp[i - m][j] 随m递减
两者最大值的最小值，即两个函数图像的交点
通过遍历可以找到这个交点，但效率低

考虑f(m) =  dp[m - 1][j - 1] - dp[i - 1][j]
m是一个递增函数，我要找的交点，就是使f(m)在0附件的m值
递增代表有序，那么可以通过二分来寻找
'''
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        if k == 1:
            return n
        if n == 1:
            return 1

        for i in range(1, n + 1):
            dp[i][1] = i
        for i in range(1, k + 1):
            dp[1][i] = 1

        for i in range(1, n + 1):
            for j in range(2, k + 1):
                # 在1 ~ i的哪个点摔鸡蛋 最优
                # left dp[m - 1][k - 1] < dp[i - m][k]
                # right dp[m - 1][k - 1] > dp[i - m][k]
                left = 1
                right = i
                while left < right:
                    mid = left + (right - left) // 2
                    lower = dp[mid - 1][j - 1]
                    higher = dp[i - mid][j]

                    if lower < higher:
                        left = mid + 1
                    elif lower > higher:
                        right = mid
                    else:
                        left = right = mid
                # left : lower >= higher的第一个
                higher_index = left
                lower_index = left - 1
                this = max(dp[higher_index - 1][j - 1], dp[i - higher_index][j])
                pre = max(dp[lower_index - 1][j - 1], dp[i - lower_index][j])
                dp[i][j] = min(pre, this) + 1
        return dp[n][k]