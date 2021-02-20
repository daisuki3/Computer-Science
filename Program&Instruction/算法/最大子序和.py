'''
连续子数组的最大和

解法：前缀和，注意变量初始化，以及边界情况的处理
时间复杂度：O(N)
'''
class Solution:
    def maxSubArray(self, nums):
        if len(nums) == 0:
            return 0

        s = 0
        ans = -(10 ** 5)
        minS = 0
        
        for i in range(0, len(nums), 1):
            s += nums[i]
            
            if s - minS > ans:
                ans = s - minS
            
            if s < minS:
                minS = s
        
        return ans
        