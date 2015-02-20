#include<iostream>
#include<stdlib.h>
using namespace std;

struct node{
	int data;
	struct node *left;
	struct node *right;
};
typedef struct node node;

//return path in array for BST
//Time comlexity o(nlogn)
bool getPathArrayBST(node* root,int arr[],int *len, int se){
	if(!root) return false;
	if(root->data==se){ // preorder checking elemnt
		arr[*len]=2;//this indicate end of traversal
		*len=*len+1;
		return true;
	}
	else if(root->data > se){
		bool left = getPathArrayBST(root->left,arr,len,se);
		if (left){arr[*len]=1;*len=*len+1;return true;}
		return false;
	}
	else{
		bool right = getPathArrayBST(root->right,arr,len,se);
		if(right){arr[*len]=0;*len=*len+1;return true;}
		return false;
	}
}

//path array in binary tree
//return the reverse of path
//Time compexity o(n)
bool getPathArray(node* root,int arr[],int *len, int se){
	if(!root) return false;
	bool left = getPathArray(root->left,arr,len,se);
	bool right = getPathArray(root->right,arr,len,se);
	if(root->data==se){ // preorder checking elemnt
		arr[*len]=2;//this indicate end of traversal
		*len=*len+1;
		return true;
	}
	if(left){arr[*len]=1;*len=*len+1;return true;}
	if(right){arr[*len]=0;*len=*len+1;return true;}

	return false;
}

void inorder(node* root){
	if(!root) return;
	inorder(root->left);
	cout<<root->data<<" ";
	inorder(root->right);
}

node* getNewNode(int val){
	node* newNode = new node;
	newNode->data=val;
	newNode->left=newNode->right=NULL;
	return newNode;
}

int main(){
	node * root = getNewNode(30);
	root->left = getNewNode(17);
	root->left->left = getNewNode(8);
	root->left->right= getNewNode(22);
	root->left->right->left= getNewNode(20);
	root->left->right->left->left= getNewNode(18);
	
	root->right = getNewNode(42);
	root->right->left= getNewNode(35);
	root->right->left->left= getNewNode(32);
	root->right->left->right= getNewNode(37);
	root->right->right= getNewNode(44);
	root->right->right->right= getNewNode(46);
	//inorder(root);
	int arr[256]={0};int len=0;
	getPathArrayBST(root,arr,&len,18);
	//printing array content
	cout<<"Path Array\n";
	for(int i=0;i<len;i++){
		cout<<arr[i]<<" ";
	}
	return 0;
}