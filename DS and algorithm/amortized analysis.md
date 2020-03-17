POTENTIAL

---
Binomial QUEUE:  
a collection of heap-ordered binomial TREES  
the rank of a root in a binomial TREE is equal to the number of children  
expensive insertionsw remove trees,while cheap insetions create trees  

each insetion worst-case time O(logN)  

potential:number of trees

---
SKEW HEAPS  
classify nodes as either heavy or light,depending on whether or not 
the right subtree of any node has more nodes than the left subtree

potential:number of HEAVY nodes


FIBONACCI HEAPS
1.cuting nodes in leftist heaps  
because thge maximum right path has at most log(N+1) nodes, ONLY need  
to check the FIRST log(N+1) NODES on the path from P to the root

2.lazy merging for binomial queues  
if arbitrary cuts are made in the binomial trees, the resulting forest will  
no longer be a collection of binomial trees, and it will no longer be true that  
the rank of every tree is at most logN

Mark when a node first lose a child, when lose another child, unmarik and cut it  
from its parent, become a new root. With this, any node with N descendants has  

rank O(logN)  

proof:
lemma 1.X a node in fibonacci heap,ci be the ith child of x, rank of ci at least i-2,
lemma 2.any node of rank R>=1 has at least F(R+1) descendants 

potential:number of trees

---
SPLAY TREE
zig singlerotation  1  
zig-zag doublerotation 2  
zig-zig symmetry rotation 2  
amortized time to splay a tree with root T at node X is at most 3(R(T)-R(X))++1, which is  
O(logN)

potential: sum logS(i)
