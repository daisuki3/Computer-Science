**M * N 的玉米地，1代表可种植，0代表不可种植，且不可上下左右相邻地种植，求可行的种植方法数量**

M * N的玉米地矩阵，每一行可看做一个二进制数，这样就能用**一个十进制数来表示一行的土地状态**。

grid[M][N] 
    土地矩阵 1可种植 0不可种植
ground[M] 土地状态矩阵 
    ground[m] += grid[m][i in N] << (N - 1 - i) if (grid[m][i] == 0) 
    //grid[m][i] == 0 是为了支持后续状态是否可行的计算

state[top] 可行土地状态数组
</br>if(x & x << 1 == 0) 代表未左右相邻种植 则x是一个可行状态。
</br>top值与n有关，需计算

dp[m][top] 动态规划矩阵 **top = 1 << n 表示土地状态的十进制上界**


for j in top
    dp[0][j] = 1 if (state[j] & ground[i] == 0) 
</br>state[j] & ground[i] == 0 代表未在禁止地上种植 得到一种可行状态

状态转移方程 dp[i][j in top] = segma dp[i - 1][k in top] if(state[j] & state[k] == 0)
</br>state[j] & state[k] == 0 代表未上下相邻种植 得到一种可行状态

ans = (ans + dp[M-1][i in top]) % mod