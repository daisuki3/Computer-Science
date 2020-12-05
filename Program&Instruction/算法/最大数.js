/**
 * 给定一组非负整数 nums，重新排列它们每个数字的顺序（每个数字不可拆分）使之组成一个最大的整数。

注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。

思路：直接对数组排序，连接时可能使值更大的元素排在前面，然后转换数组为字符串

怎么判断连接时使值更大？

采用数学归纳的思想，假设现在只剩两个数字，a和b，判断谁在前谁在后？
a和b判断谁在前，直接判断'' + a + b 和 '' + b + a谁更大就行了
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    nums.sort((a, b) => {
        let aac = a + '' + b
        let bbc = b + '' + a
        

        for(let i = 0; i < aac.length; i++){
            if(aac[i] > bbc[i]){
                return -1
            }
            else if(aac[i] < bbc[i]){
                return 1
            }
        }

        return 0

  
    })

    let res = nums.join('')

    return res.replace(/^0*$/, '0')
};