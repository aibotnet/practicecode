#include<iostream>
#include<stdlib.h>
using namespace std;

struct node{
	int data;
	struct node *left;
	struct node *right;
};
typedef struct node node;


node* createBSTFromArray(char *arr , int s, int e){
	if(s>e) return NULL;
	int mid=s+(e-s)/2;
	node *newNode = new node;
	newNode->data = arr[mid];

	newNode->left  = createBSTFromArray(arr,s,mid-1);
	newNode->right = createBSTFromArray(arr,mid+1,e);

	return newNode;
}

void inorder(node* root){
	if(!root) return;
	inorder(root->left);
	cout<<root->data<<" ";
	inorder(root->right);
}

int main(){
	char arr[] = {2,4,6,8,10,12,14};
	node * root=createBSTFromArray(arr,0,6);
	inorder(root);
}
