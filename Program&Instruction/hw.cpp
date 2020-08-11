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
#include <iostream>
#include <algorithm>
using namespace std;
 
void max_heapify(int arr[], int start, int end) 
{
    //建立父节点指标和子节点指标
    int dad = start;
    int son = dad * 2 + 1;
    while (son <= end)  //若子节点指标在范围内才做比较
    {    
        if (son + 1 <= end && arr[son] < arr[son + 1]) //先比较两个子节点大小，选择最大的
            son++;
        if (arr[dad] > arr[son]) //如果父节点大於子节点代表调整完毕，直接跳出函数
            return;
        else  //否则交换父子内容再继续子节点和孙节点比较
        {
            swap(arr[dad], arr[son]);
            dad = son;
            son = dad * 2 + 1;
        }
    }
}
 
void heap_sort(int arr[], int len) 
{
    //初始化，i从最後一个父节点开始调整
    for (int i = len / 2 - 1; i >= 0; i--)
        max_heapify(arr, i, len - 1);
    //先将第一个元素和已经排好的元素前一位做交换，再从新调整(刚调整的元素之前的元素)，直到排序完毕
    for (int i = len - 1; i > 0; i--) 
    {
        swap(arr[0], arr[i]);
        max_heapify(arr, 0, i - 1);

        for (int i = 0; i < len; i++)
            cout << arr[i] << ' ';
    }
}
 
void main() 
{
    int arr[] = {52,68,23,61,90,73,82,26,34,42};
    int len = (int) sizeof(arr) / sizeof(*arr);
    heap_sort(arr, len);
    for (int i = 0; i < len; i++)
        cout << arr[i] << ' ';
    cout << endl;
    system("pause");
}