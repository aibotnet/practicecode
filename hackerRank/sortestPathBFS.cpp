#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <list>
#include <queue> 
using namespace std;


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
    g.adj[w].push_back(v);
}
 
 
void BFS(int s){
    bool *visited = new bool[g.v];int s1=s;
     for(int i = 0; i < g.v; i++)
        visited[i] = false;

    int *d = new int[g.v];
    for(int i = 0; i < g.v; i++)
        d[i] = 0;
    
    queue<int> q;
    visited[s] = true;

    list<int>::iterator i; 
    for(i = g.adj[s].begin(); i != g.adj[s].end(); ++i){
        visited[*i] = true;
        d[*i]=6;
        q.push(*i);
    }

    while(!q.empty()){
        s = q.front();
        q.pop();
        for(i = g.adj[s].begin(); i != g.adj[s].end(); ++i){
            if(!visited[*i]){
                visited[*i] = true;
                d[*i]=d[s]+6;
                q.push(*i);
            }
        }
    }

    for(int i = 0; i < g.v; i++){
        if(i==s1) continue;
        if(!visited[i]) cout<<"-1 ";
        else cout<<d[i]<<" ";
    }
    
    cout<<endl;
}


int main() {
    long t,n,m,x,y,s;
    int i=3;
    cin>>t;
    while(t){
        cin>>n;
        cin>>m;
        initialize(n);
        while(m){
            cin>>x>>y;
            addEdge(x-1,y-1);
            m-=1;
        }
        cin>>s;
        BFS(s-1);
        t-=1;
    }
    return 0;
}
