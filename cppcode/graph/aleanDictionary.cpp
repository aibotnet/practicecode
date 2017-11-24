// A C++ program to order of characters in an alien language
#include<iostream>
#include <list>
#include <stack>
#include <cstring>
using namespace std;
 

class Graph{
    int V;   
    list<int> *adj;

    void topologicalSortUtil(int v, bool visited[], stack<int> &Stack){
        visited[v] = true;
     
        list<int>::iterator i;
        for (i = adj[v].begin(); i != adj[v].end(); ++i)
            if (!visited[*i])
                topologicalSortUtil(*i, visited, Stack);
     
        Stack.push(v);
    }
    public:
        Graph(int V){
            this->V = V;
            adj = new list<int>[V];
        }
     
        void addEdge(int v, int w){
            adj[v].push_back(w);
        }
     
        void topologicalSort(){
            stack<int> Stack;
            bool *visited = new bool[V];
            for (int i = 0; i < V; i++) // Mark all the vertices as not visited
                visited[i] = false;
         
            for (int i = 0; i < V; i++)
              if (visited[i] == false)
                topologicalSortUtil(i, visited, Stack);
         
            while (Stack.empty() == false){
                cout << (char) ('a' + Stack.top()) << " ";
                Stack.pop();
            }
        }
};
 

int min(int x, int y){
    return (x < y)? x : y;
}
 
// For simplicity, this function is written in a way that only
// first 'alpha' characters can be there in words array.  For
// example if alpha is 7, then words[] should have only 'a', 'b',
// 'c' 'd', 'e', 'f', 'g'
void printOrder(string words[], int n, int alpha){
    Graph g(alpha);
 
    for (int i = 0; i < n-1; i++){
        // Take the current two words and find the first mismatching
        // character
        string word1 = words[i], word2 = words[i+1];
        for (int j = 0; j < min(word1.length(), word2.length()); j++){
            // If we find a mismatching character, then add an edge
            // from character of word1 to that of word2
            if (word1[j] != word2[j]){
                g.addEdge(word1[j]-'a', word2[j]-'a');
                break;
            }
        }
    }

    g.topologicalSort();
}
 
// Driver program to test above functions
int main()
{
    string words[] = {"baa", "abcd", "abca", "cab", "cad"};
    printOrder(words, 5, 4);
    return 0;
}