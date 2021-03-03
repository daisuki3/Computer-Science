'''
注意dfs(node.left) dfs(node.right) 不能修改同一个nums数组
'''
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        ans = []

        def dfs(node, nums):
            if node == None:
                return

            
            #nums.append(node.val)
            #leaf
            if node.left == None and node.right == None:      
                #print(node.val, nums)
                if sum(nums) + node.val == targetSum:
                    ans.append(nums + [node.val])

            dfs(node.left, nums + [node.val])
            dfs(node.right, nums + [node.val])
        
        dfs(root, [])

        return ans