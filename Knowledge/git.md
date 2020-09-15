# branch

git branch bugfix
新的分支bugfix指向当前结点


git checkout -b bugfix
新建分支bugfix并切换到bugfix

# merge

git merge bugfix
master指向一个拥有两个父节点(bugfix和之前的master)的节点

# rebase

git rebase master
将bugfix分支的改变应用到master分支上，使其呈线性，无分叉

