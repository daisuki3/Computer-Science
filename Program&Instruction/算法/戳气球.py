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