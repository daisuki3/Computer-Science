/**给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
 * 在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
 * 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器。

思路：
其实就是找两条边，它们中最小的高度和底面长形成的面积，找这个的最大值
可以用双指针，从底面最长的开始找，然后从高度低的开始往中间走

 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let ans = 0

    let left = 0, right = height.length - 1

    while(left < right){
        ans = Math.max(ans, (right - left) * Math.min(height[left], height[right]))

        if(height[left] > height[right]){
            right--
        }
        else{
            left++
        }
    }

    return ans
};