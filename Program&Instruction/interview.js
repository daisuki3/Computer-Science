/*
赛马问题 64匹马 8赛道 最少场数找top4
8 场分组赛
9 小组头名top1 
10 top2、3：同时决出，top2[A2,B1] top3[A3,B2,C1] A4,B3,C2
/////////////////////////////////////不需要如果头名为A2，则1，2，3名分别为top2，3，4
如果头名为B1，第二为C1，则1，2名为top2，3，加赛11
其余情况，1，2，3名分别为top2，3，4
11 加上D1进入比赛 头名为top4

Vue生命周期
init Events&Lifecycle 
-> beforeCreate 对象创建，还未初始化
-> init Injections & reactivity 
-> created 初始化完成，模板还未渲染
-> beforeMount 模板渲染成html
-> mounted 模板已经渲染进html
->beforeUpdate
->updated
->beforeDestroy

Vue,React区别
模板 vs JSX
对象属性 vs 状态管理
React Native vs ？

前端性能优化，即提高页面加载速度，优化用户体验
1.CSS雪碧图，避免多次请求。 background-position: -a px, -b px。
图片左上角坐标(-a,-b)效果：图片左移a px，上移b px。
2.延迟加载，减少首次访问时需要请求的资源。
图片懒加载，所有图片src为loading.gif,等图片进入视窗，再将图片改为data-src属性指向的图片。
offsetTop < scrollTop + clientHeight 加载图片


v-model 语法糖
v-model="sth" => :value="sth"  @input="sth = $event.target.value"

HEAD 只返回头部信息 场景：判断某资源是否存在，或者获取关键信息


*/
/*
foo函数返回自身被调用的次数
考察闭包和IIFE的应用
*/
let foo = function(){
    let count = 0;
    //console.log("now count : " + count)
    function closure(){
        count = count + 1
        return count;
    }

    closure.reset = function(){
        count = 0;
    };

    return closure;
}();

/*测试代码
[1,2,3,4,5].forEach(element => {
    console.log(foo())
});

foo.reset();

console.log(foo());
*/

/*
防抖
事件触发n秒后再执行回调，n秒内被触发则重新计时。
*/

function debounce(fn, delay){
    let id = null;

    return function(){
        clearTimeout(id);
        id = setTimeout(() => fn.apply(this, arguments)
        , delay);
        //为什么要有apply的这个this？
        //如果没有this，防抖 对象的方法 时会找不到this，报错
    }
};

/*
节流
事件在n秒内只能执行一次
*/
function throttle(fn, delay){
    let pre = new Date();
    let throttled = false,
        savedArgs,
        savedThis

    return function wrapper(){

        if(throttled === true){
            savedArgs = arguments;
            savedThis = this;
        }

        throttled = true;

        fn.apply(this, arguments);
        //冷却完后throttled为false,如果有冷却时错过的动作，则执行
        setTimeout(() => {
            throttled = false;
            if(savedArgs){
                wrapper.apply(savedThis, savedArgs);
                savedArgs = savedThis = null;
            }
        }, delay);

    }
};
 
/*
实现 call,apply,bind
*/
Function.prototype.my_call = function(thisArg, ...arg){
    let fn = Symbol('fn');
    thisArg.fn = this;
    let result = thisArg.fn(...arg);

    delete thisArg.fn;
    return result;
};

Function.prototype.my_apply = function(thisArg, args){
    let fn = Symbol('fn');
    thisArg.fn = this;

    let result = thisArg.fn(...args);

    delete thisArg.fn;
    return result;
};

Function.prototype.my_bind = function(thisArg, ...arg1){

    let self = this;
    let funcb = function(...arg2){
        return self.call(this instanceof self ? this : thisArg, ...arg1, ...arg2);
    };

    //让funcb有this的原型方法
    let f = function (){};
    f.prototype = this.prototype;
    funcb.prototype = new f();

    return funcb;
};

/*
实现一个new 
*/

function my_new(){
    let constructor = [...arguments][0];
    let args = [...arguments].slice(1);
    
    let obj = Object.create(constructor.prototype);

    let res = constructor.apply(obj, args);

    return typeof res === 'object' ? res : obj;
};

/*
实现一个instanceof
*/
function my_instanceof(l, r){
    l = Object.getPrototypeOf(l);
    r = r.prototype;

    while(l !== null){
        if(l === r){
            return true;
        }
        else{
            l = Object.getPrototypeOf(l);
        }
    }

    return false;
};

/*
实现Object.create()
*/
Object.prototype.my_create = function(p, properties){
    let res = {};
    Object.setPrototypeOf(res, p);
    Object.defineProperties(res, properties);

    return res;
}

/*
实现Object.assign()
*/
Object.prototype.my_assign = function(target, ...souces){
    if(target === null || target === undefined){
        return;
    }
    
    for(let i = 0; i < souces.length; i++){
        for(let [k, v] of Object.entries(souces[i])){
            target[k] = v;
            //Object.defineProperty(target, Object.getOwnPropertyDescriptor(souces[i], k));
        }
    }

    return target;
};


/*
实现Array.reduce()
*/

Array.prototype.my_reduce = function(fn, init){
    if(this.length === 0 && init === undefined){
        throw new TypeError('empty array with no init value');
    }

    let i = init === undefined ? 1 : 0;
    let ac = init === undefined ? this[0] : init;

    while(i < this.length){
        if(this[i] !== undefined){
            ac = fn(ac, this[i]);
            i++;
        }
    }

    return ac;
};

