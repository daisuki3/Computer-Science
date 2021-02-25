class Solution {
public:
    int numMusicPlaylists(int N, int L, int K) {
        /*
        dp[i][j] 长度i的列表有j首不同的歌
        dp[i][j] = dp[i - 1][j - 1] * (N - j + 1) + dp[i - K][j] * j
                
        长度L 不同的歌N
        现在求dp[L][N]
        
        
        为什么只有dp[0][0] == 1
        dp[i][0](i > 0)都是0
        
        边界 
        只处理i >= 1 && j >= 1
        j == 1 时
        从认知上来讲 dp[i][1] = 1 or 0（依据k值的给定）
        
        新歌
        dp[i][1] += dp[i - 1][1 - 1] * (N - 1 + 1);
        旧歌
        dp[i][j] = dp[i - 1][j] * (j - K);
        
        
        这个思路为什么不对
        在i-k-1到i-1中可能有很多重复歌曲的播放可能
        这个算式遗漏了这些可能  
        dp[i][j] = dp[i - K - 1][j] * j;
        */
        long  dp[L + 1][N + 1];
        long mod = pow(10, 9) + 7;     
        
        for(int i = 0; i <= L; i++){
            for(int j = 0; j <= N; j++){
                dp[i][j] = 0;
            }
            if (i == 0){
                continue;
            }
            dp[i][1] = N * max(1 - K, 0);
        }
        dp[1][1] = N;
        
        for(int i = 1; i <= L; i++){
            for(int j = 2; j <= N; j++){                
                dp[i][j] = 0;
                //旧歌
                dp[i][j] += dp[i - 1][j] * max(j - K, 0);
                //新歌
                dp[i][j] += dp[i - 1][j - 1] * (N - (j - 1));
                dp[i][j] %= mod;
            }
        }
        return dp[L][N];
    }
};