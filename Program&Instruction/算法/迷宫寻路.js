
var m = parseInt(readline())
var n = parseInt(readline())

var arr = [];

for(let i = 0; i < m; i++){
    let line = readline().split(" ").map(Number)
    arr.push(line)
}

find(arr)



function find(arr){
    let dp = [[]]
    dp[0][0] = arr[0][0]

    for(let i = 0; i < m; i++){
        let tmp = []
        for(let j = 0; j < n; j++){

            if(i == 0){
                tmp.push(dp[i][j - 1] + arr[i][j])
            }
            else if(j == 0){
                tmp.push(dp[i - 1][j] + arr[i][j])
            }
            else{
                let m = Math.min(dp[i][j - 1], dp[i - 1][j]) + arr[i][j]
                tmp.push(m)
            }
        }
        dp.push(tmp)
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