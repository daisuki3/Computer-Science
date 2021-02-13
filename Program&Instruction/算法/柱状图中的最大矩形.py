class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int: 

        '''
            暴力做法，对于每个height[i]直接遍历查找左界和右界
            short =  heights[i]
            
            right = i + 1
            while right < len(heights) and heights[right] >= short:
                right += 1
            left = i - 1
            while left >= 0 and heights[left] >= short:
                left -= 1


            area = ((right - 1) - (left + 1) + 1) * short
            if area > ans:
                ans = area
        '''
        '''
        
        暴力遍历时，考虑i 和 i + 1
        所谓i的左边界就是左边第一个小于heights[i]的heights[small]
        如果heights[i] == heights[i + 1]，那么左边界是一样的
        如果heights[i] > heights[i + 1]，那么heights[i + 1]的左边界肯定在heights[i]的左边界的左边
        如果heights[i] < heights[i + 1]，那么左边界就是i
        所以我们完全可以根据i的左边界来获取i + 1的左边界
        

        对于右边界的处理也是一样的
        遍历两次得到每个heights[i]的左界和右界

        ans = 0

        n = len(heights)
        left, right = [0] * n, [0] * n

        mono_stack  = []
        for i in range(0, n, 1):
            while len(mono_stack) != 0 and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()

            if len(mono_stack) == 0:
                left[i] = -1
            else:
                left[i] = mono_stack[-1]
            
            mono_stack.append(i)

        mono_stack = []
        for i in range(n - 1, -1, -1):
            while len(mono_stack) != 0 and heights[mono_stack[-1]] >= heights[i]:
                mono_stack.pop()

            if len(mono_stack) == 0:
                right[i] = n
            else:
                right[i] = mono_stack[-1]

            mono_stack.append(i)

        for i in range(0, n, 1):
            if (right[i] - left[i] - 1) * heights[i] > ans:
                ans = (right[i] - left[i] - 1) * heights[i]
        return ans
        '''

        '''
        上一个方法，我用left和right数组来存heights[i]的左右边界，还对heights数组进行了正反两次遍历
        然而当我仔细思考mono_stack里面存的到底是什么东西。我发现left和right数组并不是必要的。
        
        当我准备将heights[i]压入mono_stack时，首先进行一系列出栈，以使mono_stack单调递增。
        出栈结束时，mono_stack[-1]就是heights[i]的左边界!
        意思就是mono_stack[i - 1]是mono_stack[i]的左边界！
        右边界呢？加入heights[i]时要出栈，因为出栈元素大于heights[i]，所以出栈时的heights[i]就是右边界！
        '''
        ans = 0
        
        n = len(heights)
        mono_stack = [-1]

        for i in range(0, n, 1):
            if len(mono_stack) == 0 or heights[i] >= heights[mono_stack[-1]]:
                mono_stack.append(i)
            else:
                smaller_index = 0
                for j in range(len(mono_stack) - 1, -1, -1):
                    if j == 0 or heights[mono_stack[j]] < heights[i]:
                        smaller_index = j
                        break

                for j in range(smaller_index, len(mono_stack), 1):
                    area = heights[mono_stack[j]] * ((i - 1) - (mono_stack[j - 1] + 1) + 1) 
                    ans = area if area > ans else ans 
                    
                mono_stack = mono_stack[0 : smaller_index + 1]
                mono_stack.append(i)

        for i in range(1, len(mono_stack), 1):
            area = heights[mono_stack[i]] * ((n - 1) - (mono_stack[i - 1] + 1) + 1)
            ans = area if area > ans else ans

        return ans