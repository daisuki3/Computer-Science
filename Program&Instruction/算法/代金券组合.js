/*
    k个不同数字凑齐target需要的最少数字

    动态规划
    dp = []
    dp[0] = 0
    for(i in target)
        arr = []
        for(j in k)
            if(target >= nums[j])
                arr.push(dp[i - nums[j]] + 1)
        dp[i] = min(...arr)

*/

while(true){   
    var num = parseInt(readline())
    if(num == 0){
        break
    }

    var lines = readline()
    var lineArr = lines.split(" ").map(Number)
    var type = lineArr[0]
    var money = lineArr.slice(1)
    console.log(getResult(num, money))
}
 
function getResult(num, money) {
        var dp = []
        dp[0] = 0

        for (var i = 1; i <= num; i++) {

            var arr = []
            for(var j = 0; j < money.length; j++){
                if(i >= money[j]){
                    arr.push(dp[i - money[j]] + 1)
                }
            }
            dp[i] = Math.min(...arr)

        }
    return dp[num] === Infinity ? "Impossible" : dp[num]
} 



function fib(n){
    let arr = []
    arr[0] = 1
    arr[1] = 1

    for(let i = 2; i <= n; i++){
        arr[i] = arr[i -1] + arr[i - 2]
    }

    console.log(arr[n])
}
