class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        n = len(s)
        hash = {}

        def part(start):
            ans = []
            i = start 
            while i < n:
                sub_s = s[start:i + 1]
                hash_s = str(start) + ":" + str(i + 1)
                if hash_s not in hash and valid(sub_s) == True:   
                    search = part(i + 1)
                    if len(search) == 0:
                        ans.append([sub_s])
                        break
                    else:
                        for se in search:
                            ans.append([sub_s] + se)
                else:
                    hash[hash_s] = False
                i += 1
            return ans

        def valid(ts):
            left = 0
            right = len(ts) - 1
            while left <= right:
                if ts[left] != ts[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            return True

        return part(0)
