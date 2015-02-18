#include<iostream>
#include<stdlib.h>
#include<queue>
using namespace std;

//global variable v shows no of vertices
//global variable q[queue data structure]is used to store verices for BFS traversal
int v=5;
queue<int> q;


//Recursive BFS traversal Time Complexity O(v*v)
void BFS(int graph[][5], int s, int visited[]){
	visited[s]=1;
	cout<<s<<" ";
	for(int i=0;i<v;i++){
		if(graph[s][i]==1 && visited[i]==0){
			visited[i]=1;
			q.push(i);
		}
	}
	if(q.empty()) return;
	int new_vertex = q.front();q.pop();
	BFS(graph,new_vertex,visited);
}


//This method is used when all part of graph is not connected
void BSFTraversal(int graph[][5]){
	int visited[5];
	for(int i=0;i<v;i++) visited[i]=0;
	for(int i=0;i<v;i++){
		if (visited[i]==0)
			BFS(graph,i,visited);
	}
}
//graph is stored in array
int main(){
	int graph[5][5]={
		{0,1,0,1,0},
		{1,0,1,1,0},
		{0,1,0,1,1},
		{1,1,1,0,1},
		{0,0,1,1,0}	
	};
	BSFTraversal(graph);
}
