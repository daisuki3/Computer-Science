/**
 * 在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
 * 
 * 对于左上角的点，是一行中的最小值，一列中的最小值，右方和下方都大于该点。当target大于该点，无法确定下一个查找方向
 * 
 * 对于右上角的点，是一行中的最大值，一列中的最小值，下方的点大于该点，左方的点小于该点。可以根据target与该点的关系确定查找方向。
 * 
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
var findNumberIn2DArray = function(matrix, target) {
    if(matrix.length === 0){
        return false
    }

    let row = 0
    let collum = matrix[0].length - 1
    
    while(row < matrix.length && collum >= 0){
        if(matrix[row][collum] === target){
            return true
        }
        else if(matrix[row][collum] < target){
            row += 1
        }
        else{
            collum -= 1
        }
    }

    return false
};