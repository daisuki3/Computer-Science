# 数据类型

1. 字符串
2. 数值
3. 布尔值

4. null
5. undefined
6. 符号类型symbol new in ES6

7. 对象

# 原型链

原型链可以实现继承
优点：效率高,少了函数调用
缺点：子类原型对象继承了父类的实例，导致所有子类实例共享该父类实例属性和方法.

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

## 类 & 继承

ES5类的实现方式
```js
function Person(name){
    this.name = name;
}

Person.prototype.say = function(){
    console.log("my name is " + name);
}

```
ES5通过原型链的继承
```js
child.prototype = new Person();
child.prototype.constructor = child;
let c = new Child();
/*
弊端:
    1.所有子类实例共享同一个父类实例，可能存在问题
    2.无法实现多继承
    
优点：简单易实现
*/
```

ES5借用构造函数的继承
```js
function child(){
    Person.call(this);
/*
弊端：
    1.不是父类的实例
    2.不能继承父类原型上的属性。
    3.父类的实例函数无法复用
优点：
    多继承、可向父类构造函数传参
*/
}
```


ES6语法糖
```js
//ES5
function Person(name, age){
    this.name = name;
    this.age = age;
}

Person.prototype.getName = function(){
    return this.name;
}


//ES6

class Person{
    constructor(name, age){
        this.name = name;
        this.ag = age;
    }

    getName(){
        return this.name;
    }
}
```

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
函数退出后，栈清空，闭包如何实现的？
闭包会维护一个Scope对象，保存其需要的变量。

## 垃圾回收机制

- 引用计数
    定义对象不再需要：没有其他对象引用到它
    限制：循环引用，即两个对象互相引用，之后离开作用域后，它们不再有用也不会被回收。
    ```js
        //循环引用的例子，myDiv从DOM树中删除后仍然不会被回收，包括lotsOfData，造成大量的内存浪费。
        var div
        window.onload = function(){
            div = document.getElementById("myDiv")
            div.circularReference = div
            div.lotsOfData = new Array(1000).join('')
        }
    ```

- 标记-清除
    定义对象不再需要：对象无法获得
    回收期定期从根开始，寻找从根开始引用的对象，无法引用到的对象将被回收。

    优化方案：
    1.分代收集，创建对象时放在新生代，在新生代存活时间长了移动到老生代，老生代对象检查频次低一些。
    2.
    
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

# 字符串

js中字符串分为基本字符串和字符串对象

字符串的值是不可变的，只能让变量指向新的字符串。

那么为什么字符串是不变量呢？

- 利用常量池，节省堆空间
- 安全性，如果字符串可变，生产新字符串时会改变原字符串。


```js
a = "test"
b = new String("test")

typeof a // string
typeof b // object

a[0] = '1'
a //"test"

b[0] = '1'
b //String {"test"}


//由数组生产字符串的方法
a = [1,2,3]
a.join() //"1,2,3"

```



# 内存泄漏

```js
var theThing = null;
var replaceThing = function () {
    var originalThing = theThing;   
    var unused = function () {
        if(originalThing) {}
    };
    theThing = {
        longStr: new Array(1000000).join('*'),
        someMethod: function () {}
    };

};

setInterval(replaceThing, 100);

```

以上代码内存泄漏的原因：第n次执行replaceThing函数时，unused闭包引用了第n-1次的theThing，之后replaceThing函数又重新定义了theThing，这样第n-1次的theThing无法被使用也无法被回收，导致内存泄漏。

解决: 去除unuserd函数或者在replaceThing函数最后一行加上 originlThing = null。

# apply & call & bind

apply函数签名
fun.apply(thisArg, [argsArray]);

call函数签名
fun.call(thisArg, arg1, arg2...);

bind函数签名
fun.bind(thisArg, arg1, arg2...)，返回一个this指向无法改变的函数

# async & defer
script标签的属性

- 默认值，既没有async也没有defer
    脚本的读取会阻塞html解析，脚本执行也会阻塞html解析
- async
    脚本的读取不会阻塞html解析，脚本执行阻塞html解析
- defer
    脚本的读取不会阻塞html解析，脚本在html解析完之后，DOMContentLoaded事件触发之前执行

