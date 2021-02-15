class Solution:
    def maximalRectangle(self, matrix) -> int:
        row = len(matrix)
        if row == 0:
            return 0
        ans = 0
        col = len(matrix[0])
        for j in range(0, col, 1):
            mono_stack = [-1]
            
            for i in range(0, row, 1):
                if j > 0 and int(matrix[i][j]) == 1 and int(matrix[i][j - 1]) > 0:
                    matrix[i][j] = str(int(matrix[i][j - 1]) + 1) 

                while len(mono_stack) > 1 and int(matrix[mono_stack[-1]][j]) >= int(matrix[i][j]):
                    length = int(matrix[mono_stack[-1]][j])
                    width = (i - 1) - (mono_stack[-2] + 1) + 1
                    ans = length * width if length * width > ans else ans 
                    mono_stack.pop()
                mono_stack.append(i)
            
            for i in range(1, len(mono_stack), 1):
                length = int(matrix[mono_stack[i]][j])
                width = (row - 1) - (mono_stack[i - 1] + 1) + 1
                ans = length * width if length * width > ans else ans
        return ans