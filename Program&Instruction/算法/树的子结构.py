'''
比较时注意B为None时一定为True
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def find(node):
            if node == None:
                return
            if node.val == B.val:
                nodes.append(node)
            find(node.left)
            find(node.right)

        def valid(node, com):
            if com == None:
                return True
            elif node == None:
                return False
            elif node.val != com.val:
                return False
            else:
                return valid(node.left, com.left) and valid(node.right, com.right)

        nodes = []

        if B == None:
            return False
        
        find(A)

        for node in nodes:
            if valid(node, B) == True:
                return True
        
        return False