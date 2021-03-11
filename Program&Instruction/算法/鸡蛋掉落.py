class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        '''
    高于F的楼层鸡蛋会碎

    最小移动次数
    dp[i][k] = 
    如果碎了 dp[i - 1][k - 1]
    如果没碎 dp[i - 1][k]
    + 1这一次尝试

    dp[i][1] = i

    return dp[i][k]

        '''
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        if k == 1:
            return n
        if n == 1:
            return 1

        for i in range(1, n + 1):
            dp[i][1] = i
        for i in range(1, k + 1):
            dp[1][i] = 1

        for i in range(2, n + 1):
            for j in range(2, k + 1):
    
                # 在1 ~ i的哪个点测试是最优的

                # left dp[m - 1][k - 1] < dp[i - m][k]
                # right dp[m - 1][k - 1] > dp[i - m][k]
                left = 1
                right = i
                while left < right:
                    mid = left + (right - left) // 2
                    lower = dp[mid - 1][k - 1]
                    higher = dp[i - mid][k]

                    if lower < higher:
                        left = mid + 1
                    else:
                        right = mid
                # left : lower >= higher的第一个
                
                pre = max(dp[(left - 1) - 1][k - 1], dp[i - (left - 1)][k])
                this = max(dp[left - 1][k - 1], dp[i - left][k])
                if dp[left - 1][k - 1] < dp[i - left][k]:
                    print("error")
                if dp[(left - 1) - 1][k - 1] >= dp[i - (left - 1)][k]:
                    print("error")

                #print("this expect false", dp[left - 1][k - 1] < dp[i - left][k])
                #print("pre expect true", dp[(left - 1) - 1][k - 1] < dp[i - (left - 1)][k])
                dp[i][j] = min(pre, this) + 1
                '''
                min_v = -1
                for m in range(1, i + 1):
                    #       碎了 在楼下继续找   没碎 在楼上找
                    v = max(dp[m - 1][k - 1], dp[i - m][k])
                    if min_v == -1 or v < min_v:
                        min_v = v 
                dp[i][j] = min_v + 1
                '''
        return dp[n][k]