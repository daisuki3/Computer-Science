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