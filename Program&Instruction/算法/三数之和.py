'''
排序+双指针的常规思路
比较麻烦的是细节处理，答案中不能有重复数对(a, b, c)

与其煞费苦心地对数对(a,b,c)排序使a <= b <= c，并维护集合。
不如自己处理，使得可能加入答案的数对(a, b, c)不可能已经存在于答案中。
我们可以这样假定 nums[i]（遍历的i） <= nums[left] <= nums[right]（双指针）
nums[i] == nums[i - 1]和 nums[left] == nums[left - 1]做continue处理。
这样可能加入ans的数对就不可能是重复的。不必再自己筛选。

在leetcode上跑，效率大概是原来的十倍。
'''
class Solution:
    def threeSum(self, nums):
        nums.sort()

        ans = []

        for i in range(0, len(nums), 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            num = nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:

                s = nums[left] + nums[right] + num
            
                if s == 0:
                    # -4 -1 -1 0 1 2
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while left <= len(nums) - 1 and nums[left - 1] == nums[left]:
                        left += 1 

                elif s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
             
        return list(ans)