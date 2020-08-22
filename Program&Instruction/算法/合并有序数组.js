/**
 * 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。
 * 
 * 采用归并的思路，先复制nums1，然后将其和nums2归并到nums1.
 * 
 * 
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */

var merge = function(nums1, m, nums2, n) {
    let tmp = []
    for(let i = 0; i < m; i++){
        tmp.push(nums1[i])
    }

    let i1 = 0
    let i2 = 0
    let go = 0

    while(i1 < m && i2 < n){
        if(tmp[i1] <= nums2[i2]){
            nums1[go] = tmp[i1]
            i1++
        }
        else{
            nums1[go] = nums2[i2]
            i2++
        }

        go++
    }

    while(i1 < m){
        nums1[go] = tmp[i1]
        i1++
        go++
    }

    while(i2 < n){
        nums1[go] = nums2[i2]
        i2++
        go++
    }
};