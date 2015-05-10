#include<iostream>
#include<stdlib.h>
using namespace std;

struct node {
	int data;
	struct node * left;
	struct node * right;
};

typedef node node;

node * createNode(int data){
	node * temp = (node *) malloc(sizeof(node *));
	if (!temp)
	   exit(0);
	temp -> data= data;
	temp->left=temp->right=NULL;
	
	return temp;
}

node *extractLeafList(node *root , node **head){
	if (!root)
		return NULL;
	if (root->left==NULL and root->right==NULL){		
			root->right = *head;
			if ((*head)!=NULL){
				(*head)->left = root;
			}
			*head = root;
	return NULL;
	}	
	root->right=extractLeafList(root->right , head);
	root->left=extractLeafList(root->left , head);
	
	return root;
}

void printList(node *head){
	while(head){
		cout<<head->data <<" ";
		head=head->right;
	}
}

void print(node * root){
	if(!root)
		return;
	cout<<root->data<<" ";
	print(root->left);
	print(root->right);
}
int main(){
    node *head = NULL;
    node *root = createNode(1);
     root->left = createNode(2);
     root->right = createNode(3);
     root->left->left = createNode(4);
     root->left->right = createNode(5);
     root->right->right = createNode(6);
     root->left->left->left = createNode(7);
     root->left->left->right = createNode(8);
     root->right->right->left = createNode(9);
     root->right->right->right = createNode(10);
 
     cout<<"Inorder Trvaersal of given Tree is:\n";
     print(root);
 
     root = extractLeafList(root, &head);
 
     cout<<"\nExtracted Double Linked list is:\n";
     printList(head);
 
     cout<<"\nInorder traversal of modified tree is:\n";
     print(root);
     return 0;
}
