'''
复杂度：平均O(n * logn) 最坏，当每次pivot都是最值时达到，O(n^2)

稳定性：只要left和right行走时跳过nums[i] == pivot的元素。就可以保证稳定性。
错了。只是保证了pivot这个元素是稳定的。
例如 [2,  7,  3,  3,  5] pivot为5
        left    right
这时交换7和3的位置，就会破坏元素3的稳定性。
'''

def quickSort(nums):
    qSort(nums, 0, len(nums) - 1)

def qSort(nums, start, end):
    pivot = getPivot(nums, start, end)

    if end - start <= 2:
        return
    else:
        left = start
        right = end

        while left < right:
            # 交换完后分别 +1 -1 避免无限交换
            left += 1
            right -= 1
            while nums[left] <= pivot and left < end:
                left += 1
            while nums[right] >= pivot and right > 0:
                right -= 1
            if left < right:
                swap(nums, left, right)

        # 因为nums[left] > pivot
        qSort(nums, start, left - 1)
        qSort(nums, left, end)

def getPivot(nums, left, right):
    mid = int(left + (right - left) / 2)
    if nums[left] > nums[mid]:
        swap(nums, left, mid)
    if nums[mid] > nums[right]:
        swap(nums, mid, right)
    if nums[left] > nums[mid]:
        swap(nums, left, mid)
    return nums[mid]

def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp

def main():
    nums = [3,7,10,1,4, 9,8,5,2,6]
    quickSort(nums)
    print(nums)

main()