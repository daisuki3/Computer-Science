/*
n个任务 k个机器，一个任务只能在一个机器上运行，找出最小运行时间。

分支限界法：

状态节点包含了，各机器运行时间，处理已分配任务的运行时间
(即各机器运行时间的最大值)，下一个待分配任务，等信息。

处理当前状态节点时，采取广度优先搜素，分别分配下一个待分配任务
给各个机器，利用该结点的信息，可以得到下一个结点。

到达叶子节点，即全部任务已分配完时，得到可能的最优值。

采取剪枝策略，剪掉运行时间已经大于最优值的状态节点，可以减少程序运行时间。

利用最小堆（以节点运行时间为参数），即优先队列，来储存状态节点，
可以更快地得到最优值。

*/


#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

const int M = 100;
const int INF = 0x3f3f3f3f;
int x[M], n, k;
int best = INF;                                     //最佳值

struct node                                         //定义一个node
{
	int time[M];                                    //当前的time
	int num;                                        //当前的位置
	int tt;                                         //当前的最大值
	int trace[M];
	bool operator<(const node& a)const
	{				//重载运算符，实现优先队列从小到大排列
		return tt > a.tt;
	}
}point;                                             //当前点

int p_queue() 
{
	priority_queue<node> q;

	for (int i = 1; i <= k; i++) 
	{                   //初始化
		point.time[i] = 0;
		point.trace[i] = 0;
	}

	point.num = 0;
	point.tt = 0;

	while (1) 
	{                        //不符合退出循环
		if (point.num == n)
		{
			if (best > point.tt) 
			{	
				best = point.tt;
			}                     //达到最后一点给best赋值
		}
		else 
		{
			for (int i = 1; i <= k; i++)
			{
				node next;                          //定义中间变量并赋值
				next.num = point.num + 1;


				for (int m = 1; m <= k; m++) 
				{
					next.time[m] = point.time[m];
				}

				for (int j = 1; j <= n; ++j)
				{
					next.trace[j] = point.trace[j];
				}

				next.time[i] += x[next.num];
				next.trace[next.num] = i;

				next.tt = max(next.time[i], point.tt);


				if (next.tt < best) 
				{                //剪枝
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