        '''

        # time n * logn的代码
        num = 1
        if nums[i] == num:
            num += 1
        else:
            return num
        
        # space n 的代码
        dic = {}
        for i in range(len(nums)):
            if dic[i] == 0:
                return i

        return len(nums)

        检测丢失
        空间n的话可以存储
        时间n * logn的话可以排序
        如果时间n 空间1 呢？
        空间n其实可以找到缺失的所有正整数，我们要找的只是第一个
        
        不妨假设，如果没有缺失的正数，数组是什么样的？
        1 ~ N 分别填充在 下标 0 ~ N - 1
        所以我们只需要把每个数字归位，再遍历数组，第一个不合法的下标就是缺失的第一个正数的位置。
        注意，归位是需要交换数字，不处理的话，交换后可能有数字失去归位的机会。
        所以需要用一个循环来归位，保证每个合法数字都回到自己的位置。
        '''
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # a 对应下标 a - 1
        if len(nums) == 0:
            return 1
        for k in range(2):
            for i in range(len(nums)):
                correctIndex = nums[i] - 1
                while correctIndex != i and correctIndex >= 0 and correctIndex < len(nums) and nums[correctIndex] - 1 != correctIndex:
                    tmp = nums[correctIndex]
                    nums[correctIndex] = nums[i]
                    nums[i] = tmp
                    correctIndex = nums[i] - 1

        for i in range(len(nums)):
            correctNum = i + 1
            if nums[i] != correctNum:
                return correctNum

        return len(nums) + 1
                
                
