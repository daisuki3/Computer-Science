# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
快慢指针
注意快指针走的时候要判断next属性是否存在，防止没有环的链表使程序产生异常
'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        
        while fast and slow:
            fast = fast.next
            if fast:
                fast = fast.next
            else:
                break

            slow = slow.next
            
            if fast == slow:
                return True

        return False
        