
/**
 * 给出一个区间的集合，请合并所有重叠的区间。
 * 
 * 时间复杂度 n * logn
 * 先把各区间按照左坐标排序，方便进行重叠区间的合并。
 * @param {number[][]} intervals
 * @return {number[][]}
 */

var merge = function(intervals) {



    intervals.sort(function(i1, i2){
        return i1[0] - i2[0]
    })

    for(let i = 0; i <= intervals.length - 2; i++){
        if(intervals[i + 1][0] <= intervals[i][1]){

            intervals[i][1] = Math.max(intervals[i + 1][1], intervals[i][1])
            intervals.splice(i + 1, 1)
            
            //当前区间仍然需要进行合并检测
            i--
        }
    }

    return intervals
};