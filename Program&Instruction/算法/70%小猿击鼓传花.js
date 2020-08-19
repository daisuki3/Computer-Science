var a = readline().split(" ").map(Number)
var n = a[0]
var k = a[1]
var mod = 1000000007
/*
k个人 传n次后回到小猿手里

an：传递n次后回到小猿手里
bn：传递n次后不在小猿手里

则有关系式：
an = bn-1
bn = (k-1)an-1 + (k-2)bn-1

得到
an = (k-1)an-2 + (k-2)an-1
*/

//直接用dp来做，不优化时间复杂度，只能过70%的数据
an = [0, 0, (k - 1) % mod]

for(let i = 3; i <= n; i++){
    an[i] = (k - 1) * an[i - 2] + (k - 2) * an[i - 1]
    an[i] = an[i] % mod
}

console.log(an[n] % mod)




/*var a = readline().split(" ").map(Number)
var n = a[0]
var k = a[1]
var mod = 1000000007

//直接用dp来做，不优化时间复杂度，只能过70%的数据
 
var last_2 = 0
var last_1 = (k - 1) % mod
var an = 0;
 
for(let i = 3; i <= n; i++){
    an = ((k - 1) * last_2 + (k - 2) * last_1) % mod
    last_2 = last_1
    last_1 = an
}
 
console.log(an % mod)
*/
















