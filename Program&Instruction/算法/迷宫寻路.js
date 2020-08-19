
/*
    
    到达某个点必须经过其上方或左方
    所以可以用动态规划求解 dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + arr[i][j]

*/
var l = readline().split(" ").map(Number)
var m = l[0]
var n = l[1]
 
  
var arr = [];
  
for(let i = 0; i < m; i++){
    var line = readline().split(" ").map(Number)
    arr.push(line)
}
 
 
find(arr)
  
  
  
function find(arr){
    let dp = []
  
    for(let i = 0; i < m; i++){
         
        dp[i] = []
         
        for(let j = 0; j < n; j++){
              
            if(i == 0 && j == 0){
                dp[i][j] = arr[i][j]
            }
            else if(i == 0){
                dp[i][j] = dp[i][j - 1] + arr[i][j]
  
            }
            else if(j == 0){
                dp[i][j] = dp[i - 1][j] + arr[i][j]
            }
            else{
                dp[i][j] = Math.min(dp[i][j - 1], dp[i - 1][j]) + arr[i][j]
               
            }
        }
    }
  
    console.log(dp[m -1][n - 1])
      
}

/*
while(true){   


    if(num == 0){
        break
    }

    var lines = readline()
    var lineArr = lines.split(" ").map(Number)
    var type = lineArr[0]
    var money = lineArr.slice(1)
    console.log(getResult(num, money))
}
*/