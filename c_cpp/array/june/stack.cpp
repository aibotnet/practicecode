#include<stdio.h>
#include<stdlib.h>
#include<iostream>
 
using namespace std; 

struct sNode{
   int data;
   struct sNode *next;
};

typedef struct sNode sNode;  
  
void push(sNode** top_ref, int new_data){

  sNode* new_node =(struct sNode*) malloc(sizeof(struct sNode));
  
  if(new_node == NULL){
     printf("Stack overflow \n");
     getchar();
     exit(0);
  }            
  
  new_node->data  = new_data;
  new_node->next = (*top_ref);   
  (*top_ref)    = new_node;
}

int pop(sNode** top_ref){
  int res;
  sNode *top;
  
  if(*top_ref == NULL){
     printf("Stack overflow \n");
     getchar();
     exit(0);
  }
  else{
     top = *top_ref;
     res = top->data;
     *top_ref = top->next;
     free(top);
     return res;
  }
}
  

int main(){
   sNode *s =NULL;
   push(&s,1);
   push(&s,2);
   push(&s,3);

   cout<<pop(&s);
}
