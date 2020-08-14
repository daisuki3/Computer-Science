/*
n个任务 k个机器，一个任务只能在一个机器上运行，找出最小运行时间。

基本思路：最小运行时间即各机器的最长运行时间。如果不采取优化，尝试每个可能的分配策略，每个机器都可能分配到每个任务，一共有k * n种分配方案。

我们需要从k * n 种可能中找出时间最短的分配方案。

然而我们知道一些分配方案很明显是不科学的，例如将所有任务都分配给一个机器，而其他机器全部不运转。

这时候我们需要采取策略来减少程序的最佳方案的搜寻时间，提高效率。

分配状态：包含各机器分配到的任务，任务分配的进度。

那么所有独特的分配状态会形成一个树。最优时间就是其所有叶子结点的运行时间最小值。

优化方案：
- 把分配状态放进最小堆（以当前需要的运行时间为参数），每次取最小堆顶点的分配状态作为得到下一个分配状态的依据，可以较快得到一个比较小的运行时间。
- 剪枝：对于每一个新得到的分配状态，将它的运行时间与当前最优时间比较，如果过大，就将其舍弃，因为不可能通过这个分配状态得到一个更小的运行时间。

这个方法叫做分支限界法。

分支限界法：

状态节点包含了，各机器运行时间，处理已分配任务需要的时间(即各机器运行时间的最大值)，当前结点分配到的任务等信息。

处理当前状态节点时，采取广度优先搜素，分别分配下一个待分配任务给各个机器，可以得到下一个结点。

到达叶子节点，即全部任务已分配完时，得到可能的最优值。

采取剪枝策略，剪掉运行时间已经大于最优值的状态节点，可以减少程序运行时间。

利用最小堆（以节点运行时间为参数），即优先队列，来储存状态节点，可以更快地得到最优值。

*/


#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

const int M = 100;
const int INF = 0x3f3f3f3f;
int x[M], n, k;
int best = INF;                                     //最佳值

struct node                                     
{
	int timeOfMachine[M];                                    
	int curNumOfTask;                                       
	int maxTime;                                      
	int scheduleTrace[M];
	bool operator<(const node& a)const
	{				//重载运算符，实现优先队列从小到大排列
		return maxTime > a.maxTime;
	}
}point;                                       

int p_queue() 
{
	priority_queue<node> q;

	//初始化结点数据
	for (int i = 1; i <= k; i++) 
	{   
		point.timeOfMachine[i] = 0;
		point.scheduleTrace[i] = 0;
	}
	point.curNumOfTask = 0;
	point.maxTime = 0;



	while (1) 
	{                      
		if (point.curNumOfTask == n)
		{
			if (best > point.maxTime) 
			{	
				best = point.maxTime;
			}                     //达到叶子结点时给best赋值
		}
		else 
		{
			/*
				尝试分配第num个任务给每个机器 
			*/
			for (int i = 1; i <= k; i++)
			{
				node next;                          //定义中间变量并赋值
				next.curNumOfTask = point.curNumOfTask + 1;

				
				for (int m = 1; m <= k; m++) 
				{
					next.timeOfMachine[m] = point.timeOfMachine[m];
				}

				for (int j = 1; j <= n; ++j)
				{
					next.scheduleTrace[j] = point.scheduleTrace[j];
				}

				next.timeOfMachine[i] += x[next.curNumOfTask];
				next.scheduleTrace[next.curNumOfTask] = i;

				next.maxTime = max(next.timeOfMachine[i], point.maxTime);


				if (next.maxTime < best) 
				{   //剪枝,如果当前时间已经过长则不必入队
					q.push(next);
				}
			}
		}

		if (q.empty() == true) 
		{                              //队列无值退出循环
			return best;
		}
		else 
		{                                      //取队列中第一个值进入下一步循环
			point = q.top();
			q.pop();
		}

	}
	return best;
}

int main() {
	cin >> n >> k;                                  //输入
	for (int i = 1; i <= n; i++)
	{
		cin >> x[i];
	}

	cout << p_queue() << endl;                      //输出
}