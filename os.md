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

破坏循环等待（不高效）

破坏不可剥夺（资源没得到满足时释放保持的所有资源）

破坏请求与保持条件
1. 一次性申请（可能使进程发生饥饿）
2. 运行中逐步释放使用完毕的资源

# 文件系统

**在磁盘上组织文件的方法**

- 从名称到地址的映射
- 管理存储空间
- 文件信息共享
- 文件保密安全措施
