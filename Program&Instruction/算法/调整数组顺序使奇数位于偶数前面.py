'''
维护一个奇数下标oddIndex
发现奇数则交换到该下标
碰到奇数且i == oddIndex表明该位置已经属于奇数，oddIndex + 1
就可以确信i > oddIndex时,num[oddIndex] % 2 == 0
'''
class Solution:
    def exchange(self, nums):
        oddIndex = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                if i != oddIndex:
                    tmp = nums[i]
                    nums[i] = nums[oddIndex]
                    nums[oddIndex] = tmp
                oddIndex += 1

        return nums