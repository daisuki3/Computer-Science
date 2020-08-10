

/* 	稳定性：稳定
	距离较远的插入排序*/
void ShellSort(int *A,int n) {
	int i, j, incre;


	for(incre = n / 2; incre > 0; incre /= 2)

		for (i = incre; i < n; i++) {
			int tmp = A[i];
			for (j = i; j >= incre && A[j - incre] > tmp; j -= incre) 
				A[j] = A[j - incre];
			A[j] = tmp;
		}
}
