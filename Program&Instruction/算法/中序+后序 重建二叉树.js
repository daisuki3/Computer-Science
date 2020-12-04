/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */

 /*
 递归版本 非常简单 
 只要根据postorder末端的根节点值划分一下inorder和postorder
 再设置个出口就好了
 */
var buildTree = function(inorder, postorder) {
    if(inorder.length === 0){
        return null
    }
    
    if(inorder.length === 1){
        return new TreeNode(inorder[0]) 
    }

    let root = new TreeNode(postorder[postorder.length - 1])

    let i = 0
    for(; i < inorder.length; i++){
        if(inorder[i] === root.val){
            break
        }
    }

    root.left = buildTree(inorder.slice(0, i), postorder.slice(0, i))
    root.right = buildTree(inorder.slice(i + 1), postorder.slice(i, postorder.length - 1))

    return root
};