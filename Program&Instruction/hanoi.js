/*
汉诺塔问题 三个柱子 src 从下往上盘子编号递减  aux 辅助柱子 dist 目标柱子
设计程序把src上的柱子移动到dist上去，要求每次只能移动一个盘子，且整个过程中编号小的盘子不能放在编号大的盘子下面

 思路：
 运用递归来解决
 子问题：要把X放到dist上去，必须先把X - 1移动到aux上去，然后再将X - 1移动到dist上来。
*/


var hanoi = function(disc, src, aux,dist){
    if(disc > 0){
        hanoi(disc - 1, src, dist, aux);

        document.writeln("move disc " + disc + " from " + src + " to " + dist);
    
        hanoi(disc - 1, aux, src, dist);
    }
}