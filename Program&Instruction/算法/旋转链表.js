/**
 * 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
 * 
 * 思路：
 * 每个节点向右移动k个位置，其实就是尾部k个结点移动到首部。
 * 
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
    if(!head || !head.next){
        return head
    }


    /*
    function toHead(node){
        let tmp = node
        while(tmp.next.next !== null){
            tmp = tmp.next
        }

        let newHead = tmp.next
        newHead.next = node
        tmp.next = null

        return newHead
    }
    */

    let len = 1
    let end = head
    while(end.next !== null){
        end = end.next
        ++len
    }

    k = k % len
    if(k === 0){
        return head
    }

    let off = len - k + 1    
    let node = head
    for(let i = 1; i < off - 1; i++){
        node = node.next
    }
    let newHead = node.next

    node.next = null
    end.next = head

    return newHead
};