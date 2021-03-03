'''
暴力思路
枚举s1所有的排列，到s2中去找

排列即字符集相等，长度相等
暴力检查s2中所有长度为n的子串
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def compare(h1, h2):
            for s in s1:
                if s not in h2 or h1[s] != h2[s]:
                    return False
            return True

        n = len(s1)
        if n > len(s2):
            return False
            
        s1_hash = {}
        s2_hash = {}
        for i in range(n):
            if s1[i] in s1_hash:
                s1_hash[s1[i]] += 1
            else:
                s1_hash[s1[i]] = 1

            if s2[i] in s2_hash:
                s2_hash[s2[i]] += 1
            else:
                s2_hash[s2[i]] = 1
        
        if compare(s1_hash, s2_hash) == True:
            return True
        
        for i in range(n, len(s2)):
            s2_hash[s2[i - n]] -= 1
            if s2[i] in s2_hash:
                s2_hash[s2[i]] += 1
            else:
                s2_hash[s2[i]] = 1    

            if compare(s1_hash, s2_hash) == True:
                return True
        
        return False