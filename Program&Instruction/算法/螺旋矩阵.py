'''
注意边界处理
即rowStart == rowEnd 和 colStart == colEnd的时候
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rowStart = 0
        rowEnd = len(matrix) - 1
        colStart = 0
        colEnd = len(matrix[0]) - 1

        ans = []
        while rowStart <= rowEnd and colStart <= colEnd:
            if rowStart == rowEnd:
                for i in range(colStart, colEnd + 1):
                    ans.append(matrix[rowStart][i])
                break
            elif colStart == colEnd:
                for i in range(rowStart, rowEnd + 1):
                    ans.append(matrix[i][colStart])
                break
                
            for i in range(colStart, colEnd):
                ans.append(matrix[rowStart][i])
            for i in range(rowStart, rowEnd):
                ans.append(matrix[i][colEnd])
            for i in range(colEnd, colStart, -1):
                ans.append(matrix[rowEnd][i])
            for i in range(rowEnd, rowStart, -1):
                ans.append(matrix[i][colStart])

            rowStart += 1
            rowEnd -= 1
            colStart += 1
            colEnd -= 1
        
        return ans