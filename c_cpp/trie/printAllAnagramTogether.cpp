#include <iostream>
#include <string.h>
#include <ctype.h>
#include <list>
#include <stdlib.h>

using namespace std;
 
#define NO_OF_CHARS 26
 


struct TrieNode{
    bool isEnd;  
    struct TrieNode* child[NO_OF_CHARS]; 
    list<int> l; 
};
 

struct TrieNode* newTrieNode(){
    struct TrieNode* temp = new TrieNode;
    temp->isEnd = 0;
    for (int i = 0; i < NO_OF_CHARS; ++i)
        temp->child[i] = NULL;
    return temp;
}
 
int compare(const void* a, const void* b){  return *(char*)a - *(char*)b; }
 

void insert(struct TrieNode** root, char* word, int index){
    if (*root == NULL)
        *root = newTrieNode();
 
    if (*word != '\0')
        insert( &( (*root)->child[tolower(*word) - 'a'] ), word+1, index );
    else{ 
        (*root)->l.push_back(index);
        (*root)->isEnd = 1;
    } 
}
 

void printAnagramsUtil(struct TrieNode* root, char *wordArr[]){
    if (root == NULL) return;
    list<int>::iterator i;
    if (root->isEnd){
        for (i=root->l.begin(); i != root->l.end(); ++i)
            cout<<wordArr[*i]<<endl;
    }
    for (int i = 0; i < NO_OF_CHARS; ++i)
        printAnagramsUtil(root->child[i], wordArr);
}
 

void printAnagramsTogether(char* wordArr[], int size){
    struct TrieNode* root = NULL;
 
    for (int i = 0; i < size; ++i){
        int len = strlen(wordArr[i]);
        char *buffer = new char[len+1];
        strcpy(buffer, wordArr[i]);
        qsort( (void*)buffer, strlen(buffer), sizeof(char), compare );
        insert(&root,  buffer, i);
    }

    printAnagramsUtil(root, wordArr);
}
 
 
int main(){
    char* wordArr[] = {"cat", "dog", "tac", "god", "act", "gdo"};
    int size = sizeof(wordArr) / sizeof(wordArr[0]);
    printAnagramsTogether(wordArr, size);
    return 0;
}