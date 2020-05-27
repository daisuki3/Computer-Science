#include<iostream>
#include<algorithm>
using namespace std;

struct node;
typedef struct node* avlTree;
struct node{
	int val;
	avlTree left;
	avlTree right;
	int height;
	node(int x):val(x),height(1),left(NULL),right(NULL) {}
};


int height(avlTree root);

avlTree singleRotationWithLeft(avlTree node1) 
{
	/*
		    node1			      			  node2
		   /     \                           /     \
		  /       \   N                     /       \
		node2      h(X)      ----->       h(X+1)    node1
	       /     \                              	   /     \
	      /       \	M                                 /  M    \  N
	    h(X+1)   h(x)                                 h(x)     h(X)

*/
	avlTree node2 = node1->left;
	
	node1->left = node2->right;
	node2->right = node1;
	
	node1->height = max(height(node1->left), height(node1->right)) + 1;
	node2->height = max(height(node2->left), height(node2->right)) + 1;
	return node2;
}


avlTree singleRotationWithRight(avlTree node1) {
	//similar to singleRotationWithLeft
	avlTree node2 = node1->right;

	node1->right = node2->left;
	node2->left = node1;

	node1->height = max(height(node1->left), height(node1->right)) + 1;
	node2->height = max(height(node1->left), height(node2->right)) + 1;
	return node2;
}


avlTree doubleRotationWithLeft(avlTree node1) {
	node1->left = singleRotationWithRight(node1->left);
	node1 = singleRotationWithLeft(node1);
	return node1;
}


avlTree doubleRotationWithRight(avlTree node1) {
	node1->right = singleRotationWithLeft(node1->right);
	node1 = singleRotationWithRight(node1);
	return node1;
}


int height(avlTree root) {
	if (!root) return 0;
	else
		return root->height;
}


avlTree findMin(avlTree root) {
	if (!root)
		return NULL;
	avlTree temp = root;
	while (temp->left)
		temp = temp->left;
	return temp;
}


avlTree insert(int x, avlTree root) {
	if (!root) {
		avlTree ans = new node(0);
		ans->val = x;
		return ans;
	}
	else if (x == root->val)
		return root;
	else if (x < root->val) {
		root->left = insert(x, root->left);

		if (!root->right) {
			if (root->left->height == 2) {
				if (x < root->left->val)
					root = singleRotationWithLeft(root);
				else if (x > root->left->val)
					root = doubleRotationWithLeft(root);
			}
		}
		else if (root->left->height - 2 == root->right->height) {
			if (x < root->left->val)
				root = singleRotationWithLeft(root);
			else if (x > root->left->val)
				root = doubleRotationWithLeft(root);
		}
	}
	else if (x > root->val) {
		root->right = insert(x, root->right);

		if (!root->left) {
			if (root->right->height == 2) {
				if (x > root->left->val)
					root = singleRotationWithRight(root);
				else if (x < root->right->val)
					root = doubleRotationWithRight(root);
			}
		}
		if (root->right->height - 2 == root->left->height) {
			if (x > root->left->val)
				root = singleRotationWithRight(root);
			else if (x < root->right->val)
				root = doubleRotationWithRight(root);
		}
	}

	root->height = max(height(root->left), height(root->right)) + 1;
	return root;
}


 avlTree delete_avlTree(int x, avlTree root) {
	if (!root)
		return NULL;
	else if (x == root->val) {
		if (!root->right)
			return root=root->left;
		else {
			avlTree rightMin = findMin(root->right);
			root->val = rightMin->val;
			root->right = delete_avlTree(root->val, root->right);
			if (height(root->left) - 2 == height(root->right)) {
				if (height(root->left->left) > height(root->left->right))
					root = singleRotationWithLeft(root);
				else
					root = doubleRotationWithLeft(root);
			}
		}
	}
	else if (x < root->val) {
		root->left = delete_avlTree(x, root->left);
	}
	else if (x > root->val) {
		root->right = delete_avlTree(x, root->right);
	}

	root->height = max(height(root->left), height(root->right))+1;
	return root;
}


int main()
{
	avlTree one = new node(8);
	avlTree two = new node(5);
	avlTree three = new node(10);
	avlTree four = new node(4);

	one->left = two;
	one->right = three;
	two->left = four;

	two->height = 2;
	one->height = 3;

	one = delete_avlTree(5, one);

	cout << one->left->val << endl;
}

