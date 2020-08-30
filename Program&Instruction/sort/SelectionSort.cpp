
/* 稳定性：不稳定
   将某元素交换到队头时，可能破坏被交换元素的稳定
*/
void SelectionSort(int *A, int n){
	int i, j , min, tmp;

	//寻找第i小的数，放到开头藏起来
	for(i = 0; i < n - 1; i++){
		min = i;
		
		for(j = i + 1;j < n; j++)
			if(A[j] < A[min])
				min = j;

		//swap
		tmp = A[i];
		A[i] = A[min];
		A[min] = tmp;
	}
}
