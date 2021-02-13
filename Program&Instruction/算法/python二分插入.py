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
            if self.window[mid] <= num:
                self.window = self.window[:mid + 1] + [num] + self.window[mid + 1:]
            elif self.window[mid] > num:
                self.window = self.window[:mid] + [num] + self.window[mid:]