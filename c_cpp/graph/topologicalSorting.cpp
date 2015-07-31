#include<iostream>
#include <list>
#include <stack>
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
                cout << Stack.top() << " ";
                Stack.pop();
            }
        }
};
 

 
int main(){
    // Create a graph given in the above diagram
    Graph g(6);
    g.addEdge(5, 2);
    g.addEdge(5, 0);
    g.addEdge(4, 0);
    g.addEdge(4, 1);
    g.addEdge(2, 3);
    g.addEdge(3, 1);
 
    cout << "Following is a Topological Sort of the given graph \n";
    g.topologicalSort();
 
    return 0;
}