# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue
class Codec:
    '''
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return []
        num_of_level = 1
        q = Queue()
        q.put(root)
        ans = []
        while 1:
            last_level = True
            for i in range(0, num_of_level):
                node = q.get()
                if node == None:
                    ans.append(None)
                    q.put(None)
                    q.put(None)
                else:
                    ans.append(node.val)
                    q.put(node.left)
                    q.put(node.right)

                    if node.left != None or node.right != None:
                        last_level = False

            if last_level == True:
                break

            num_of_level *= 2
        
        index = 0
        for i in range(len(ans) - 1, -1, -1):
            if ans[i] != None:
                index = i
                break
        
        return ans[:index + 1]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None

        root = TreeNode(data[0])
        num_of_level = 2
        parent = 0
        child = 1
        q = Queue()
        q.put(root)
        while child < len(data):
            i = 1
            while i <= num_of_level and child < len(data):
                node = q.get()
                left = TreeNode(data[child])
                child += 1
                if left != None:
                    node.left = left
                q.put(left)
                
                if child >= len(data):
                    break
                right = TreeNode(data[child])
                child += 1
                if right != None:
                    node.right = right
                q.put(right)
                i += 2
            
            num_of_level *= 2
        
        return root
    '''
    '''
    严格的层次遍历，需要去维护层次状态
    很多冗余代码，而且序列化字符串里很多None
    用DFS+队列，不必手动维护层次状态
    
    这种情况下如何序列化？
    每次从队列取node，都把node序列化
    node不为None时，向队列加入node的左右子树
    队列为空时，序列化完成，因为只有真实node（非None）才能向队列添加元素
    
    那么如何反序列化？
    需要适用队列来把树还原
    维护一个当前node的孩子指针（不是真的指针，其实就是跟踪data数组的下标）
    当开始第i层第一个node的处理时，孩子指针在第i+1层的第一个node

    那么对于队列里取出的node
    真实node（非None）：根据孩子指针更新它的左右子树（注意左右子树为为空时不必更新）
    ，左右子树入队列，更新孩子指针。
    虚拟None:什么也不做。因为虚拟node是没有孩子的，它不能去影响孩子指针。

    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        q = Queue()
        q.put(root)
        ans = ""
        
        while q.empty() == False:
            node = q.get()
            if node == None:
                ans += ",null"
            else:
                ans += "," + str(node.val)
                q.put(node.left)
                q.put(node.right)
        return ans[1:]

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return None
        data = data.split(",")
        root = TreeNode(int(data[0]))
        q = Queue()
        q.put(root)
        i = 1

        while q.empty() == False:
            node = q.get()
            if node != None:
                if data[i] != "null":
                    node.left = TreeNode(int(data[i]))
                    q.put(node.left)
                i += 1
                if data[i] != "null":
                    node.right = TreeNode(int(data[i]))
                    q.put(node.right)
                i += 1
        return root            
    '''

    '''
    我为什么需要一个队列？为了维持秩序！
    为了序列化时的秩序被反序列化捕捉到。
    那我可以直接用dfs来维持秩序啊。就不需要再去频繁的入队，出队。
    '''
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []

        def dfs(node):
            if not node:
                ans.append("x")
                return 
            
            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return ",".join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        self.i = 0
        def dfs():
            
            if self.i >= len(data) or data[self.i] == "x":
                self.i += 1
                return
            node = TreeNode(int(data[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))