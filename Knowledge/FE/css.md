.x 类选择器 <div class="x">

#x id选择器 <div id="x"> 
id是唯一的


伪类
:link
:visited

伪元素
::before
::after


子选择符 >
紧邻同胞选择符 +
一般同胞选择符 ~
通用选择符 *

# 层叠

## 样式表来源
- 浏览器默认
- 用户样式表
- 作者链接样式表
- 作者嵌入样式
- 作者行内样式

重要性递增

## 层叠规则

- 按照样式表来源顺序排序 和 !important 强制规则
- 按特指度排序
**特指度计算方法**
三位数特指度
I-C-E
选择符有id I +1
选择符有类 C +1
选择符有元素名 E +1

应用特指度数值最高的规则



固定宽度布局

# 流动布局：布局大小随浏览器窗口大小变化

不要为浮动拦加内边距(padding)来使内容和边界分隔，这样会增加浮动栏的宽度，可能会造成右边的浮动栏下滑。可行的做法是为浮动栏加一个内部div，然后设置内部div内边距为0，加外边距(margin)，这样不会更改浮动栏的宽度。

中栏流动布局：中栏变窄变宽，左栏右拦宽度都不变。
实现方法：
- 加一个左栏中栏的两栏外包装，设置中栏外边距Apx，两栏外包装设置负外边距-Apx把右拦拉回来达到固定的效果。
- CSS3 display:table-cell IE-7及以下浏览器不支持

横向导航栏居中
实现方法：
- 使用display:table
  .navi{
    display: table;
    text-align: center;
    margin: 5px auto;
}

**弹性布局：布局大小和内容大小都随浏览器窗口大小变化，过于复杂所以很难设计得好。**

- 聚焦搜索框时变宽 使用focus伪类

- 弹出层被覆盖 解决办法：设置z-index让弹出层显示在上层

- position:
static 遵循基本的定位规定
relative 参考自身静态位置
absolute 参考最近的具有定位设置的父元素
fixed 参考可视窗口



# 浮动 & BFC(Block Formatting Context)

先来看看浮动可能造成的副作用

这个例子中，浮动的图片影响有三：
1. 父元素div.out高度塌陷，现在图片高度不再计入div.out的高度
2. 子文本排列在图片周围
3. 相邻文本也排列在图片周围

```html
        <div class="out">
            <img class="float" src="../1.png">
            
            <p>被影响的子文本</p>
        </div>

        <div class="next">
            被影响的相邻文本
        </div>
```

```css
.float{
    margin-left: 5px;
    float:left;
    width: 100px;
    height: 100px;
}

.out{
    border: 2px solid red;
}

.next{
    margin: 20px;
    border: 2px solid blue;
}
```

消除这些副作用的方法；清除浮动

```css
p{
  clear: left;
}
```

clear:left告诉浏览器该元素的左边不能有浮动元素，所以子文本被移动到了图片下方。
这样，虽然图片已经脱离文档流，仍然不计入div.out的高度，在div.out眼中，只是子文本的上方多出了一片空白区域。


假如我们希望子文本排列在图片周围，而相邻文本排列在下方呢？这时候清除浮动就不起作用了。派上用场的是BFC,块级格式化上下文。它让div.out中的元素不影响外部元素。

我们需要先去掉clear:left,来为div.out创建BFC。
```css
.out{
  overflow:auto;
}
```

BFC的作用主要有这几点：
1. 浮动元素无法溢出BFC,消除浮动造成的高度塌陷
2. 阻止外边距合并

# flex布局

## 项目

flex-grow 默认0 即有多余空间也不放大
flex-shrink 默认1 即空间不足就缩小
flex-basis 分配多余空间前占据的主轴空间
flex : 0 1 200px 对应grow,shrink,basis 不放大,不足时缩小,200px

## 容器

# link & @import
- link
  HTML文件中的标签，可以引入除CSS的其它文件
- @import
  CSS中的规则，必须先于所有其他规则
  @import url list-of-media-queries

# position
static 默认在文档流
relative 相对于文档流中原本的位置移动
absolute 脱离文档流 相对于第一个relative父元素定位，如果没有就是body
fixed 在视图中固定位置
sticky 初始行为是relative，滑动到阙值后是fixed，粘贴在最近的可滚动祖先上

z-index 用来决定元素重叠时谁在上层显示

# overflow
visible 默认值 溢出盒子
hidden 
(also overflow-y or overflow-x)scroll
auto 浏览器决定是否加滚动轮

# value & unit
- 绝对单位
px pixels

- 相对单位
em 父元素font-size
rem 根元素font-size
vh 1% 窗口高度
vw 1% 窗口宽度

width: 50% 父元素宽度的50%

margin: 10% & padding: 10% 
都是相对父元素的宽度计算

# inline & block

# 居中

为什么 margin：auto只能水平居中？
因为auto是利用剩余空间，垂直高度是不确定的，所以为0。