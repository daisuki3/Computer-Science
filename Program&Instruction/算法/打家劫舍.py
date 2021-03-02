'''
因为不能打劫相邻房屋
在第i个房屋时，可以选择打劫i - 1，也可以选择i - 2和i，取较大者，dp[n - 1]就是最优解
因为数据初始化需要用到nums[0]和nums[1]，所以注意在开头进行边界处理

和斐波那契数列类似，计算i只需要用到i - 1 和 i - 2，所以空间复杂度可以降低到O(1)
'''
class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])


        return dp[n - 1] 