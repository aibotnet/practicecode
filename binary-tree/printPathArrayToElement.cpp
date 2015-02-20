#include<iostream>
#include<stdlib.h>
using namespace std;

struct node{
	int data;
	struct node *left;
	struct node *right;
};
typedef struct node node;


void getPathArray(node* root,char *arr,int *len){

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
	inorder(root);
	getPathArray(arr);
}