/*
实现Array.map()
*/

Array.prototype.my_map = function(fn, context){
    let res = [];
    for(let i = 0; i < this.length; i++){
        let tmp;
        if(context !== undefined){
            tmp = fn.call(context, this[i]);
        }
        else{
            tmp = fn(this[i]);
        }
        res.push(tmp);
    }
    return res;
};

/*
实现Array.flat()
*/

Array.prototype.my_flat = function(depth){
    let arr = this;
    let res = [];
    let de = depth || 1;

    function dfs(array, depth){

        for(let i = 0; i < array.length; i++){
            if(Array.isArray(array[i]) === true && depth > 0){
                dfs(array[i], depth - 1)
            }
            else{
                res.push(array[i]);
            }
        }
    }

    dfs(arr, de);
    return res;
};


/*
const arr1 = [0, 1, 2, [3, 4]];

console.log(arr1.my_flat());
// expected output: [0, 1, 2, 3, 4]

const arr2 = [0, 1, 2, [[[3, 4]]]];

console.log(arr2.my_flat(2));
*/

/*CSS三角形
.tri{
    height: 0;
    width: 0;
    border: 30px solid transparent;
    border-left-color: blue;
}
*/

//垂直居中
/*
justify-content: center; 水平居中 主轴对齐
align-items: center; 垂直居中  交叉轴对齐
*/

// 三栏布局
/* 
flex三栏
.container {
    display: flex;
}
.main {
    flex-grow: 1;
    height: 300px;
    background-color: red;
}
.left {
    order: -1;
    flex: 0 1 200px;
    margin-right: 20px;
    height: 300px;
    background-color: blue;
}
.right {
    flex: 0 1 100px;
    margin-left: 20px;
    height: 300px;
    background-color: green;
}
*/
//flex : grow默认0空间多余不放大 shrink默认1空间不够缩小 basis


/*
设置浮动 float：left 的原因。
让左右两栏进入第一行。

如何理解margin-left: -100%;
-100%是指父元素width * 100%
*/

/*圣杯布局 
容器设置margin留出空隙

margin-left 回到main的左右两边
position:relative 离开main到预留出的空隙上去
.container {
    margin-left: 120px;
    margin-right: 220px;
}
.main {
    float: left;
    width: 100%;
    height: 300px;
    background-color: red;
}
.left {
    float: left;
    width: 100px;
    height: 300px;
    margin-left: -100%;
    position: relative;
    left: -120px;
    background-color: blue;
}
.right {
    float: left;
    width: 200px;
    height: 300px;
    margin-left: -200px;
    position: relative;
    right: -220px;
    background-color: green;
}
*/

/*
双飞翼布局
中栏100%宽度,再添加一个内部div并设置margin-left,right为左右两栏预留位置
左右两栏利用负边距来覆盖中栏的预留位置

.container{
    overflow: hidden;
}

.main{
    width :100%;
    float: left;
    background: red;
}


.mid-inner{
    height: 80px;
    background: red;
    margin-left: 100px;
    margin-right: 100px;
}

.left{
    width: 100px;
    float: left;
    height: 80px;
    margin-left: -100%;
    background: yellow;

}

.right{
    width: 100px;
    float: left;
    height: 80px;
    margin-left: -100px;
    background: green;
 
}
*/


/*
数组去重
*/
function unrepeat(arr){
    return Array.from(new Set(arr));
}
/*

1.[...new Set(arr)]

2. function(arr){
    let a = [];
    for(let i = 0; i < arr.length; i++){
        if(a.indexof(arr[i]) === -1){
            a.push(arr[i]);
        }
    }

    return a;
}

3. filter
*/
/*
千分位格式化
*/
function format(num){
    let numArr = String(num).split('').reverse();

    let start = numArr.indexOf('.');
    start = start === -1 ? 0 : start + 1;

    let integ = '';
    for(let i = 1, j = start; j < numArr.length; i++,j++){
        integ += numArr[j];
        if(i % 3 === 0 && numArr[j + 1] !== undefined && numArr[j + 1] !== '-'){
            integ += ',';
        }
    }

    return integ.split('').reverse().join('') + numArr.slice(0, start).reverse().join('');
}

//console.log(format(-351122312312.4443));
/*
函数柯里化 
add()
*/

function add(...args1){
  
    let s = args1.reduce((prev, next) => prev + next);

    let t = function (...args2){
        if(args2.length === 0){
            return s;
        }
        
        let s2 = args2.reduce((prev, next) => prev + next);
        
        return add(s, s2);
    };

  

    t.toString = function(){
        return s;
    };

    return t;
};


//console.log(add(2)(9,3)());

/*
用setTimeout实现setInterval
*/
function my_setInterval(fn, sec, ...args){
    function interval(){
        setTimeout(interval, sec);
        fn(...args);
    }

    setTimeout(interval, sec);
}

/*
实现promise
*/

/*
promise.all
*/

function promise_all(promises){
    let list = []
    let len = 0

    return new Promise((resolve, reject) => {
        for(let val of promises){
        
            Promise.resolve(val).then(
            data => {
                list[i] = data
                len++
    
                if(len === promises.length){
                    resolve(list)
                }
            },
            error => {
                reject(error)
            })
        }
    })
}

/*
实现promise.race
*/

function promise_race(promises){

    return new Promise((resolve, reject) => {
        for(let val of promises){
            Promise.resolve(val).then(
                data => {
                    resolve(data)
                },
                error => {  
                    reject(error)
                }
            )
        }
    })
}
