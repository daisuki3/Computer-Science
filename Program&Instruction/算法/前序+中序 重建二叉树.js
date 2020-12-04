/**
 * 输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
 * 
 * 
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */

 /*
 迭代版本的思路
 添加前序数组中的元素到树中
 根据中序数组来判断是左子还是右子
 
 中序数组j代表当前最深的左子
 前序数组i是沿着左子下去的
 每下一个，进一次栈，因为以后还要处理右子
 
 当找到最深的左子后，开始处理右子。
 如果当前j等于栈顶元素，说明无右子
 否则当前j是右子里最深的左子
 */
var buildTree = function(preorder, inorder){
    if(preorder.length === 0){
        return null
    }

    let root = new TreeNode(preorder[0])
    
    let node = root
    let i = 0
    let j = 0
    let s = [root]

    while(i < preorder.length){
        
        node = s[s.length - 1]
        while(preorder[i] !== inorder[j]){
            i++
            node.left = new TreeNode(preorder[i])
            node = node.left
            s.push(node)
        }
        
        
        while(s.length > 0 && s[s.length - 1].val === inorder[j]){
            //出栈意味着node的左子树已经处理完了
            node = s.pop()
            j++
        }

        i++
        if(i < preorder.length){
            node.right = new TreeNode(preorder[i])
            s.push(node.right)    
        }
        
    }

    return root
}



/*
递归版本
可以通过前序preoder中第一个结点，也就是根节点，找到中序inorder中左树的结点数量
*/
/**
 * @param {number[]} preorder
 * @param {number[]} inorder
 * @return {TreeNode}
 */
var buildTree = function(preorder, inorder) {
    if(preorder.length === 0){
        return null
    }
    
    let root = new TreeNode(preorder[0])
    if(preorder.length === 1){
        return root
    }

    let i 
    for(i = 0; i < inorder.length; i++){
        if(inorder[i] === preorder[0]){
            break
        }
    }
    
    root.left = buildTree(preorder.slice(1, i + 1), inorder.slice(0, i))
    root.right = buildTree(preorder.slice(i + 1), inorder.slice(i + 1))

    return root
};