# 数据类型

1. 字符串
2. 数值
3. 布尔值
4. null
5. undefined
6. 符号类型 new in ES6

7. 对象

# 原型链

Foo.prototype._proto_ 和 Function.prototype._proto_ 都是 Object.prototype，而object.prototype._proto_是null

所有的函数例如 function  Foo(), function Object(), function Function()的_proto_都是Function.prototype

# 闭包

## 什么是闭包
在函数内部可以访问外部的变量。

也即函数可以记住它被创建时的上下文环境。

## 为什么要有闭包
为了提供一个让外部可以访问到函数内部的变量的方法。


# 内存

- 堆内存
    1. 保存对象的内容
- 栈内存
    1. 变量标识符
    2. 指向堆内存对象的指针

# 比较

- == 只进行值的比较
- === 不仅进行值的比较，还进行数据类型的比较

# 构造函数 
``` javascript
var Vehicle = function(p){
    this.price = p;
}

var myv = new Vehicle(500);

myv.price // 500

//this代表要创建的对象的实例

//如果不使用new来调用构造函数，this代表全局对象
var e = Vehicle(1500);

e //undefined
price//1500
```

# 作用域
在函数内部定义的变量，函数外部不可见

# 闭包
内部函数可以访问定义它们的外部函数的参数和变量

函数可以访问它被创建时所处的上下文环境，这称为闭包。

``` javascript
var myObject = (function(){
    var value = 0;

    return {
        increment: function(inc){
            value += typeof inc === 'number'? inc : 1;
        },
        getValue: function(){
            return value;
        }
    };
}());
```
myObject是函数function()的返回值，也即一个对象，这个对象不能直接访问value变量，保证了value变量的私有性，但是可以通过对象中的函数实现对value变量的访问。

# 柯里化

把函数与传递给它的参数结合，产生一个新的函数。

# 记忆

把计算结果储存下来供以后使用，其实就是动态规划。

```javascript

var fibonacci = function(){
    var memo = [0,1];

    var fib = function(n){
        var result = memo[n];
        if(typeof result !=== 'number'){
            result = fib(n - 1) + fib(n - 2);
            memo[n] = result;
        }

        return result;
    }

    return fib;
}
```

