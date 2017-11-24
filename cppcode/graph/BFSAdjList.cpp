#include<iostream>
#include <list>
#include <queue> 
using namespace std;
 
// Graph class represents a directed graph using adjacency list representation
struct graph{
    int v;
    list<int> *adj;
}g;
 
 void initialize(int v){
    g.v=v;
    g.adj=new list<int>[v];
 }

void addEdge(int v, int w){
    g.adj[v].push_back(w); // Add w to v’s list.
}
 

 
void BFS(int s){
    bool *visited = new bool[g.v];
    for(int i = 0; i < g.v; i++)
        visited[i] = false;
    queue<int> q;
    visited[s] = true;
    q.push(s);

    list<int>::iterator i; 
    while(!q.empty()){
        s = q.front();
        cout << s << " ";
        q.pop();
        for(i = g.adj[s].begin(); i != g.adj[s].end(); ++i){
            if(!visited[*i]){
                visited[*i] = true;
                q.push(*i);
            }
        }
    }
}
 
int main(){
    // Create a graph given in the above diagram
    initialize(4);
    addEdge(0, 1);
    addEdge(0, 2);
    addEdge(1, 2);
    addEdge(2, 0);
    addEdge(2, 3);
    addEdge(3, 3);
 
    cout << "Following is Depth First Traversal (starting from vertex 2) \n";
    BFS(2);
 
    return 0;
}
