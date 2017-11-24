#include<iostream>
#include<stdlib.h>
using namespace std;

//global variable v shows no of vertices
int v=5;


//Recursive DFS traversal Time Complexity O(v*v)
void DFS(int graph[][5], int s, int visited[]){
	visited[s]=1;
	cout<<s<<" ";
	for(int i=0;i<v;i++){
		if(graph[s][i]==1 && visited[i]==0){
			DFS(graph,i,visited);
		}
	}
}

//This method is used when all part of graph is not connected
void DFSTraversal(int graph[][5]){
	int visited[5];
	for(int i=0;i<v;i++) visited[i]=0;
	for(int i=0;i<v;i++){
		if (visited[i]==0)
			DFS(graph,i,visited);
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
	DFSTraversal(graph);
}
