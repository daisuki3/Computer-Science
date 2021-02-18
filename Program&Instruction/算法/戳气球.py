'''
戳破一个气球后，会使本不相邻的气球相邻，用普通的DP很难处理。
采取反向的思路，向nums中添加气球。
dp[i][j]为向区间(i, j)中添加第一个气球能得到的最大值
dp[i][j] = max(k in [i+1, j-1]) dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j]

      j
    0 1 2 
  i 1 
    2
现在确定dp顺序
(k in [i+1, j-1])
根据dp[i][k]可以确定是从左往右
根据dp[k][j]可以确定是从下往上

边界：
因为是开区间，所以要得到添加完所有气球的最优解，还需要手动添加左右边界。
'''
class Solution:
    def maxCoins(self, nums) -> int:
        if len(nums) == 0:
            return 0

        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        '''
        dp[i][j] = max(chose in [i + 1, j - 1]) nums[i] * nums[j] * nums[chose] 
        (i < j - 1)
        '''

        i = n - 3
        while i >= 0:

            dp[i][i] = 0
            dp[i][i + 1] = 0
            j = i + 2

            while j < n:
                max_val = 0

                for k in range(i + 1, j):
                    val = dp[i][k] + nums[i] * nums[k] * nums[j] + dp[k][j]
                    if val > max_val:
                        max_val = val

                dp[i][j] = max_val
                j += 1

            i -= 1

        return dp[0][n - 1]