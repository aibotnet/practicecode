#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
 
/*  Tree node structure */
struct Node
{
    int key;
    struct Node *left, *right;
};
 
/* Helper function that allocates a new node with the
   given key and NULL left and right pointer. */
struct Node *newNode(char k)
{
    struct Node *node = (struct Node*)malloc(sizeof(struct Node));
    node->key = k;
    node->right = node->left = NULL;
    return node;
}

int max(int a, int b){
    if(a>b) return a; return b;
}
int getHeight(struct Node *root){
    if(!root) return 0;
    return 1+ max(getHeight(root->left),getHeight(root->right));
}

int getPathArray(struct Node* root,int element,int PA[],int i){
    if(!root) return 0;
    if(root->key==element) return 1;
    int a = getPathArray(root->left,element,PA,i+1);
    if(a){PA[i]=1;return 1;}
    int b = getPathArray(root->right,element,PA,i+1);
    if(b){PA[i]=0;return 1;}
    return 0;
} 
void printPathArray(struct Node *root, int element){
    int height=getHeight(root),i;
    if(!root) return;
    int *PA=(int *)malloc(sizeof(int)*height);
    for(i=0;i<height;i++) PA[i]=-1;
    if(root->key==element){
        printf("%s\n", "No need to traverse element at top");
    }
    else if(getPathArray(root,element,PA,0)){
        for(i=0;PA[i]!=-1;i++)
            printf("%d\n", PA[i]);
    }else{
        printf("%s\n", "-1");
    }   
}
 
// Driver Program
int main()
{
    struct Node* root = NULL;
    root = newNode(10);
    root->left = newNode(20);
    root->right = newNode(30);
 
    root->left->right = newNode(40);
    root->left->left = newNode(50);
    root->right->left = newNode(60);
    root->right->right = newNode(70);
 
    root->left->left->left = newNode(80);
    root->left->left->right = newNode(90);
    root->left->right->left = newNode(80);
    root->left->right->right = newNode(90);
    root->right->left->left = newNode(80);
    root->right->left->right = newNode(90);
    root->right->right->left = newNode(80);
    root->right->right->right = newNode(90);

    printPathArray(NULL,10);
}