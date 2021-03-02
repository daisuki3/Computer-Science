'''
加入了限制条件，不能同时打劫第一个和最后一个
思路：转换为两个打家劫舍问题
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        def r(nums):
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

        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        else:
            return max(r(nums[:-1]), r(nums[1:]))