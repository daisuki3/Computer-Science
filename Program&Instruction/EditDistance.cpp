int NumOfOp(string olds, string news) {
	/*
		计算，在olds上，只能用三种操作，替换一个元素，删除一个元素，插入一个元素
		把olds转换成news的最小操作数
		
		矩阵元素dp(i,j) 表示 olds[0]..olds[i] 转化成 news[0]...news[j] 需要的操作数 

		状态转移方程 dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
										  |	              |                |            
										  |			      |				   |	
										  替换			  删除             插入

        替换，删除，插入分别代表了，olds[i] 和 news[j] 不相等时的三种处理方式
		
		替换：总成本为 dp[i-1][j-1] + 1 其中
		dp[i - 1][j - 1] 代表 把 olds[0]..olds[i - 1] 转换到 news[0]..news[j - 1] 的代价
		1 代表 olds[i] = news[j]
		
		删除：总成本为 dp[i - 1][j]  + 1 其中
		dp[i - 1][j] 代表 把 olds[0]..olds[i - 1] 转换到 news[0]..news[j] 的代价
		1 代表 删除olds[i]

		插入: 总成本为 dp[i][j - 1] + 1 其中
		dp[i][j - 1] 代表 把 olds[0]..olds[i] 转换到 news[0]..news[j - 1] 的代价
		1 代表 插入一个值 tmp (= news[j]) 到 olds[i] 和 olds[i + 1] 中间

		一直取三个值中的最小值，得到dp[i][j]，就是最小成本		
	*/
	int m = olds.size(); int n = news.size();

	vector<vector<int>> dp(m + 1, vector<int>(n + 1, 0));

	for (int i = 0; i <= n; i++)
		dp[0][i] = i;
	for (int i = 0; i <= m; i++)
		dp[i][0] = i;
	//初始化

	for (int i = 1; i <= m; i++) 
		for (int j = 1; j <= n; j++) {
			if (olds[i] == news[j])
				dp[i][j] = dp[i - 1][j - 1];
			else {
				int a = min(dp[i - 1][j - 1], dp[i - 1][j]);
				int b = min(a, dp[i][j - 1]);
				dp[i][j] = b + 1;
			}
		}
	
	return dp[m][n];
}