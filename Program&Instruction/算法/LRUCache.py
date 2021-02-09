'''
设计一个put get时间复杂度都为O(1)的LRUCache
双向链表存储key和value
哈希表存储key -> node的映射

get可以直接取哈希表 dict[key].val
操作时，把存储key的节点node放到链表头部。
put可能涉及双向链表的尾部节点删除。

需要注意的点：
1.因为是双向链表，所以更新位置时，前后节点的域都要更新。
2.如果更新涉及到尾节点，要更新LRUCache.tail。
'''
class LRUCache:

    def __init__(self, capacity: int):
        self.length = 0
        self.head = None
        self.tail = None
        self.dict = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.dict:
            if self.dict[key] != self.head:
                node = self.dict[key]
                if node == self.tail:
                    self.tail = node.prev
                node.toHead(self.head)
                self.head = node
            return self.head.val
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            if self.dict[key] != self.head:
                node = self.dict[key]
                if node == self.tail:
                    self.tail = node.prev
                node.toHead(self.head)
                self.head = node

            self.head.val = value
        else:
            node = LinkedListNode(key, value)
            node.next = self.head
            if self.head != None:
                self.head.prev = node
            
            self.head = node
            self.dict[key] = node

            if self.length == 0:
                self.tail = node
            
            self.length += 1
            if self.length > self.capacity:
                newTail = self.tail.prev
                if newTail != None:
                    newTail.next = None

                self.tail.prev = None
               # print("%d poped" %self.tail.val)
                self.dict.pop(self.tail.key)
                
                self.tail = newTail 
                self.length -= 1
class LinkedListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def toHead(self, head):
        self.prev.next = self.next
        if self.next != None:
            self.next.prev = self.prev
        self.next = head
        head.prev = self
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)