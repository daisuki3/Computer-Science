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
    

            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))