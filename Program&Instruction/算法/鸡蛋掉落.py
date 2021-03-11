'''
dp[i][j] = 1 + min( m:1 ~ i max(dp[m - 1][j - 1], dp[i - m][j]) )

i j 固定时
dp[m - 1][j - 1] 随m递增
dp[i - m][j] 随m递减
m取 1 ~ i时，两者较大值的最小值，即两个函数图像的交点
通过遍历可以找到这个交点，但效率低

考虑f(m) =  dp[m - 1][j - 1] - dp[i - m][j]
m是一个递增函数，我要找的交点，就是使f(m)在0附件的m值
递增代表有序，那么可以通过二分来寻找
'''
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        arr = [[0] * (k + 1) for _ in range(n + 1)]

        # i:楼层数 j:鸡蛋个数
        # 用函数式dp可以减少重复计算，只计算dp数组中自己需要的数据并存储，提高性能
        def dp(i, j):
                # 在1 ~ i的哪个点测试是最优的
                # left dp[m - 1][k - 1] < dp[i - m][k]
                # right dp[m - 1][k - 1] > dp[i - m][k]
            if j == 1:
                return i
            if i <= 1:
                return i

            if arr[i][j] != 0:
                return arr[i][j]

            left = 1
            right = i
            while left < right:
                mid = left + (right - left) // 2
                lower = dp(mid - 1, j - 1)
                higher = dp(i - mid, j)

                if lower < higher:
                    left = mid + 1
                elif lower > higher:
                    right = mid
                else:
                    left = right = mid
                # left : lower >= higher的第一个
            more_equal_index = left
            less_index = left - 1 
            pre = max(dp(less_index - 1, j - 1), dp(i - less_index, j))
            this = max(dp(more_equal_index - 1, j - 1), dp(i - more_equal_index, j))

            arr[i][j] = min(pre, this) + 1

            return arr[i][j]

        return dp(n, k)