#include<iostream>
using namespace std;

void swap(int arr[],int f,int s){int temp=arr[s];arr[s]=arr[f];arr[f]=temp;}

void maxHeapify(int arr[],int i,int n){
	int lh=i*2,rh=lh+1;
	int minindex=i;
	if( (lh < n) && (arr[minindex] < arr[lh])){minindex=lh;}
	if( (rh < n) && (arr[minindex] < arr[rh])){minindex=rh;}
	if(i==minindex) return;
	swap(arr,i,minindex);
	maxHeapify(arr,minindex,n);
}

void createHeap(int arr[], int n){
	for(int i=n/2;i>=0;i--){maxHeapify(arr,i,n);}
}
void extractMax(int heap[], int n){
	swap(heap,0,n-1);
	maxHeapify(heap,0,n-1);
}

int heapSort(int *arr,int n){
	createHeap(arr,n);
	while(n){extractMax(arr,n);n--;}
}

int main(){
	int  arr[] = {10,9,8,7,6,5,4,3,2,1};
	int n = sizeof(arr)/sizeof(arr[0]);
	heapSort(arr,n);
	for(int i=0;i<n ;i++)
		cout<<arr[i]<<endl;
}
