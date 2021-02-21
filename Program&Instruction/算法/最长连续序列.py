class Solution:
    def longestConsecutive(self, nums) -> int:
        '''
        排序时间复杂度O(n*ogn)
        得到n组连续序列
        
        时间O(n)的算法肯定是只得到一组最长的连续序列
        '''
        ans = 0
        UFS = UnionFindSet()
        for num in nums:

            if UFS.find(num) != "x":
                continue
            pre = UFS.find(num - 1)
            post = UFS.find(num + 1)
            UFS.add(num)
            if pre != "x" and post != "x":
                UFS.union(num, num - 1)
                UFS.union(num + 1, num - 1)
            elif pre != "x":
                UFS.union(num, num - 1)
            elif post != "x":
                UFS.union(num + 1, num)

        return UFS.biggest_family()


class UnionFindSet:

    def __init__(self):
        self.parent_dict = {}
        self.family_num = {}

    def add(self, num):
        self.parent_dict[num] = num
        self.family_num[num] = 1

    def union(self, a, b):
        if self.parent_dict[a] != self.parent_dict[b]:
            a_parent = self.find(a)
            b_parent = self.find(b)
            self.parent_dict[a_parent] = b_parent
            self.family_num[b_parent] += self.family_num[a_parent]
            del self.family_num[a_parent]

    def find(self, num):
        # 不存在
        if num not in self.parent_dict:
            return "x"

        parent = self.parent_dict[num]
        # 不是集合的根
        if parent != self.parent_dict[parent]:
            self.parent_dict[parent] = self.find(parent)
            self.parent_dict[num] = self.parent_dict[parent]
            return self.parent_dict[num]
        else:
            return parent

    def biggest_family(self):
        max = 0
        for f in self.family_num:
            # print("%d num : %d" %(f, self.family_num[f]))
            if self.family_num[f] > max:
                max = self.family_num[f]

        return max