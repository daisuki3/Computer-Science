/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */



var reverseKGroup = function(head, k) {
    
    /*
        翻转nhead起始的k个结点
        如果不足k个结点，则直接返回
    */
    function reverseK(nhead){
        let length = 0;
        let node = nhead;
        let newhead = nhead;

       
        while(node !== null){
            length++;
            node = node.next;
        }
        //长度不足不必翻转，长度足够则使恰好k个结点翻转
        if(length < k){
            return newhead;
        }
        else{
            let n = 2;
            while(n <= k){
                //tmp消除
                let tmp = nhead.next;
                nhead.next = tmp.next;
        
                //tmp来到头部
                tmp.next = newhead;
                newhead = tmp;
                n++;
            }

            return newhead;
        }
    }

    /*
        reverseK()翻转后，原先的链头现在到了链尾
        
        对于每个链尾，可以翻转其后的k个元素并作出操作
        1.更新链尾的next属性
        2.替换新的链尾

        那么第一组如何处理呢？
        可以使用一个假结点，使其下一个元素为链头
        
        最后返回假结点的next属性即可
    */
    var dummy = new ListNode(100);
    dummy.next = head;

    var node = dummy;
    var tail;

    while(1){
        
        tail = node.next;
        node.next = reverseK(node.next);
        
        if(tail === node.next){
            break;
        }
        else{
            node = tail;
        }
        
    }
    
    return dummy.next;

};