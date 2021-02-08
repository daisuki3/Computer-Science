'''
回溯法
一行一行地填
每一行的空格，依次尝试可用数字。
注意把第i + 1行的结果和第i行联系起来
也就是在i中一定要 reutrn f(i + 1)
'''
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board, 0)

    def solve(self, board, i):   

        nums = []
        for j in range(9):
            nums.append(j + 1)
        for j in range(9):
            if board[i][j] != '.':
                nums.remove(int(board[i][j]))
        for j in range(9):
            if board[i][j] == '.':
                for k in range(len(nums)):
                    if nums[k] != '.':
                        tmp = nums[k]
                        board[i][j] = str(nums[k])
                        nums[k] = '.'
                        if self.checkColumn(board, i, j) == True and self.check_9(board, i, j) == True and self.solve(board, i) == True:
                            return True
                        else:
                            board[i][j] = '.'
                            nums[k] = tmp
                return False

        if i == 8:
            return True
        else:
            return self.solve(board, i + 1)


    def checkColumn(self, board, i, j):
        for k in range(9):
            if k == i:
                continue
            elif board[k][j] == board[i][j]:
                #print("co false i %d j %d board[i][j] %s" %(i, j, board[i][j]))  
                return False
                
        return True
    
    def check_9(self, board, i, j):
        ii = i
        jj = j
        row = 0
        while i >= 0:
            row += 1
            i -= 3
        col = 0
        while j >= 0:
            col += 1
            j -= 3
        
        row_start = 3 * (row - 1) + 1 - 1
        col_start = 3 * (col - 1) + 1 - 1
        num = 0
        for m in range(row_start, row_start + 3):
            for n in range(col_start, col_start + 3):
                if m == ii and n == jj:
                    continue
                elif board[m][n] == board[ii][jj]:
                    #print("9 false i %d j %d board[i][j] %s " %(ii, jj, board[ii][jj]))
                    return False
        return True
