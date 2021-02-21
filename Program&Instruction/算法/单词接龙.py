'''
暴力思路：深度优先搜索，从endWord开始，遍历wordList找可以替换的单词。
递归寻找，直到能转换为beginWord。
即使是小规模数据也有可能会超时。


广度优先搜索+最短路：这样理解，单词a，b之间有边如果a和b只差一个字母。
那么原题的意思就是找beginWord到endWord的最短路。
怎么初始化这个图是一个问题。

暴力做法O(N^2)对每个单词都遍历数组找邻点。
换一种思路。比如"hot"连接到 "*ot" "h*t" "ho*" 
这样也可以形成一条路径，只不过长度是原来的两倍。
ans = distance[endWord] // 2 + 1

怎么初始化、存储这个数据结构也是个问题。
很显然的思路是edge[word]为一个数组，里面存了相邻单词。
以下代码就是这样做的，明显缺点是edge字典太大了。
可以考虑做一个单词到id的映射，edge存id，减少空间的使用。
'''

import queue
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        def addEdge(word):
            nonlocal edge

            chars = list(word)
            if word not in edge:
                edge[word] = []

            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = '*'
                newWord = "".join(chars)

                if newWord not in edge:
                    edge[newWord] = []
                
                edge[newWord].append(word)
                edge[word].append(newWord) 
                chars[i] = tmp

        edge = dict()
        distance = dict()

        for w in wordList:
            addEdge(w)
            distance[w] = -1

        addEdge(beginWord)
        distance[beginWord] = 0
        q = queue.Queue()
        q.put(beginWord)
        while q.empty() == False:
            w = q.get()
            if w == endWord:
                return distance[endWord] // 2 + 1
            
            d = distance[w]
            for neiborW in edge[w]:
                
                if neiborW not in distance:
                    distance[neiborW] = -1

                if distance[neiborW] == -1:
                    distance[neiborW] = d + 1
                    q.put(neiborW)
        return 0
            