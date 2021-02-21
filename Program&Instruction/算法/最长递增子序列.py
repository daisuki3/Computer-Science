'''
动态规划秒了
复杂度 时间O(N^2) 空间O(N)
'''

class Solution:
    def lengthOfLIS(self, nums) -> int:
        dp = []

        for i in range(0, len(nums), 1):
            dp.append(1)
            
            maxV = 1
            
            j = i - 1
            while j >= 0:
                if nums[i] > nums[j] and dp[j] + 1 > maxV:
                    maxV = dp[j] + 1
                j -= 1

            dp[i] = maxV

        return dp[len(nums) - 1]