```
void printPath(vertex v, Table T) {

	if (T[v].path != -1]{
		printPath(T[v].path,T);
		printf("to";)
		}

	printf("%v",v); 
}
```


topologic sort O(E+V)  
the body of the for loop is executed at most once per edge, 
the queue operations are done at most once per vertice

```
unwighted shortest path O(E+V):
void unweighted(table T) {
	queue Q;
	vertex v, w;

	enqueue(s, Q);

	while (!isEmpty(Q)) {
		v = dequeue(Q);

		for each w adjacent to v //adjacency list is used
			if (T[w].dist == inf) {      // no known field ,v konw=>
				T[w].dist = T[v].dist + 1;   // v.dist!=inf				
				T[w].path = v;
				enqueue(w, Q);
			}
	}
}
```

weighted shortest path ( djkstra's algorithm  O(E*logV+V*logV):  

```
void djkstra(Table T) { //distances need to be kept in a priority queue 
	vertex v, w;        ///to make findSmallestDistVertex efficient

	while (1) {
		v = findSmallestDistVertex(T);    //smallest unknown vertex
		if (!v)
			break;

		T[v].known = true;
		for each w adjacent to v
			if(!T[w].known)
				if (T[v].dist + Cvw < T[w].dist) {
					T[w].dist = T[v] + Cvw;
					T[w].path = v;
				}
	}
}
```

```
weightedNegative shortest path O(E*V):
void weightedNegative(Table T) {
	queue Q;
	vertex v, w;

	enqueue(s, Q);//s :start vertex

	while (!isEmpty(Q)) {
		v = dequeue(Q);   //at most v times 
		for each w adjacent to v  //avoid negative cycle
			if (T[v].dist + Cvw < T[w].dist) {
				T[w].dist = T[v].dist + Cvw;
				T[w].path = q;
				if (w not in the queue)
					enqueue(w, Q);
			}
	}
}
```

- Newwork Flow Problems 
G , flow grapg Gf, residual graph Gr 
**residual graph:find new path, can change the path pattern** 
-- naive: f maximum flow  O(f*E), augmenting path can be found in O(E) 
-- tricking: 
1. choose augmenting path with largest increase in flow 
O(E*logCapmax) augmentations ?????????????  O(E*logV) per augmentation 
2. choose path with least number of edges


- Minimum Spanning Tree: 
-- **Prime's algorithm  O(E*logV) using binary heap** 
The heap should order the vertices by the smallest edge-weight that connects them to 
any vertex in the partially constructed minimum spanning tree (MST) (or infinity if no such edge exists). 
at each step adding the cheapest possible edge from the tree to another vertex

-- **Kruskal's  algorithm  O(E*logE)** 
continually to select the edges in order of smallest weight and accept an edge if it does not cause a cycle


