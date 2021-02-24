'''
单链表快排
跟数组快排不同的细节处理 

1.
一定要传入参数n

2.
处理的时候一定要i<=n 
如果是 while node != None，会遍历完整个链表

3.
取avg，小于avg的和大于avg的分别排序。

4.
特殊情况，所有值都相等时。
如果是单纯的<=avg分入一组，会导致毫无进展，因为所有节点都归入了一组。
所以最好把 == avg的节点均匀分开。

'''
class Solution:
    def sortList(self, head):
        # 单链表快排
        def quickS(qHead, n):
            #退出条件
            if n == 0:
                return None
            if n == 1:
                return qHead

            node = qHead
            s = 0
            i = 1
            while i <= n:
                s += node.val
                node = node.next
                i += 1
            
            avg = s / n

            dummy = ListNode(0)
            dummy.next = qHead
            dummyLess = ListNode(0)
            dummyLess.next = dummy

            node = dummy
            less = 0
            flag = True

            for i in range(n):
                if node.next.val <= avg:
                    if node.next.val == avg:
                        if flag == True:
                            flag = False
                        else:
                            flag = True
                            node = node.next
                            continue

                    tmp = node.next
                    node.next = tmp.next
                    
                    tmp.next = dummyLess.next
                    dummyLess.next = tmp
                    less += 1
                else:
                    node = node.next 

            dummy.next = quickS(dummy.next, n - less)
         
            dummyLess.next = quickS(dummyLess.next, less)

            node = dummyLess
            while node.next != dummy:
                node = node.next
            node.next = dummy.next
            
            return dummyLess.next

        node = head
        hn = 0
        while node != None:
            hn += 1
            node = node.next     

        return quickS(head, hn)