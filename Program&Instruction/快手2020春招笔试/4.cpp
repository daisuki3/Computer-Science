    #include<vector>
    
    int GetMaxStaffs(vector<vector<char> >& pos) {
        // write code here
        int m = pos.size();
        int n = pos[0].size();
        int ans = 0;
        
        for(int i = 0;i < m;i++)
            for(int j = 0;j < n ;j++){
                if(pos[i][j] == '*')
                    continue;
                else if(pos[i][j] = '.'){
                    if( (i == 0 || pos[i - 1][j] != 'a') &&
                        (i == m - 1 || pos[i + 1][j] != 'a') &&
                        (j == 0 || pos[i][j - 1] != 'a') &&
                        (j == n - 1 || pos[i][j + 1] != 'a')
                      ){
                        ans++;
                        pos[i][j] = 'a';
                    }
                       
                }
            }
        
        return ans;
    }