function swap(arr, i, j){
    let tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
};

function heapy(arr, end){
    
    for(let i = Math.floor((end - 1) / 2); i >= 0; i--){
        let parent = arr[i];
        if(2 * i + 1 <= end && arr[2 * i + 1] > arr[i]){
            swap(arr, i, 2* i + 1);
        }
        if(2 * i + 2 <= end && arr[2 * i + 2] > arr[i]){
            swap(arr, i, 2 * i + 2);
        }
    }
};

function heapsort(arr){
    let len = arr.length;
    let end = len - 1;
    for(let i = 0; i <= len - 2; i++){
        heapy(arr, end);
        swap(arr, 0, end);
        end--;
    }

    return arr;
};

console.log(heapsort([9,4,5,7,3,4,2,1]));