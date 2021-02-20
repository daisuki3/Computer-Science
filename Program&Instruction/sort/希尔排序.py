'''
复杂度: 时间 O(N ^(1.3 ~ 2)) 依赖gap序列的选择
稳定性：不稳定。
带gap的插入排序，在插入时不会考虑数组中前方的所有元素，造成稳定性的丢失。
'''

# 带步长的插入排序
def ShellSort(nums):
    n = len(nums)
    gap = int(n)

    while gap >= 1:
        i = gap
        while i < n:
            index = i
            tmp = nums[i]

            # 找到插入坐标
            j = i - gap
            while j >= 0:
                if nums[j] <= tmp:
                    break
                else:
                    index = j
                j -= gap

            # 进行插入
            for k in range(i, index, -gap):
                nums[k] = nums[k - gap]
            nums[index] = tmp

            i += gap
        gap = int(gap / 2)


def main():
    nums = [9, 4, 5, 7, 3, 4, 2, 1]
    ShellSort(nums)
    nums1 = [3, 6, 123, 46, 24, 6, 124, 62, 52, 5, 1, 51, 51, 123, 16, 4, 1, 51, 617, 5, 235, 12]
    ShellSort(nums1)
    print(nums)
    print(nums1)


main()