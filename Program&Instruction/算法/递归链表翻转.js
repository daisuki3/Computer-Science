
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