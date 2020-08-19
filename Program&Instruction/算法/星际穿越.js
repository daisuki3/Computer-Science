var n = parseInt(readline())

arr = []
var maxpoint = {
    x : 0,
    y : 0,
    z : 0,
    value : 0
}

for(let i = 0; i < n; i++){
    arr[i] = []
    for(let j = 0; j < n; j++){
        arr[i][j] = []
        for(let k = 0; k < n; k++){
            arr[i][j][k] = readline().split(" ").map(Number)[3]
            
            if(maxpoint.value < arr[i][j][k]){
                maxpoint.x = i
                maxpoint.y = j
                maxpoint.z = k
                maxpoint.value = arr[i][j][k]
            }

        }
    }
}

console.log(travel(arr, maxpoint, maxpoint.x, maxpoint.y, maxpoint.z, 0))

var turn = [[0, 0, 1], [0, 0, -1], [0, 1, 0], [0, -1, 0], [1, 0, 0], [-1, 0, 0]]

function travel(arr, maxpoint, a, b, c, energy){
    
    let energy = energy + arr[a][b][c]
    let max = energy

    for(let i = 0; i < 6; i++){
        let x = a + turn[i][0]
        let y = b + turn[i][1]
        let z = c + turn[i][2]

        //路不通
        if(x < 0 || y < 0 || z < 0 
            || x == n || y == n || z == n
            || arr[x][y][z] >= arr[a][b][c]){
                continue;
            }
        
        if(travel(arr, maxpoint, x, y, z, energy) > max){
            max = travel(arr, maxpoint, x, y, z, energy)
        }
    }

    return max
}

