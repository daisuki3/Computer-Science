/**
 * 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
 * 
 * 双指针。
 * 右指针一边走一边加子数组值。
 * 符号要求后，更新最小值。
 * 左指针开始走，一边走一边减子数组值，如果符合要求，更新最小值。
 * 
 * 
 * @param {number} s
 * @param {number[]} nums
 * @return {number}
 */
var minSubArrayLen = function(s, nums) {
    if(nums.length === 0){
        return 0
    }

    let start = 0
    let end = 0
    let sum = 0

    let ans = Number.MAX_SAFE_INTEGER
     
    while(end < nums.length){

        sum += nums[end]

        while(sum >= s){
            ans = Math.min(ans, end - start + 1)
            sum -= nums[start]
            start++
        }

        end++
    }

    return ans === Number.MAX_SAFE_INTEGER ? 0 : ans


};