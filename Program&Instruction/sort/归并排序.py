'''
复杂度: 时间O(N*logN) 空间O(N)
稳定性：归并时，碰到相等的情况优先选择下标在前的元素，可以保证稳定性
'''
def MSort(nums, start, end):
    if start == end:
        return 
    mid = start + int((end - start) / 2)
    MSort(nums, start, mid)
    MSort(nums, mid + 1, end)

    tmp = []

    p1 = start
    p2 = mid + 1
    while p1 <= mid and p2 <= end:
        if nums[p1] <= nums[p2]:
            tmp.append(nums[p1])
            p1 += 1
        elif nums[p1] > nums[p2]:
            tmp.append(nums[p2])
            p2 += 1
    
    while p1 <= mid:
        tmp.append(nums[p1])
        p1 += 1
    while p2 <= end:
        tmp.append(nums[p2])
        p2 += 1
    
    for i in range(start, end + 1, 1):
        nums[i] = tmp[i - start]

def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp


def MergeSort(nums):
    n = len(nums)    
    MSort(nums, 0, n - 1)


def main():
    nums = [9,4,5,7,3,4,2,1]
    MergeSort(nums)
    nums1 = [3,6,123,46,24,6,124,62,52,5,1,51,51,123,16,4,1,51,617,5,235,12]
    MergeSort(nums1)
    print(nums)
    print(nums1)


main()