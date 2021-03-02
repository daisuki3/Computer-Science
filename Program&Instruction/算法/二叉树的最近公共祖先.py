'''
最近公共祖先c的特性
p和q分别在c的左右子树
根据这个特性来找到c
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = []
        def dfs(node):
            if node == None:
                return False
            
            #print(node.val)
            left = dfs(node.left)
            right = dfs(node.right)

            if (left and right) or ((p == node or q == node) and (left or right)):
                #print(node.val)
                ans.append(node)
            
            if node == p or node == q or left or right:
                return True
            
            return False
        
        dfs(root)

        return ans[0]    