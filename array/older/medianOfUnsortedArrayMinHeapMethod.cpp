#include<iostream>
#include<stdlib.h>
using namespace std;

void swap(int arr[],int f,int s){
	int temp=arr[s];arr[s]=arr[f];arr[f]=temp;
}
void minHeapify(int arr[],int i,int n){
	int lh=i*2,rh=lh+1;
	int minindex=i;
	if( (lh < n) && (arr[minindex] > arr[lh])){minindex=lh;}
	if( (rh < n) && (arr[minindex] > arr[rh])){minindex=rh;}
	if(i==minindex) return;
	swap(arr,i,minindex);
	minHeapify(arr,minindex,n);
}

void createHeap(int arr[], int n){
	//Convert this array to min heap of size n --> time complexity = O(n)
	for(int i=n/2;i>=0;i--){
		minHeapify(arr,i,n);
	}
	for(int i=0;i<n;i++){
		cout<<arr[i]<<"\n";
	}
}
void deleteMin(arr, n){
	arr[0]=arr[n-1];
	minHeapify(arr,0,n);
}
int medianOfUnsortedArrayMinHeapMethod(int *arr,int n){
	createHeap(arr, n);
	if(n%2==1){
		
	}
	else{
		
	}	
}

int main(){
	int  arr[] = {10,9,8,7,6,5,4,3,2,1};
	cout<<"Median is : "<<medianOfUnsortedArrayMinHeapMethod(arr, sizeof(arr)/sizeof(int))<<endl;
}
