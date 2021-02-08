'''
kmp算法
注意在搜索时 i += 1
'''
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        startIndex_OnFail = []
        for i in range(len(t)):
            startIndex_OnFail.append(0)

        for i in range(1, len(t) - 1):
            begin = startIndex_OnFail[i - 1]
            while begin != 0 and t[i] != t[begin]:
                begin = startIndex_OnFail[begin - 1]

            if t[i] == t[begin]:
                startIndex_OnFail[i] = begin + 1
            else:
                startIndex_OnFail[i] = 0
        i = 0
        j = 0
        while i < len(s):

            while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    if j > 0:
                        j = startIndex_OnFail[j - 1]
                    else:
                        i += 1
                else:
                    i += 1
                    j += 1

            if j == len(t):
                return i - len(t)
            else:
                return -1

def main():
    s = Solution()
    print(s.minWindow("abababc", "ababc"))
main()