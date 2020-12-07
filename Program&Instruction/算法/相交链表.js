/**
 * 编写一个程序，找到两个单链表相交的起始节点。
 * 
 * 思路
 * 可以ta tb走过相同的路程然后在相交的点相遇
 * 相同的路程是 两段链表交点前的路程加交点后的路程
 * 注意处理边界情况 没有交点 或者 某条链表为空
 * 
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(headA, headB) {
    if(headA === null || headB === null){
        return null
    }

    let ta = headA, tb = headB
    let flagA = false, flagB = false

    while(ta !== tb){
        ta = ta.next
        tb = tb.next
        if(ta === null){
            if(flagA) return null
            ta = headB
            flagA = true
        }
        if(tb === null){
            if(flagB) return null
            tb = headA 
            flagB = true
        }
    }  

    return ta
};
/*
代码太不优雅了
去掉flag？

*/

while(ta !== tb){
    ta = ta.next
    tb = tb.next
    if(ta === null){
        ta = headB
    }
    if(tb === null){
        tb = headA 
    }
}  

/*
这样写是有问题的
如果两条链表不相交的话
会无限循环
能不能让链表不相交的时候也能使ta === tb？这样就不用加flag了
当然可以

*/

while(ta !== tb){
    ta = ta === null ? headB : ta.next
    tb = tb === null ? headA : tb.next
}

/*
之前的代码直接跳过了链表尾部后面的null
现在
null是两条不相交链表的ta tb走完两条链之后的归属
*/