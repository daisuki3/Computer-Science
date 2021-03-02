'''
先用dfs得到层次遍历数组
再把奇数下标的列表反转即得到锯齿形
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []

        def dfs(node, level):
            if node == None:
                return

            if len(ans) == level:
                ans.append([])
            
            ans[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        
        for i in range(1, len(ans), 2):
            ans[i] = ans[i][::-1]
        
        return ans