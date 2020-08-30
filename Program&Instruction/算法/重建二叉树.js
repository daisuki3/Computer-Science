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
var buildTree = function(preorder, inorder) {
    let s = []
    let dummy = new TreeNode(10)

    let i = 0
    let j = 0

    let node = dummy
    while(1){

        while(i < preorder.length){

            if(i > 0 && preorder[i - 1] === inorder[j]){
                break
            }

            node.left = new TreeNode(preorder[i])
            node = node.left
            s.push(node)
            i++
        }

        if(i === preorder.length){
            break
        }

        //找到非空的右子树
        while(s.length >= 2 && inorder[j + 1] === s[s.length - 2].val){
            s.pop()
            j++
        }

        node = s.pop()
        node.right = new TreeNode(preorder[i])
        i++
        node = node.right
        s.push(node)
        //使j指向最左端的叶子
        j++
    }

    return dummy.left
};



/*
var buildTree = function(preorder, inorder) {
    if(preorder.length === 0){
        return null
    }
    let s = []
    let j = 0
    let root = new TreeNode(preorder[0])
    s.push(root)

    for(let i = 1; i < preorder.length; i++){
        let node = s[s.length - 1]

        if(node.val !== inorder[j]){
            //可以增加左子
            node.left = new TreeNode(preorder[i])
            s.push(node.left)
        }
        else{
            while(s.length > 0 && s[s.length - 1].val === inorder[j]){
                node = s.pop()   
                j++
            }
            node.right = new TreeNode(preorder[i])
            s.push(node.right)
            //指到最左的子
        }
    }

    return root
};
*/