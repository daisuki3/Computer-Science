
function reverse(head){
    if(head === null  || head.next === null){
        return head;
    }
    else{
        
        tmp = reverse(head.next)
        
        //加一条反链条
        head.next.next = head
        //必须设置当前结点next属性为null，否则以后改变当前结点next属性时会出错
        head.next = null
        
        //其实就是返回原链表的最后一个结点
        return tmp
    }
}


//迭代版本
var reverseList = function(head) {
    if(head === null){
        return  null
    }
    
    let nh = head
    let node = head
    while(node.next !== null){
        let tmp = node.next
        node.next = tmp.next

        tmp.next = nh
        nh = tmp
    }

    return nh

};

//递归版本
/*
思路 
head的下一个结点 是 翻转后head的上一个结点
所以递归翻转head.next 返回新的头结点 
然后设置head的父节点，也就是原来链表中head的下一个结点 更新子结点为null

*/
var reverseList = function(head) {
    if(head === null){
        return null
    }

    if(head.next === null){
        return head
    }

    let pre_last = head.next
    let newhead = reverseList(head.next)
    pre_last.next = head
    head.next = null

    return newhead
};
