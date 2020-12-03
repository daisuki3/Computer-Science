/**
 * 利用快排的思路，找pivot，也就是三点的中值
 * 对于快排，元素过少时，< 3个，会出现bug，所以元素 <=3时直接用getPivot()暴力排序
 * 
 * 由于只用找第k个，所以不用关心整个数组是否有序
 * 只需要确保 左边的元素都小于它 右边的元素都大于它 而它是倒数第k个元素
 * 
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    
    let n = nums.length

    function swap(i, j){
        let tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
    }

    function qSort(start, end){
        if(start >= end){
            return 
        }

        if(start > n - k){
            return
        }

        if(start + 2 >= end){
            getPivot(start, end)
            return 
        }

        

        let pivot = getPivot(start, end)
        swap(Math.floor((start + end) / 2), end)

        let i = start, j = end
        while(i < j){
            while(nums[++i] < pivot){}
            while(nums[--j] > pivot){}

            if(i < j){
                swap(i, j)
            }
          
        }
        //pivot在end处，i处的元素大于等于pivot  
        // 如果i 和 end 相等了 怎么办？特殊情况 start 和 end 太近时直接暴力排序
        swap(i, end)

        qSort(i + 1, end)
        if(i <= n - k){
            return
        }

        qSort(start, i - 1)
    }

    function getPivot(start, end){
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
        
        return nums[mid]
    }

    qSort(0, nums.length - 1)

    return nums[n - k]
    //return nums[n - k]
};