'''
复杂度: O(n^2)
稳定性：稳定。插入时只跃过了大于nums[j]的元素，保证了稳定性。
'''
def InsertionSort(nums):
    n = len(nums)
    j = 1

    while j <= n - 1:
        index = j
        for i in range(j - 1, -1, -1):
            if nums[i] <= nums[j]:
                break
            elif nums[i] > nums[j]:
                index = i
        tmp = nums[j]
        for i in range(j, index, -1):
            nums[i] = nums[i - 1]
        nums[index] = tmp

        j += 1
    

def main():
    nums = D
    InsertionSort(nums)
    print(nums)
main()