
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

    return function(args){
        let that = this;
        let _args = arguments;
        clearTimeout(id);
        id = setTimeout(() => fn.apply(that, _args)
        , delay);
    }
};

/*
节流
事件在n秒内只能执行一次
*/
function throttle(fn, delay){
    let pre = new Date();

    return function(args){
        let now = new Date();
        if(now - pre > delay){
            pre = now;
            fn.apply(this, arguments);
        }
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
实现promise
*/
