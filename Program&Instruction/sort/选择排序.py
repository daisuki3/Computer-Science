'''
复杂度：O(n^2)
稳定性：不稳定。
从找到的值看，每次找最小值时，都是选择第一个最小值，所以维护了稳定性。
但是被交换的值，稳定性可能会丢失。
'''
def SelectionSort(nums):
    j = 0
    n = len(nums)
    while j <= n - 2:
        minI = j
        for i in range(j + 1, n):
            minI = i if nums[i] < nums[minI] else minI

        tmp = nums[j]
        nums[j] = nums[minI]
        nums[minI] = tmp
        j += 1
    

def main():
    nums = [3,7,10,1,4, 9,8,5,2,6]
    SelectionSort(nums)
    print(nums)
main()