/**
 * 我们从二叉树的根节点 root 开始进行深度优先搜索。

在遍历中的每个节点处，我们输出 D 条短划线（其中 D 是该节点的深度），然后输出该节点的值。
（如果节点的深度为 D，则其直接子节点的深度为 D + 1。根节点的深度为 0）。

如果节点只有一个子节点，那么保证该子节点为左子节点。

给出遍历输出 S，还原树并返回其根节点 root。

思路：
可以储存一个路径数组，也即从根到达该结点的路径
而不是我最常处理树遍历时用的栈

遇到新结点时，有两种情况

一是它的深度是上一个结点的深度 + 1，也就是左子

二是它的深度不再比上一个结点深，也就是先序遍历换到了右子
怎么判断是谁的右子呢？根据路径深度！
它的深度是count
那么深度为depth - 1的结点的右子就是它

 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {string} S
 * @return {TreeNode}
 */
var recoverFromPreorder = function(S) {
    let dummy = new TreeNode(0)

    let s = []
    let node = dummy
    let index
    
    
    for(let i = 0; i < S.length; i = index){
        let count = 0
        
        for(index = i; index < S.length; index++){
            if(S[index] === '-'){
                count++
            }
            else{
                break
            }
        }

        let num = ''
        for(; index < S.length; index++){
            if(S[index] === '-'){
                break
            }
            num += S[index]
        }

        if(count === s.length){ 
            node.left = new TreeNode(num)
            node = node.left
            s.push(node)
        }    
        else{
            s = s.slice(0, count)
            node = s[s.length - 1]

            node.right = new TreeNode(num)
            node = node.right
            s.push(node)
        }
    }

    return dummy.left
};