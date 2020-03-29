void InsertionSort(int *A, int n) {                 
  // 升序排序
	int j, p;
 /*A[0]..A[p - 1]为升序
  在上述序列中找到A[p]的位置
  比A[p]大的元素都被右移，直到寻找到A[p]的位置
  使A[0]..A[p]为升序
*/
	for (p = 1; p < n; p++) {
		int tmp = A[p];
    
		for (j = p; j > 0 && A[j - 1] > tmp; j--)  
			A[j] = A[j - 1];
      
		A[j] = tmp;
    
	}
}
