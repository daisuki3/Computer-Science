/*
给定一个无序的整数数组，找到其中最长上升子序列的长度。

思路:维护一个升序数组，利用二分查找，输入数组中的数字要么替换该数组中的某个值，
要么添加到升序数组末尾，升序数组的长度即为最长上升子序列的长度。
时间复杂度 n * logn

*/

/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    let arr = []

    for(let i = 0; i < nums.length; i++){
        let left = 0, right = arr.length

        while(left < right){
            let mid = Math.floor((left + right) / 2)
            if(arr[mid] < nums[i]){
                left = mid + 1
            }
            else if(arr[mid] >= nums[i]){
                right = mid
            }
        } 

        if(right > nums.lentgh - 1){
            arr.push(nums[i])
        }
        else{
            arr[right] = nums[i]
        }
    }
    
    return arr.length
};