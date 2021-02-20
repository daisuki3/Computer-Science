'''
复杂度: O(N * logN)
稳定性: 不稳定。
从局部看，在建堆或者维护堆时，对于两个相同值的孩子，优先选择下标大的孩子作为堆顶。
从全局看，如果交换上去的孩子在以后的竞争中失败，就可能导致不稳定。
建堆复杂度: O(N)
 0
1 2
left = 2 * i + 1
right = 2 * i + 2
堆状数组
parent = int((i - 1) / 2)
'''

# 建堆 复杂度O(N)
def heapify(nums, end):
    last_parent = int((end - 1) / 2)
    i = last_parent
    while i >= 0:
        max_heap(nums, i, end)
        i -= 1

# 调整堆
def max_heap(nums, index, end):
    i = index
    while i <= end:
        # 寻找左右子中较大者
        left = 2 * i + 1
        right = 2 * i + 2
        big = left

        if right <= end and nums[right] >= nums[left]:
            big = right
        elif left <= end and (right > end or nums[left] > nums[right]):
            big = left
        else:
            break

        if nums[big] > nums[i]:
            swap(nums, big, i)
            i = big
        else:
            break


def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp


def HeapSort(nums):
    n = len(nums)
    j = n - 1
    heapify(nums, n - 1)

    while j >= 1:
        swap(nums, 0, j)
        # 删除复杂度应该为O(logN)
        j -= 1
        max_heap(nums, 0, j)


def main():
    nums = [9,4,5,7,3,4,2,1]
    HeapSort(nums)
    nums1 = [3,6,123,46,24,6,124,62,52,5,1,51,51,123,16,4,1,51,617,5,235,12]
    HeapSort(nums1)
    print(nums)
    print(nums1)


main()