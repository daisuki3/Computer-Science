```C
int hash(char *key, int tableSize) {
	unsigned int hashVal = 0;
	while (*key)
		hashVal += (hashVal << 5) ^ *(key++);
	
	return hashVal % tableSize;
}
```

**hi(x) = (hash(x) + Fi(x)) % tableSize**

# conflict management
- separate chain  
		require pointers

- open addressing 

	- linear probing Fi(x)=i  
			drawback: cluster

	- quadratic probing Fi(x)=i^2  
			(x) = the biggest integer not bigger than x  
			[x] = the smallest integer not smaller than x  
			
			theorem : if tablesize is prime, a new element can always be inserted  
			if the table is at least half empty( used size n <= (x) )  
			
			prove that the first (x) probing cell is different from each other,  
			so we have (x) + 1 alternative cells. At most (x) cells are occupied,  
			so the new element can be inserted.  
			
			prove:
			suppose, 1 <= i <= j < (x), and hi(i),hi(j) is equal.  
			h(i) + i^2 = h(j) + j^2 mod(tablesize)
			(i + j)(i - j) = 0 mod(tablesize)
			then we get i = j, contradiction! so hi(i), hi(j) is different.
			
			
			drawback: hash to the same position then have same alternative cells.

	- double hashing Fi(x)=i*hash2(x)  
			hash2(x)=tableSize-(x mod tableSize) and never evaluate to 0 !!

- rehashing  (not that bad, adding a constant cost to each insertion  
		first prime that is twice as large as the old table size  

- extendible hashing  
		like b-tree !!

