int bsearch(int *A, int start, int end, int value){
    int mid;
    while(start <= end){
        mid = start + (end - start) / 2;
        if(A[mid] == value){
            return mid;
        }
        else if (A[mid] > value){
            end = mid - 1;
        }
        else{
            start = mid + 1;
        }
    }

    return -1;
}

//返回value出现的第一个位置
int bsearch_lowerbound(int* A, int start, int end, int value) {
    int mid;
    while (start < end) {
        mid = start + (end - start) / 2;
        //区间变为[start, mid]
        if (A[mid] >= value) {
            end = mid;
        }
        //区间变为[mid + 1, end]
        else {
            start = mid + 1;
        }
    }

    return start;
}