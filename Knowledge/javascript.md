# 数据类型

1. 字符串
2. 数值
3. 布尔值
4. null
5. undefined
6. 符号类型symbol new in ES6

7. 对象

# 原型链

prototype是**生产对象的模板**。
_proto_是**对象中指向模板的属性**。

Foo.prototype._proto_ 和 Function.prototype._proto_ 都是 Object.prototype，而object.prototype._proto_是null

所有的函数例如 function Foo(), function Object(), function Function()的_proto_都是Function.prototype

# 闭包

### 什么是闭包
在函数内部可以访问外部的变量。
内部函数可以访问定义它们的外部函数的参数和变量
函数可以访问它被创建时所处的上下文环境，这称为闭包。


### 为什么要有闭包
为了提供一个让外部可以访问到函数内部的变量的方法。

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

# this绑定
- 默认绑定到window
- 隐式绑定
    this指向最近的一个调用它的对象
- 隐式绑定丢失
    作为参数传递或变量赋值，会导致this重新进行隐式绑定，可能改变this指向
- 显示绑定
    通过call,apply以及bind改变this指向

    bind是硬绑定，返回一个boundFunction函数，其this无法通过call,apply以及bind再次改变
    ```javascript
        let obj1 = {
            name: '听风是风'
        };
        let obj2 = {
    name: '时间跳跃'
        };
        var name = '行星飞行';

        function fn() {
            console.log(this.name);
        };
        fn.call(obj1); //听风是风
        fn(); //行星飞行
        fn.apply(obj2); //时间跳跃
        fn(); //行星飞行
        let boundFn = fn.bind(obj1);//听风是风
    boundFn.call(obj2);//听风是风
    boundFn.apply(obj2);//听风是风
    boundFn.bind(obj2)();//听风是风
    ```

- new绑定
    new调用的构造函数其this指向创建的对象
    new绑定无法和call,apply一起调用，但其优先级大于显示绑定bind

优先级
显示 > 隐式 > 默认  
new > bind > 隐式 > 默认


# Promise & setTimeout
promise是异步任务中的微任务
setTimeout是异步任务中的宏任务
先执行微任务

# ES6

 var Person = (function () {
     function Person (name) {
          this._name = name;
     }
     Person.prototype.greet = function () {
          console.log(“Hi, my name is “ + this._name);
     }
     Person.prototype.greetDelay = function (time) {
          var _this = this;
          setTimeout(function () {
               console.log(“Hi, my name is “ + _this.name);
          }, time);
     }
})();
# 函数传值

js中函数是按值传递的

如果形参为对象，实参为指针A，传入的是复制的指针B，该指针B可以改变对象的值，但无法改变指针A的值（地址）

```javascript
function test(){

}
```

# DOM

- get
document.getElementsByTags()
document.getElementById()
this.getAttribute()

- set
this.setAttribute()

- js解耦
事件绑定 this.onclick = function(){

}

- 加载问题
window.onload = func
所有DOM元素加载完后再运行func，不会产生找不到元素错误。

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


# 数组

## splice
var fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.splice(2, 0,"Lemon","Kiwi");
//在索引2处添加元素，删除0个元素

fruits 输出结果：
Banana,Orange,Lemon,Kiwi,Apple,Mango

## slice
a
(6) [2, 5, 7, 6, 8, 9]

a.slice(1,4)
(3) [5, 7, 6]

a.slice(1)
(5) [5, 7, 6, 8, 9]