/**
 * 
 * 在未排序的数组中找到第 k 个最大的元素
 * 
 * 利用快速排序的思路，把数组分为两组，一组大于pivot，一组小于pivot。
 * 
 * 然后根据两组的起始坐标与k的关系，递归调用或返回。
 * 
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {

    function sort(start, end){


        let pivot = getPivotValue(start, end)
        let left = start
        let right = end - 1

        while(right > left){
            while(nums[++left] < pivot){
            }
            while(nums[--right] > pivot){
            }

            if(left < right){
                swap(left, right)
            }

        }

        swap(left, end - 1)
    
        if(nums.length - k === left){
            return nums[left]
        }
        else if(nums.length - k > left){
            sort(left + 1, end)
        }
        else{
            sort(start, left - 1)
        }
        
        return nums[nums.length -k]
    }

    function getPivotValue(start, end){
        let mid = Math.floor((start + end) / 2)

        if(nums[start] > nums[mid]){
            swap(start, mid)
        }

        if(nums[start] > nums[end]){
            swap(start, end)
        }

        if(nums[mid] > nums[end]){
            swap(mid, end)
        }

        swap(mid, end - 1)
        
        return nums[end - 1]
    }

    function swap(a, b){
        let tmp = nums[a]
        nums[a] = nums[b]
        nums[b] = tmp
    }

    return sort(0, nums.length - 1)
};