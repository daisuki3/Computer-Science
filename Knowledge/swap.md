数据交换技巧

swap(&nums[i], &nums[j]){
    
    //数据初始化
    nums[i] = nums[i] ^ nums[j];

    //nums[j]变成了最初的nums[i]
    nums[j] = nums[i] ^ nums[j];
    
    //nums[i]变成了最初的nums[j]
    nums[i] = nums[i] ^ nums[j];
}
