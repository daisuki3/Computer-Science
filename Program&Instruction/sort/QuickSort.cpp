#define cutoff (5)

void Qsort(int *, int, int);
int Median3(int *, int, int);

void Swap(int *a, int *b) {
	int tmp = *a;
	*a =*b;
	*b = tmp;
}
void QuickSort(int *A, int n) {
	Qsort(A, 0, n - 1);
}

/* 	递归的排序算法，先调整再递归排序 
	稳定性：稳定

	pivot:一个尽可能合理的序列中值
	得到pivot后，将序列元素相对pivot换位：对于升序排序，小于pivot的元素在左，大于pivot的元素在右
	
	现在的序列正中央大概率并不是元素换位后pivot的正确位置，因为pivot的位置由序列中小于pivot的元素个数来决定
	那么需要先将pivot藏在序列的左端或右端（本程序将pivot藏在了右端）
	等到pivot的位置可以确定了，再将它放到正确的位置

*/
void Qsort(int *A, int left, int right) {
	if (left + cutoff <= right) {

		int pivot = Median3(A, left, right);
		int i = left, j = right - 1;
		
		while (1) {
			while (A[++i] < pivot);
			while (A[--j] > pivot);

			if (i < j)
				Swap(&A[i], &A[j]);
			else
				break;
		}
		
		//元素换位结束时，A[i] > pivot
		Swap(&A[i], &A[right - 1]);

		Qsort(A, 0, i - 1);
		Qsort(A, i + 1, right);
	}
	else
		//在序列元素不多时，使用递归的快速排序效率低，此时选用元素少时高效的插入排序
		InsertionSort(A + left, right - left + 1);
}


/* 	left < center < right
	把中间值藏在right-1的位置并返回
*/
int Median3(int *A, int left, int right) {
	int center = (left + right) / 2;

	if (A[left] > A[center])
		Swap(&A[left], &A[center]);
	if (A[left] > A[right])
		Swap(&A[left], &A[right]);
	//let A[left] be the smallest one
	if (A[center] > A[right])
		Swap(&A[center], &A[right]);
	//then finally right <= center<= right

	Swap(&A[center], &A[right - 1]);
	return A[right - 1];
}
