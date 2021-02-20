'''
复杂度: O(n^2)
稳定性：稳定。
因为只会在相邻下标交换，且具有相等关系时不交换，所以是稳定的。
'''
def BubbleSort(nums):
    n = len(nums)
    j = n - 1
    while j > 0:
        for i in range(0, j):
            if nums[i] > nums[i + 1]:
                tmp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = tmp
        
        j -= 1

def main():
    nums = [3,7,10,1,4, 9,8,5,2,6]
    BubbleSort(nums)
    print(nums)
main()