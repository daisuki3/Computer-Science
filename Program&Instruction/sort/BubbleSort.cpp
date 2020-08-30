
/*	升序
	稳定性：稳定
	不会交换两个相等的元素
*/
void BubbleSort(int *A, int n){
	int j, i, tmp;
	for(i = 0; i < n - 1; ++i)
	//寻找第i大的数，放到末尾藏起来

		for(int j = 0; j < n - 1 - i; ++j)
			if(A[j] > A[j + 1]){
				//swap
				tmp = A[j];
				A[j] = A[j + 1];
				A[j + 1] = tmp;

			}
}
