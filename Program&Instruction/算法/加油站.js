/**
 * 在一条环路上有 N 个加油站，其中第 i 个加油站有汽油 gas[i] 升。

你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。

如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1。

说明: 

如果题目有解，该答案即为唯一答案。
输入数组均为非空数组，且长度相同。
输入数组中的元素均为非负数。

思路：
加油站总油量 > 总耗费油量 才能绕环路一周

怎么判断从哪开始可以绕一周呢？

直接从 0 开始模拟

当某点油量小于0，说明已经走过的路上的点都不行，为什么？
因为在start是有多余油的，不加start的多余油更到不了

所以换start为下一个点开始模拟

 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {

    let start = 0, gasInCar = 0, restGas = 0

    for(let i = 0; i < gas.length; i++){
        gasInCar += gas[i] - cost[i]
        restGas += gas[i] - cost[i]

        //车开不过去
        if(gasInCar < 0){
            start = i + 1
            gasInCar = 0
        }
    }

    if(restGas < 0 || gas.length === 0){
        return -1
    }

    return start

};