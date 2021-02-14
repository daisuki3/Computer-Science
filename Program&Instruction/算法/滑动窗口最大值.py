class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        维护长度为k的单调增数组，移动窗口时，删除出窗元素，新元素二分插入
        删除橱窗元素复杂度是O(k),二分插入O(logK)其实意义并不大
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
        '''

        '''
        为什么要维护一个单调增的长度k数组？
        为了移除出窗元素时O(1)得到顶替元素!
        注意最大值这个条件是很强的，意味着一个数入窗后，
        目前窗内所有比它小的元素都不再有最大值的机会。
        所以其实不需要单调增的k数组，
        我需要的只是一个顶替队列，这个顶替队列不需要长度k单调增。
        考虑单调减的双端队列，num入窗时移除所有比它小的元素。
        队首就是窗口内的最大值。
        '''
        ans = []
        deque = collections.deque()
        for i in range(0, k, 1):
            while len(deque) != 0 and nums[deque[-1]] <= nums[i]:
                deque.pop()
            deque.append(i)
        ans.append(nums[deque[0]])

        for i in range(k, len(nums), 1):
            while len(deque) != 0 and nums[deque[-1]] <= nums[i]:
                deque.pop()
            deque.append(i)
            if deque[0] == i - k:
                deque.popleft()
            ans.append(nums[deque[0]])
        
        return ans