#include<iostream>
#include<stdlib.h>
using namespace std;

int printarray(int arr[], int f ,int n){
	for(int i=f;i<=n;i++){
		cout<<arr[i]<<" ";
	}
	cout<<endl;
}


void swap(int arr[], int i , int j){
	int temp = arr[i];
	arr[i]=arr[j];
	arr[j]=temp;
}

int partition(int arr[], int start, int end){
	int mid = start+(end-start)/2;
	int i,j,key;
	key=arr[end];i=start-1;j=start;
	
	while(j<end){
		if(arr[j]<key){
			swap(arr, i+1,j);i++;
		}j++;
	}
	swap(arr, i+1, end);
	printarray(arr,start,end);
	return i+1; 
}
int _findkthsmallestElement(int *arr,int low , int high, int k){
	if (low==high)
		return arr[low];
	cout<<"Value of k is : "<<k<<endl;
	int pivot_index = partition(arr, low, high);
	cout<<"Returned pivot_index is : "<<pivot_index<<endl;
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
	int  arr[] = {2,3,5,-1,7,6,3,9,2,4,-3,-6,11};
	cout<<"kth sm is : "<<findkthsmallestElement(arr,sizeof(arr)/sizeof(int)-1, 4)<<endl;
	return 0;
}
