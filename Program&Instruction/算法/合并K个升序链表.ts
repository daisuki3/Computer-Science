//合并时 链表的长度越长，效率越高
 class ListNode {
        val: number
        next: ListNode | null
        constructor(val?: number, next?: ListNode | null) {
             this.val = (val===undefined ? 0 : val)
            this.next = (next===undefined ? null : next)
        }
}

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    
    if (lists.length === 0) return null

    return merge(lists, 0, lists.length - 1)
};

function merge(lists: Array<ListNode | null>, l: number, r: number): ListNode | null {
    if (l === r) return lists[l]

    const mid = l + ( (r - l) >> 1 )
    const left = merge(lists, l, mid)
    const right = merge(lists, mid + 1, r)

    return mergeTwoLists(left, right)
}

function mergeTwoLists(a: ListNode | null, b: ListNode | null): ListNode | null {
    
    if (!a || !b) return a ? a : b

    const head = new ListNode()

    let pointer = head
    while(a && b) {
        
        if (a.val <= b.val) {
            pointer.next = a
            a = a.next
        } 
        else {
            pointer.next = b
            b = b.next
        }

        pointer = pointer.next
    }

    pointer.next = a ? a : b

    return head.next

}