/**给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。


思路：
最无脑的做法是遍历 复杂度O(n)
稍微好一点的是二分先找到位置 
再从那个位置左右遍历，某些情况下这个算法的复杂度也会到达O(n)

最优解是个性化的二分
这个二分不是找满足条件的那个元素(也即 === target)，而是找满足条件下标最小的那个元素，一直找下去
那么设置该条件为 >= target 这样找到的就是下标最小的那个
设置该条件为 > target 这样找到的就是下标最大的那个的后一位

边界情况处理 减少冗余代码
找下标最小时，如果找不到 直接返回-1 -1
之后找下标最大时，可以保证一定存在

* @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    /* 
        二分然后遍历的方法

    function bSearch(start, end){
        while(start <= end){
            let mid = Math.floor((start + end) / 2)

            if(nums[mid] === target){
                return mid
            }
            else if(nums[mid] > target){
                end = mid - 1
            }
            else if(nums[mid] < target){
                start = mid + 1
            }

        }

        return -1
    }

    let index = bSearch(0, nums.length - 1)
    if(index === -1){
        return [-1, -1]
    }

    let min,max
    min = max = index
    
    while(min >= 1 && nums[min - 1] === target){
        min--
    }

    while(max <= nums.length - 2 && nums[max + 1] === target){
        max++
    }

    return [min, max]
    */

    function bSearch(smallestBigger){
        let start = 0, end = nums.length - 1
        let ans = nums.length

        while(start <= end){
            let mid = Math.floor((start + end) / 2)
            
            //这样ans就是最小的符合 >= target的下标
            if((nums[mid] >= target && smallestBigger === false) || (smallestBigger === true && nums[mid] > target)){
                end = mid - 1
                ans = mid
            }
            else{
                start = mid + 1
            }
        }

        if(nums[ans] === target || smallestBigger === true){
            return ans
        }
        else{
            return -1
        }
    }

    let min = bSearch(false)
    if(min === -1){
        return [-1, -1]
    }

    let max = bSearch(true) - 1

    return [min, max]
};