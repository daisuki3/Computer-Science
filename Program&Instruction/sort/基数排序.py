'''
复杂度：时间O(N * K) 空间
稳定性：稳定。
值相同元素优先选择下标小的入桶，所以是稳定的。
'''
import math
def RadixSort(nums, radix):
    n = len(nums)
    k = int(math.log(max(nums), radix))

    for m in range(k + 1):
        bucket = [[] for _ in range(radix)]
        for i in range(n):
            #启发，对于radix=10 673 第一轮 nums[i] % 10 第二轮 (nums[i]/radix) % radix
            bucket[int(nums[i]/(radix ** m)) % radix].append(nums[i])
    
        nums = []
        #print(bucket)
        for i in range(radix):
            nums += bucket[i]
    return nums
def main():
    nums = [9, 4, 5, 7, 3, 4, 2, 1]
    nums1 = [3, 6, 123, 46, 24, 6, 124, 62, 52, 5, 1, 51, 51, 123, 16, 4, 1, 51, 617, 5, 235, 12]

    print(RadixSort(nums, 10))
    print(RadixSort(nums1, 10))


main()