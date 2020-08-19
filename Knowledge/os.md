# File System:
- Transforms blocks into Files and Directories
- Optimize for access and usage patterns
- **Maximize sequential access, allow efficient random access**



# File System Components
- Naming: Interface to find files by name, not by blocks
- Disk Management: collecting disk blocks into files
- Protection: Layers to keep data secure
- Reliability/Durability: Keeping of files durable despite crashes, media failures, attacks, etc.



# 死锁

1. 资源互斥条件
某种资源一次只允许一个进程访问，直到使用结束

2. 请求与保持条件
占有资源并等待其他进程释放需要的资源

3. 不可剥夺条件

4. 循环等待条件
每个进程都占有下个进程需要的至少一种资源

解除死锁的方法：
- 破坏循环等待（不高效）

- 破坏不可剥夺（资源没得到满足时释放保持的所有资源）

- 破坏请求与保持条件
    1. 一次性申请资源（可能使进程发生饥饿）
    2. 运行中逐步释放使用完毕的资源



# 文件系统

**在磁盘上组织文件的方法**

- 从名称到地址的映射
- 管理存储空间
- 文件信息共享
- 文件保密安全措施



# LRU换页算法

# 句柄

存储系统资源物理地址的变量

# Linux 五种IO模型

## 同步IO
- 阻塞
</br>等待数据处理的过程中进程被挂起

- 非阻塞
</br>等待数据处理的过程中进程继续执行，但是会不断询问数据状态

- 信号驱动
</br>进程继续运行，端口可用时用信号通知进程

- 多路复用
</br>一个进程同时对多个IO端口进行监控，当任何一个端接口可用时函数返回。

## 异步IO

数据的请求和读写由系统处理，所有事物处理完成后通知进程，不会阻塞进程的运行。

缺点：可能造成IO任务积压，内存占用过高而崩溃。



# select & poll & epoll

均利用IO多路复用机制

select和poll时间复杂度为n，发生IO事件后无差别轮询。
select：默认1024个fd数量
poll：链表保存fd，无最大连接数限制

epoll：event poll 事件驱动，时间复杂度为1.