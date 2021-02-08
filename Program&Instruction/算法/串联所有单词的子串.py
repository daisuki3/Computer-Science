'''
0 ~ len(s) - total_length都有可能是符合条件的子串的起点
对于每个起点维护一个remain字典，存储可用的单词数量
在检测起点的合法性时，更新字典值（-1），不合条件（不存在，或者为remain[word] == 0）立即退出.
一次走unit_length。
时间复杂度 n * len(words)
空间复杂度 len(words)
'''
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or len(words) == 0:
            return []
        unit_length = len(words[0])
        total_length = unit_length * len(words)

        ans = []

        for i in range(0, len(s) - total_length + 1):
            j = i
            remain = {}
            for w in words:
                remain[w] = remain.get(w, 0) + 1

            while True:
                ok = False
                w = s[j: j + unit_length]
                if remain.get(w, -1) != -1 and remain[w] > 0:
                    remain[w] -= 1
                    ok = True

                if ok == True:
                    j += unit_length
                    if j - total_length == i:
                        ans.append(i)
                        break
                else:
                    break
        
        return ans
