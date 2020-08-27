/**
 * 大小为n的数组中所有数字都满足 0 <= nums[i] <= n - 1，找出该数组中任意一个重复数字
 * 
 * 在该数组中，若无重复数字，那么每个下标都唯一对应一个与下标相等的值
 * 
 * 如果对数组进行排序后，进行下标与值的比对，时间复杂度为O(n * logn)
 * 
 * 如果用哈希表，时间复杂度为O(n)，代价是空间复杂度为O(n)
 * 
 * 时间复杂度为n，空间复杂度为1的算法：
 * 遍历数组，当下标i与nums[i]不相等时，准备交换该nums[i]到与其值nums[i]相等的下标j处(即j == nums[i])，若j处值与i处值相等，则代表nums[i]是重复数字。
 * 
 * @param {number[]} nums
 * @return {number}
 */
var findRepeatNumber = function(nums) {
    for(let i = 0; i < nums.length; i++){
        while(nums[i] !== i){
            if(nums[i] === nums[nums[i]]){
                return nums[i]
            }

            let index = nums[i]
            nums[i] = nums[index]
            nums[index] = index
        }
    }
};




/** 
 *  大小为n + 1的数组中所有数字都满足 0 <= nums[i] <= n - 1，找出该数组中任意一个重复数字
 *  限制条件:不得更改原数组
 * 
 *  二分查找的思路：分为两组，0 ~ mid, mid + 1 ~ n，若数组中0 ~ mid出现的次数超过mid + 1，代表该区间内有重复数字，依次进行二分查找直到得到重复数字。
 *  时间复杂度 logn * n 
 * @param {number[]} nums
 * @return {number}
 */
var findRepeatNumber = function(nums) {

    let start = 0
    let end = nums.length - 1
    
    while(1){
        if(start === end){
            return start
        }

        let mid = Math.floor((start + end) / 2)

        if(searchRepeat(start, mid) === true){
            end = mid
        }
        else{
            start = mid + 1
        }
    }

    function searchRepeat(start, end){
        let count = 0
        for(let i = 0; i < nums.length; i++){
            if(nums[i] >= start && nums[i] <= end){
                count++
            }
        }

        return count > (end - start + 1)
    }
};