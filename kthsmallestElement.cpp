#include<iostream>
#include<stdlib.h>
using namespace std;

int printarray(int arr[], int n){
	for(int i=0;i<n;i++){
		cout<<arr[i]<<" ";
	}
}


void swap(int arr[], int i , int j){
	cout<<i <<" "<<j<<endl;
	printarray(arr,9);
	cout<<endl;
	int temp = arr[i];
	arr[i]=arr[j];
	arr[j]=temp;
	printarray(arr,9);
	cout<<endl;
}

int partition(int arr[], int start, int end){
	int mid = start+(end-start)/2;
	int i,j,key;
	swap(arr, mid,end);
	key=arr[end];
	i=start-1;
	j=start;
	
	while(j<end){
		if(arr[j]<key){
			swap(arr, i+1,j);
			i++;
		}
		j++;
	}
	swap(arr, i+1, end);
	return i+1; 
}
int _findkthsmallestElement(int *arr,int low , int high, int k){
	if (low==high)
		return arr[low];
	int pivot_index = partition(arr, low, high);
	int left_size = pivot_index-low+1;
	if (k<left_size)
		return _findkthsmallestElement(arr,low, pivot_index-1,k);
	else if (k > left_size)
		return _findkthsmallestElement(arr,pivot_index+1, high,k-left_size);
	else
		return arr[pivot_index];
}
int findkthsmallestElement(int *arr,int n, int k){
	return _findkthsmallestElement(arr,0, n,k);
}

int main(){
	int  arr[] = {12,13,6,-1,4,0,7,9,5};
	cout<<findkthsmallestElement(arr,sizeof(arr)/sizeof(int) , 6);
	return 0;
}
