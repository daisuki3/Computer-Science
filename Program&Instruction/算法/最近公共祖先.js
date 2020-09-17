/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {TreeNode}
 */
var lowestCommonAncestor = function(root, p, q) {
    let ans = null
    
    function hasPOrQ(node){
        if(node === null){
            return false
        }
        
        let l = hasPOrQ(node.left)
        let r = hasPOrQ(node.right)

        if((l && r) || ((l || r) && (node.val === p.val || node.val === q.val))){
            ans = node
        }

        return l || r || node.val === p.val || node.val === q.val
    }

    hasPOrQ(root)

    return ans
};