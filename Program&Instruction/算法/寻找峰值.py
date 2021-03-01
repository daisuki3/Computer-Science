'''
半峰：至少比一端大

左右两端点都是半峰，进行二分查找，过程中始终保证left和right都是半峰，结束时较大者为峰值
'''

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right - 1:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif mid - 1 >= 0 and nums[mid - 1] > nums[mid]:
                right = mid - 1
            elif nums[mid + 1] > nums[mid]:
                left = mid + 1
        
        if nums[left] > nums[right]:
            return left
        else:
            return right