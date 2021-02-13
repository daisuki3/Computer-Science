class Solution:
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        暴力方法只能过47/60个样例
        '''
        n = len(nums)
        ans = [-sys.maxsize - 1] * (n - k + 1) 
        
        self.window = []
        for i in range(0, k, 1):
            self.insert(nums[i])
        ans[0] = self.window[-1]
        for i in range(k, n, 1):
            self.window.remove(nums[i - k])
            self.insert(nums[i])
            ans[i - k + 1] = self.window[-1]
        
        return ans
    

    def insert(self, num):
        start = 0
        end = len(self.window) - 1
        mid = 0

        if end == -1:
            self.window.append(num)
        else:
            while start < end:
                mid = int(start + (end - start) / 2)
                if self.window[mid] < num:
                    start = mid + 1
                elif self.window[mid] > num:
                    end = mid - 1
                else:
                    break 
            mid = start
            print(mid)
            if self.window[mid] <= num:
                self.window = self.window[:mid + 1] + [num] + self.window[mid + 1:]
            elif self.window[mid] > num:
                self.window = self.window[:mid] + [num] + self.window[mid:]
        print(self.window)