'''
双指针
维护一个字典，表示双指针中还需要抵消的T字符
右指针遍历S减少字典值（可以为负数）
左指针遍历S增加字典值
当字典值全小于0代表双指针内部覆盖了子串

这个方法不能通过LeetCode上最后一个超长样例（超时）
需要一点优化
不要dic[s[right]] == 0去检查双指针了是否覆盖
用一个count来计算已经覆盖了的子串长度 count满了再去左移左指针
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == 0:
            return ""

        dic = {}
        for c in t:
            dic[c] = dic.get(c, 0) + 1

        matchCount = 0
        ans_l = 0
        ans_r = len(s)
        left = 0
        right = 0

        while right < len(s):
            if s[right] in dic:
                dic[s[right]] -= 1
                if dic[s[right]] >= 0:
                    matchCount += 1
                if matchCount == len(t):
                    while True:
                        if right - left + 1 < ans_r - ans_l + 1:
                            ans_l = left
                            ans_r = right
                        if s[left] in dic:
                            dic[s[left]] += 1
                            if dic[s[left]] == 1:
                                left += 1
                                matchCount -= 1
                                break
                        left += 1

            right += 1            

        if ans_r < len(s):
            return s[ans_l : ans_r + 1]
        else:
            return ""