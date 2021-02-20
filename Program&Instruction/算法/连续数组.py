'''
0和1数量相等的最长子区间

暴力法是枚举所有的区间，时间O(n^2)

前缀和思想：count代表当前[0,i]中1比0多几个。
那么如果两个下标的count值相等，说明它们之间0和1的数量是相等的
'''
class Solution:
    def findMaxLength(self, nums):
        countHash = {0:-1}
        
        count = 0
        ans = 0
        for i in range(0, len(nums)):
            if nums[i] == 1:
                count += 1
            elif nums[i] == 0:
                count -= 1

            if count not in countHash:
                countHash[count] = i  
            else:
                if i - countHash[count] + 1 > ans:
                    ans = i - countHash[count]
        
        return ans