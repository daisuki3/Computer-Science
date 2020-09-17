/**
 * @param {number[]} postorder
 * @return {boolean}
 */

/*最后一个结点为根节点 
    左子树结点值小于根结点值
    右子树结点值大于根结点值
*/
var verifyPostorder = function(postorder) {
    
    function check(start, end){

        if(start >= end){
            return true
        }

        let rootval = postorder[end]
        
        let leftend = start - 1

        for(let i = start; i < end; i++){
            if(postorder[i] > rootval){
                break
            }
            leftend++
        }

        let rightstart = leftend + 1
        for(let i = rightstart; i < end; i++){
            if(postorder[i] < rootval){
                return false
            }
        }

        return check(start, leftend) && check(leftend + 1, end - 1)
    }

    if(postorder.length === 0){
        return true
    }

    return check(0, postorder.length - 1)
};