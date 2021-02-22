'''
常规DFS处理，处理边界情况的处理。

注意到dfs函数有很多重复计算。
例如dfs(2)中递归计算了dfs(7)
可能dfs(4)中也要计算dfs(7)
所以建立 dfs的参数到返回结果 的映射。

def dfs(i):
    if i in dfsmap:
        return dfsmap[i]
    '''
    Code 
    '''
    dfsmap[i] = ans

'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache(None)
        
        
        def dfs(start):
            end = start
            ans = []

            while end < len(s):
                word = s[start : end + 1]
                if word in wordSet:
                    if end == len(s) - 1:
                        return [[word]]
                    else:
                        wordBreaks = dfs(end + 1)
                        for wordBreak in wordBreaks:
                            ans.append([word] + wordBreak)
                end += 1

            return ans

        wordSet = set(wordDict)
        breaks = dfs(0)

        return [" ".join(b) for b in breaks]

        
