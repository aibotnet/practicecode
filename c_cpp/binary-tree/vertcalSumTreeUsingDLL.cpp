#include<iostream>
#include<stdlib.h>
using namespace std;
 
/*  Tree node structure */
struct Node
{
    int key;
    struct Node *left, *right;
};
 
/* Helper function that allocates a new node with the
   given key and NULL left and right pointer. */
struct Node *newNode(int k)
{
    struct Node *node = (struct Node*)malloc(sizeof(struct Node));
    node->key = k;
    node->right = node->left = NULL;
    return node;
}
typedef struct Node node;

node * getVerticalSum(node *root,node *res){
    if(!root) return NULL;
    if(!res){//this block is used only once in starting
        res=newNode(root->key);
    }
    else{
        res->key=res->key+root->key;
    }
    if(root->left){
        if(res->left==NULL){
            res->left=newNode(0);
            res->left->right=res;
        }
        getVerticalSum(root->left,res->left);
    }
    if(root->right){
        if(res->right==NULL){
            res->right=newNode(0);
            res->right->left=res;
        }
        getVerticalSum(root->right,res->right);
    }
    return res;
}

// Driver Program
int main()
{
    struct Node* root = NULL;
    root = newNode(10);
    root->left = newNode(20);
    // root->right = newNode(30);
 
    // root->left->right = newNode(40);
    // root->left->left = newNode(50);
    // root->right->left = newNode(60);
    // root->right->right = newNode(70);
 
    // root->left->left->left = newNode(80);
    // root->left->left->right = newNode(90);
    // root->left->right->left = newNode(80);
    // root->left->right->right = newNode(90);
    // root->right->left->left = newNode(80);
    // root->right->left->right = newNode(90);
    // root->right->right->left = newNode(80);
    // root->right->right->right = newNode(90);

    node* res= getVerticalSum(NULL,NULL);
    node * t=res;
    while(res && res->left){
        res=res->left;
        
    }
    
    while(res){
        cout<<res->key<<" ";
        res=res->right;
    }
}