#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ARRAY_SIZE(a) sizeof(a)/sizeof(a[0])
#define ALPHABET_SIZE (26) // Alphabet size (# of symbols)
// Converts key current character into index
// use only 'a' through 'z' and lower case
#define CHAR_TO_INDEX(c) ((int)c - (int)'a')
 
// trie node
typedef struct trie_node trie_node_t;
struct trie_node{
    int value;
    trie_node_t *children[ALPHABET_SIZE];
};
// trie ADT
typedef struct trie trie_t;
struct trie{
    trie_node_t *root;
    int count;
};
// Returns new trie node (initialized to NULLs)
trie_node_t *getNode(void)
{
    trie_node_t *pNode = NULL;
 
    pNode = (trie_node_t *)malloc(sizeof(trie_node_t));
 
    if( pNode )
    {
        int i;
 
        pNode->value = 0;
 
        for(i = 0; i < ALPHABET_SIZE; i++)
        {
            pNode->children[i] = NULL;
        }
    }
 
    return pNode;
} 
// Initializes trie (root is dummy node)
void initialize(trie_t *pTrie)
{
    pTrie->root = getNode();
    pTrie->count = 0;
}
 
// If not present, inserts key into trie
// If the key is prefix of trie node, just marks leaf node
void insert(trie_t *pTrie, char key[]){
    int level;int length = strlen(key);
    int index;trie_node_t *temp;
 
    pTrie->count++;
    temp = pTrie->root;
    for( level = 0; level < length; level++ ){
        index = CHAR_TO_INDEX(key[level]);
        if( !temp->children[index] ){
            temp->children[index] = getNode();
        }
        temp = temp->children[index];
    }
    temp->value = pTrie->count;// end of word
}
 
// Returns non zero, if key presents in trie
int search(trie_t *pTrie, char key[]){
    int level;int length = strlen(key);
    int index;trie_node_t *temp;
 
    temp = pTrie->root;
    for( level = 0; level < length; level++ ){
        index = CHAR_TO_INDEX(key[level]);
        if( !temp->children[index] ){
            return 0;
        }
        temp = temp->children[index];
    }
    return (0 != temp && temp->value);
}
 
// Driver
int main(){
    // Input keys (use only 'a' through 'z' and lower case)
    char keys[][8] = {"the", "a", "there", "answer", "any", "by", "bye", "their"};
    trie_t trie;int i;
    char output[][32] = {"Not present in trie", "Present in trie"};
    initialize(&trie);
    // Construct trie
    for(i = 0; i < ARRAY_SIZE(keys); i++){
        insert(&trie, keys[i]);
    }
    // Search for different keys
    printf("%s --- %s\n", "the", output[search(&trie, "the")] );
    printf("%s --- %s\n", "these", output[search(&trie, "these")] );
    printf("%s --- %s\n", "their", output[search(&trie, "their")] );
    printf("%s --- %s\n", "thaw", output[search(&trie, "thaw")] );
 
    return 0;
}