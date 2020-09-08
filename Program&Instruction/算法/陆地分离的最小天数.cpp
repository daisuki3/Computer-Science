class Solution {
    public:
      struct dsu {
        int n;
        vector<int> pre;
        vector<int> sz;
        dsu(int _n) : n(_n), pre(_n), sz(_n, 1) {
          iota(pre.begin(), pre.end(), 0);
        }
        int get(int x) {
          return x == pre[x] ? x : pre[x] = get(pre[x]);
        }
        void unition(int x, int y) {
          x = get(x);
          y = get(y);
          if (x == y) return;
          if (sz[x] > sz[y]) {
            pre[y] = x;
            sz[x] += sz[y];
          } else {
            pre[x] = y;
            sz[y] += sz[x];
          }
        }
      };
    
      bool have;
      int Time;
      vector<int> dfn, low;
      vector<vector<int>> G;
      void Tarjan(int u, int p) {
        dfn[u] = low[u] = ++Time;
        int child = 0;

        if(G[u].size() == 0){
            have = true;
        }

        for (int v : G[u]) {
          if (!dfn[v]) {
            child++;
            Tarjan(v, u);
            low[u] = min(low[u], low[v]);
            if (p == -1 && child > 1) {
              have = true;
            } 
            else {
              if (p != -1 && low[v] >= dfn[u]) {
                have = true;
              }
            }
          } 
          else{
            low[u] = min(low[u], dfn[v]);
          }
        }
      }



      int dx[4] = {-1, 1, 0, 0};
      int dy[4] = {0, 0, -1, 1};
      int minDays(vector<vector<int>>& grid) {
        int n = (int)grid.size();
        int m = (int)grid[0].size();
        dsu d(n * m);
        have = false;
        Time = 0;
        dfn.resize(n * m);
        low.resize(m * n);
        G.resize(n * m, vector<int>());
    
        vector<bool> mark(n * m, false);
    
        for (int i = 0; i < n; i++) {
          for (int j = 0; j < m; j++) {
            if (!grid[i][j]) continue;
            int u = i * m + j;
            mark[u] = true;
            for (int k = 0; k < 4; k++) {
              int x = i + dx[k];
              int y = j + dy[k];
              if (x >= 0 && x < n && y >= 0 && y < m && grid[x][y] != 0) {
                int v = x * m + y;
                mark[v] = true;
                d.unition(u, v);
                G[u].push_back(v);
                G[v].push_back(u);
              }
            }
          }
        }
        int cycle = 0;
        for (int i = 0; i < n * m; i++) {
          if (mark[i] && i == d.get(i)) {
            cycle++;
          }
        }
        if (cycle > 1 || cycle == 0) return 0;
        for (int i = 0; i < n * m; i++) {
          if (mark[i]) {
            Tarjan(i, -1);
            break;
          }
        }
        return have ? 1 : 2;
      }
    };