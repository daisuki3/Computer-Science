/*
思路
队列是先进先出
栈是先进后出

那么用两个栈 
一个栈用来进入
一个栈用来删除
把进入栈的元素一个个出栈，再压进删除栈里
就成了先进先出，也就是队列
*/


var CQueue = function() {
    this.push = []
    this.pop = []
};

/** 
 * @param {number} value
 * @return {void}
 */
CQueue.prototype.appendTail = function(value) {
    this.push.push(value)
};

/**
 * @return {number}
 */
CQueue.prototype.deleteHead = function() {
    
    if(this.pop.length !== 0){
        return this.pop.pop()
    }

    if(this.push.length === 0){
        return -1
    }

    while(this.push.length !== 0){
        this.pop.push(this.push.pop())
    }
    return this.pop.pop()
};

/**
 * Your CQueue object will be instantiated and called as such:
 * var obj = new CQueue()
 * obj.appendTail(value)
 * var param_2 = obj.deleteHead()
 */