/*
turn 数组应定义在调用函数之前 否则turn === undefined
注意变量名污染 函数内变量不要和全局变量名相同

*/

var a = readline().split(" ").map(Number)
var m = a[0]
var n = a[1]
var k = a[2]
 
var arr = []
var memo = []


for(let i = 0; i < m; i++){
    arr[i] = []
    memo[i] = []
    let row = readline().split(" ").map(Number)
     
    for(let j = 0; j < n; j++){
        memo[i][j] = []
        arr[i][j] = row[j]
    }
}

let ans = 0
var turn = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for(let i = 0; i < m; i++){
    for(let j = 0; j < n; j++){
        ans = Math.max(ans, go(i, j, k))
    }
}

console.log(ans)



function go(i, j, privilege){
    
    //走到（i，j）位置还剩当前特权数时，能走的最长路径已保存，可以取用
    if(memo[i][j][privilege] !== undefined){
        return memo[i][j][privilege]
    }
    //console.log("i :" + i + " j :" + j + " privilege :" + privilege)
   
 
    let tmpmax = 1
     
    for(let t = 0; t < 4; t++){
        
        let row = i + turn[t][0]
        let col = j + turn[t][1]
        if(row >= 0 && row < m && col >= 0 && col < n){

            if(arr[i][j] < arr[row][col]){
                tmpmax = Math.max(tmpmax, go(row, col, privilege) + 1)
            }
            else{
                if(privilege > 0){
                    tmpmax = Math.max(tmpmax, go(row, col, privilege - 1) + 1)
                }
            }
        }
    }
     
    //console.log("i :" + i + " j :" + j + " tmpmax : " + tmpmax)

    memo[i][j][privilege] = tmpmax

    return tmpmax
}

/*
1 3 3
2 4 9
8 9 2 
*/