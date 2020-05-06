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
void Qsort(int *A, int left, int right) {
	if (left + cutoff <= right) {
		int pivot = Median3(A, left, right);
		int i = left, j = right - 1;
		
		while (1) {
			while (A[++i] < A[pivot]);
			while (A[--j] > A[pivot]);

			if (i < j)
				Swap(&A[i], &A[j]);
			else
				break;
		}
		
		Swap(&A[i], &A[right - 1]);

		Qsort(A, 0, i - 1);
		Qsort(A, i + 1, right);
	}
	else
		InsertionSort(A + left, right - left + 1);
}

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
