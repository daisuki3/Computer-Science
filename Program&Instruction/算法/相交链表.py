# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB

        while a != b:
            
            if a == None:
                a = headB
            else:
                a = a.next
            
            if b == None:
                b = headA
            else:
                b = b.next
        return a 