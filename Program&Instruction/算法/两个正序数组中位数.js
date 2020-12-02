/**
 * nums1 和 nums2 为正序数组，找出这组数据的中位数
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
var findMedianSortedArrays = function(nums1, nums2) {
    let m = nums1.length
    let n = nums2.length
    
   
    //获取两个数组中第k大的数字
    function getK(k, index1, index2){


        if(index1 >= m){
            return nums2[index2 + k - 1]
        }
        else if(index2 >= n){
            return nums1[index1 + k - 1]
        }
        else if(k == 1){
            return Math.min(nums1[index1], nums2[index2])
        }
        else{
            let newi1 = Math.min(Math.floor(k / 2) - 1 + index1, m - 1)
            let newi2 = Math.min(Math.floor(k / 2) - 1 + index2, n - 1)
            
            let newk
            if(nums1[newi1] <= nums2[newi2]){
                newk = newi1 - index1 +1
                index1 = newi1 + 1
            }
            else if(nums1[newi1] > nums2[newi2]){
                newk = newi2 - index2 + 1
                index2 = newi2 + 1
            }

            return getK(k - newk, index1, index2)
        }

    }

    return (getK(Math.ceil((m + n) / 2), 0, 0) + getK(Math.ceil((m + n + 1) / 2), 0, 0)) / 2
};