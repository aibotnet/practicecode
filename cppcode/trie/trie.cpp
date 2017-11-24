#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
#define ARRAY_SIZE(a) sizeof(a)/sizeof(a[0])
#define ALPHABET_SIZE (26)
#define CHAR_TO_INDEX(c) ((int)c - (int)'a')
#define FREE(p) free(p); p = NULL;

 
struct trie_node{
    bool flag;
    trie_node *child[ALPHABET_SIZE];
};
 
struct trie{
    trie_node *root;
    int count;
};

trie_node *getNode(void){
    trie_node *pNode = new trie_node;
    pNode->flag = false;
    for(int i = 0; i < ALPHABET_SIZE; i++)
        pNode->child[i] = NULL;
    return pNode;
}
 
void initialize(trie *pTrie){
    pTrie->root = getNode();// Initializes trie (root is dummy node)
    pTrie->count = 0;
}
 

void insert(trie *pTrie, char key[]){
    int index;
    int length = strlen(key);
    trie_node *temp = pTrie->root;
    pTrie->count++;
 
    for(int level = 0; level < length; level++ ){
        index = CHAR_TO_INDEX(key[level]);
        if( !temp->child[index] ){
            temp->child[index] = getNode();
        }
        temp = temp->child[index];
    }
    temp->flag = true; // mark last node as leaf
}

int search(trie *pTrie, char key[]){
    int length = strlen(key);
    int index;
    trie_node *temp= pTrie->root;
 
    for(int level = 0; level < length; level++ ){
        index = CHAR_TO_INDEX(key[level]);
        if( !temp->child[index] )
            return 0;
        temp = temp->child[index];
    }
    return (0 != temp && temp->flag);
}

bool leafNode(trie_node *pNode){return pNode->flag;}
 
bool isItFreeNode(trie_node *temp){
    for(int i = 0; i < ALPHABET_SIZE; i++)
        if( temp->child[i] ) return false; 
    return true;
}
 
bool deleteHelper(trie_node *pNode, char key[], int level, int len){
    if( pNode ){
        if( level == len ){
            if( pNode->flag ){
                pNode->flag = false;// Unmark leaf node
                if( isItFreeNode(pNode) )
                    return true;
                return false;
            }
        }
        else {
            int index = CHAR_TO_INDEX(key[level]);
 
            if( deleteHelper(pNode->child[index], key, level+1, len) ){
                FREE(pNode->child[index]);// last node marked, delete it
 
                // recursively climb up, and delete eligible nodes
                return ( !leafNode(pNode) && isItFreeNode(pNode) );
            }
        }
    }
    return false;
}
 
void deleteKey(trie *pTrie, char key[]){
    int len = strlen(key);
    if( len > 0 ){
        deleteHelper(pTrie->root, key, 0, len);
    }
}

// Driver
int main(){
    char keys[][8] = {"the", "a", "there", "answer", "any", "by", "bye", "their"};
    trie mtrie;
    char output[][32] = {"Not present in trie", "Present in trie"};
 
    initialize(&mtrie);

    for(int i = 0; i < ARRAY_SIZE(keys); i++){
        insert(&mtrie, keys[i]);
    }
 
    // Search for different keys
    printf("%s --- %s\n", "the", output[search(&mtrie, "the")] );
    printf("%s --- %s\n", "these", output[search(&mtrie, "these")] );
    printf("%s --- %s\n", "their", output[search(&mtrie, "their")] );
    printf("%s --- %s\n", "thaw", output[search(&mtrie, "thaw")] );
    
    deleteKey(&mtrie, "their");
    printf("%s --- %s\n", "their", output[search(&mtrie, "their")] );

    return 0;
}