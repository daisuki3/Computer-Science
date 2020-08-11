RedBlanckTree : binary search tree with following properties
1. every node is colored either red or black
2. the root is black
3. the children of red node must be black (no consecutive red nodes
4. every path from a node to a NULL pointer must contain the same 
number of black nodes   //why?
(NULL nodes are black

height of a RBT is at most 2log(N+1)
proof:
h(v) height
bh(v) black height (no v itself
lemma  tree V has at least 2^bh(v) - 1 nodes 
bh(v) >= h(v)/2
n>= 2^(h(v)/2) -1 => h(v)<= 2log(N+1)

insert : the node to be inserted must be red 

Bottom-up:
1. parent black
we are done immediately (trivial

2. parent red
(parent sibling black
rotate and change color 

(parent sibling red 
?????need percolate up until reach a black great-grandparent when great-gandparent is red 
??????? must fail 

Top-down:guarantee when parent red, sibling won't be red 
when we see a node that has two red children, we make it red and the two children black
(if its parent is red, we perform appropriate rotations, as mentioned in bottom-up,
parent red, sibling black rotation

delete: everything boils down to being able to delete a leaf, delete a red leaf node,
top-down,guarantee that X must be red, or it must go to the next red node later on



#include<iostream>
using namespace std;

struct RBTnode;
typedef struct RBTnode *RBT;
typedef enum ColorTpe{red,black} Colortype;
RBT X,T,P,GP;

RBT singleRotationWithLeft(RBT root);
RBT singleRotaionWithRight(RBT root);
RBT doubleRotaionWithLeft(RBT root);
RBT doubleRotaionWithRight(RBT root);

struct RBTnode{
    int data;
    RBT left;
    RBT right;
    Colortype color;
};

RBT findMin(RBT root){
    if(!root)
        return root;
    RBT temp=root;
    while(temp->left)
        temp=temp->left;
    return temp;
}

RBT singleRotationWithLeft(RBT root){
    RBT node= root->left;
    root->left=node->right;
    node->right=node;

    return node;
}

RBT singleRotaionWithRight(RBT root){
    RBT node=root->right;
    root->right=node->left;
    node->left=root;

    return node;
}

RBT doubleRotaionWithLeft(RBT root){
    root->left=singleRotaionWithRight(root->left);
    root=singleRotationWithLeft(root);

    return root;
}

RBT doubleRotaionWithRight(RBT root){
    root->right=singleRotationWithLeft(root->right);
    root=singleRotaionWithRight(root);

    return root;
}

void blackSiblingRotate(){  //the GP position must be black after rotating

    if(P->data < GP->data){
        if(X->data < P->data){   //P is the mew root
            P->color=black;
            GP->color=red;
            GP=singleRotationWithLeft(GP);//GP=P 
    }
        else if(X->data > P->data){ // X is the new root
            X->color=black;
            GP->color=red;
            GP=doubleRotaionWithLeft(GP);//GP=X
            P=X;
    }
}
    else if(P->data > GP->data){
        if(X->data > P->data){
            P->color=black;
            GP->color=red;
            GP=singleRotationWithLeft(GP);//GP=P
        }
        else if(X->data < P->data){
            X->color=black;
            GP->color=red;
            GP=doubleRotaionWithRight(GP);//GP=X
            P=X;
        }
    }
}

void handleTwoRedChild(){
    X->color=red;
    X->left->color=black;
    X->right->color=black;

    if(P->color==red) //P can't be root, root->color is black
        blackSiblingRotate();
}

RBT Insert(int item,RBT root){
    X=P=GP=root;
    while(X){
        if(item==X->data) // item already in RBT
            return root;

        if(X->left->color==red && X->right->color==red)
            handleTwoRedChild();

        GP=P;P=X;

        if(item<X->data)
            X=X->left;
        else
            X=X->right;
    }
    
    RBT newNode=new struct RBTnode;
    newNode->data=item;
    newNode->left=newNode->right=NULL;
    newNode->color=red;
    X=newNode;
    if(item<P->data)
        P->left=newNode;
    else
        P->right=newNode;

    if(P->color==red)
        blackSiblingRotate();

    return root;
}

RBT Delete(int item,RBT root){
    T=X=P=root;

    if(X->left->color==black && X->right->color==black)
        X->color=red;
    else if(X->left->color==black && !(item>X->data)){
        X=singleRotaionWithRight(X);
        X->color=black;
        X=X->left;
        X->color=red;
    }
    else if(X->right->color==black && !(item<X->data)){
        X=singleRotationWithLeft(X);
        X->color=black;
        X=X->right;
        X->color=red;
    }

    while(X){
        if(X->color==black){
            if(X==P->left){
                if(X->left->color==black && X->right->color==black){
                    if(T->left->color==black && T->right->color==black){
                        P->color=black;
                        X->color=T->color=red;
                    }
                    else if(T->left->color==red){
                        P=doubleRotaionWithRight(P);
                        P=P->left;
                        P->color=black;
                        X=P->left;
                        X->color=red;
                    }
                    else if(T->right->color==red){
                        P=singleRotationWithLeft(P);
                        P->color=red;
                        P->right->color=black;
                        P=P->left;
                        P->color=black;
                        X=P->left;
                        X->color=red;
                    }
                }
                else if(X->left->color==black && !(item>X->data)){
                    X=singleRotaionWithRight(X);
                    X->color=black;
                    X=X->left;
                    X->color=red;
                }
                else if(X->right->color==black && !(item<X->data)){
                    X=singleRotationWithLeft(X);
                    X->color=black;
                    X=X->right;
                    X->color=red;
                }
            }
            else{// X==P->right
                if(X->left->color==black && X->right->color==black){
                    if(T->left->color==black && T->right->color==black){
                        P->color=black;
                        T->color=X->color=red;
                    }
                    else if(T->right->color==red){
                        P=doubleRotaionWithLeft(P);
                        P=P->right;
                        P->color=black;
                        X=P->right;
                        X->color=red;
                    }
                    else if(T->left->color==red){
                        P=singleRotationWithLeft(P);
                        P->color=red;
                        P->left->color=black;
                        P=P->right;
                        X=P->right;
                        X->color=red;
                    }
                }
                else if(X->left->color==black && !(item>X->data)){
                    X=singleRotaionWithRight(X);
                    X->color=black;
                    X=X->left;
                    X->color=red;
                }
                else if(X->right->color==black && !(item<X->data)){
                    X=singleRotationWithLeft(X);
                    X->color=black;
                    X=X->right;
                    X->color=red;
                }
            }
        }

        if(item==X->data){
            if(X==P->left){
                if(!X->right){
                    P->left=X->left;
                    delete X;
                    break;
                }
                else if(!X->left){
                    P->left=X->right;
                    delete X;
                    break;
                }
                else{ // X has two child
                    RBT temp=findMin(X->right);
                    X->data=temp->data;
                    P=X;
                    X=X->right;
                    T=X->left;
                }
            }
            else{//X==P->right
                if(!X->right){
                    P->right=X->left;
                    delete X;
                    break;
                }
                else if(!X->left){
                    P->right=X->right;
                    delete X;
                    break;
                }
                else{ // X has two child
                    RBT temp=findMin(X->right);
                    X->data=temp->data;
                    P=X;
                    X=X->right;
                    T=X->left;
                }

            }

        }
        else if(item<X->data){
            P=X;
            X=X->left;
            T=X->right;
        }
        else if(item>X->data){
            P=X;
            X=X->right;
            T=X->left;
        }
    }

    root->color=black;
    return root;
}
