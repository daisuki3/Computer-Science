'''
针对与root节点的关系，一共有六种可能的路径
1. 不经过root而在root.left
2. 不经过root而在root.right
3. 经过root和左树
4. 经过root和右树
5. 经过root和左右树
6. 只经过root

显然3 4 5 6是可以同时计算的，只需要比较单条路径的长度
计算12如果再开一个递归，效率太低，会超时
其实计算3 4 5 6的同时，1 2也被计算出来了

'''
class Solution:
    
    def maxPathSum(self, root: TreeNode) -> int:
        if root == None:
            return -sys.maxsize - 1
        left, left_single = self.deepest_Max_Path_Sum(root.left)
        right, right_single = self.deepest_Max_Path_Sum(root.right)
        
        return max(left_single, right_single, 
        left + root.val, right + root.val, left + right + root.val, root.val)

    def deepest_Max_Path_Sum(self, node):
    
        if node == None:
            return 0, -sys.maxsize - 1
        
        #left_single是路径只在node.left范围内行走时的最大值
        left, left_single = self.deepest_Max_Path_Sum(node.left)
        right, right_single = self.deepest_Max_Path_Sum(node.right)

        # 1 go left 
        # 2 go right 
        # 3 stay node
        # 4 stay befor node
        return max(left + node.val, right + node.val, node.val, 0),
         max(left_single, right_single, left + node.val,
          right + node.val, left + right + node.val, node.val)