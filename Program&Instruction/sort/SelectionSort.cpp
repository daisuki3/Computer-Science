
/* 稳定性：稳定
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
