/*
void SelectionSort(int *A, int n){

    node i = List.next;
    node last = list;
	for(;i != NULL; i = i.next, last = last.next){
		//寻找第i小的数，放到开头藏起来
		node min = i;


		for(node j = i.next;j != NULL; j = j.next)
			if(j.data < min.data)
				min = j;

		//swap
        last.next = min.next;

        min.next = i.next;
        i.next = min;

	}
}

哈希表：
0 21
1
2 22
3 17
4 
5 19
6 20->27

成功查找的平均长度 (1+1+1+1+1+2)/6 = 7/6



1.该结点序列表示一个最大堆
2.该结点序列不是一个堆 
堆排序的前两趟
82 68 73 61 52 42 23 26 34 90

73 68 42 61 52 34 23 26 82 90


路径矩阵
   0 1 2
0  x 0 0      x 0 0    x 0 1     x 0 1
1  1 x 1  ->  1 x 1 -> 1 x 1 ->  2 x 1
2  2 o x      2 0 x    2 0 x     2 0 x 

最短路径
v0->v1  4(路径：v0v1)
v0->v2  6（路径：v0v1v2)
v1->v0  5 (路径：v1v2v0)
v1->v2  2(路径：v1v2)
v2->v0  3(路径：v2v0)
v2->v1  7(路径：v2v0v1)

*/
#include<iostream>
#include<vector>
using namespace std;

int fib(int n);

int main(){
    int n;
    cin>>n;
    
    cout<<fib(n)<<endl;
    
    return 0;
}

int fib(int n){
    vector<int> nums(n,1);
    
    if(n <= 2){
        return nums[n];
    }
    for(int i = 2; i < n; i++){
        nums[i] = nums[i - 1] + nums[i - 2];
    }
    
    return nums[n];
}