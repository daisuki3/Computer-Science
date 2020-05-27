void Msort(int *A, int *tmp, int left, int right);
void Merge(int *A, int *tmp, int left, int right, int rightend);

void MergeSort(int *A, int n) {
	int *tmp = new int[n];
	if (tmp != NULL) {
		Msort(A, tmp, 0, n - 1);
		delete []tmp;
	}
}

void Msort(int *A, int *tmp, int left, int right) {
	if (left < right) {
		int center = left + (right - left) / 2;
		Msort(A, tmp, left, center);
		Msort(A, tmp, center + 1, right);
		//合并两个有序序列
		Merge(A, tmp, left, center + 1, right);
	}
}

void Merge(int *A, int *tmp, int left, int right, int rightend) {
	int  leftend, num, tmppos;

	leftend = right - 1;
	tmppos = left;
	num = rightend - left + 1;

	while (left <= leftend && right <= rightend) 
		if (A[left] <= A[right])
			tmp[tmppos++] = A[left++];
		else
			tmp[tmppos++] = A[right++];

	while (left <= leftend)
		tmp[tmppos++] = A[left++];
	while (right <= rightend)
		tmp[tmppos++] = A[right++];
	
	for (int i = 0; i < num; i++)
		A[rightend] = tmp[rightend--];
}
