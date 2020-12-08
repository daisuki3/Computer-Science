/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */

 /*
 思路 二叉搜索树的中序遍历数组应该是一个严格升序的数组
 只需要得到中序遍历然后遍历验证就行了
 */
var isValidBST = function(root) {
    
    let inor = []
    function inorder(root){
        if(!root) return

        inorder(root.left)
        inor.push(root.val)
        inorder(root.right)
    }



    inorder(root)

    for(let i = 0; i < inor.length - 1; i++){
        if(inor[i] >= inor[i + 1]){
            return false
        }
    }

    return true

};