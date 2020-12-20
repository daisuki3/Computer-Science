/*
思路：
nums[i] + i 是 i 的最远跳跃点，却不一定是最有潜力的跳跃点
在 i ~ nums[i] + i 中，搜寻最有潜力的起跳点

边界处理
nums[max] + max 为新的最远跳跃点
jump++ 选择该点跳跃，继续搜寻
如果最远点超过末尾，最后一次起跳，return jump + 1

*/

func jump(nums []int) int {
    var n int = len(nums)

    if n == 1 || n == 0 {
        return 0
    }

    var maxJumpTo, jump int = nums[0], 0;

    var i int = 0

    for maxJumpTo < n - 1 {
        var tmax int = maxJumpTo

        //在maxJumpTo内寻找 潜力最强的跳跃点 起跳
        for ; i < maxJumpTo; i++ {
            if nums[i] + i > nums[tmax] + tmax {
                tmax = i
            }
        }

        jump = jump + 1
        maxJumpTo = nums[tmax] + tmax
    }

    return jump + 1

}