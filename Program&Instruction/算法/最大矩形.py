class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        if row == 0:
            return 0
        ans = 0
        col = len(matrix[0])

        for i in range(0, row, 1):
            for j in range(0, col, 1):
                if matrix[i][j] == "0":
                    continue
                if j > 0 and matrix[i][j - 1] != "0":
                    matrix[i][j] = str(int(matrix[i][j - 1]) - 1)
                    continue
               
                k = j
                num_of_1s = 0  
                while k < col:
                    if matrix[i][k] != "1":
                        break
                    else:
                        num_of_1s += 1
                        k += 1
                matrix[i][j] = str(num_of_1s)
        #print(matrix)
        for j in range(0, col, 1):
            mono_stack = [-1]
            
            for i in range(0, row, 1):
                while len(mono_stack) > 1 and int(matrix[mono_stack[-1]][j]) > int(matrix[i][j]):
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