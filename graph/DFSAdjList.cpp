#include<iostream>
#include <list>
 
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
 
void DFSUtil(int v, bool visited[]){
    // Mark the current node as visited and print it
    visited[v] = true;
    cout << v << " ";
 
    // Recur for all the vertices adjacent to this vertex
    list<int>::iterator i;
    for(i = g.adj[v].begin(); i != g.adj[v].end(); ++i)
        if(!visited[*i])
            DFSUtil(*i, visited);
}
 
// DFS traversal of the vertices reachable from v. It uses recursive DFSUtil()
void DFS(int v){
    // Mark all the vertices as not visited
    bool *visited = new bool[g.v];
    for(int i = 0; i < g.v; i++)
        visited[i] = false;
    // Call the recursive helper function to print DFS traversal
    DFSUtil(v, visited);
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
    DFS(2);
 
    return 0;
}
