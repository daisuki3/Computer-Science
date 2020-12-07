/**
 * 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
 * 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
 * @return {number}
 */
/*
笨蛋做法 找中位数 复杂度 nlogn
var majorityElement = function(nums) {
    nums.sort((a, b) => a - b)
    
    return nums[Math.floor((0 + nums.length - 1) / 2)]
};
*/

/*
思路
碰到相同的+1
不同的-1
count=0换个数字 
*/
var majorityElement = function(nums) {
    let ans
    let count = 1
    for(let i = 0; i < nums.length; i++){
        if(nums[i] === ans){
            count++
        }
        else{
            count--
            if(count === 0){
                ans = nums[i]
                count++
            }
        }
    }

    return ans
};