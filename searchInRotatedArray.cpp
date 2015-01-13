#include<iostream>
#include<stdlib.h>
using namespace std;

int binarySearch(int arr[], int x, int f , int l){
	if (f>l)
		return -1;
	int mid = f+(l-f)/2;
	if (arr[mid] == x)
		return x;
	else if(arr[mid] > x)
		return binarySearch(arr, x, f, mid-1);
	else
		return binarySearch(arr, x, mid+1, l);
}

int pivotIndex(int arr[], int f , int l){
	if (f>l)
		return -1;
	int mid = f +(l-f)/2;
	
	if (mid < l && arr[mid] > arr[mid+1])
		return mid;
	if (mid > l && arr[mid-1] > arr[mid])
		return mid-1;
	
	if(arr[f] > arr[mid])
		return pivotIndex(arr,f,mid-1);
	else
		return pivotIndex(arr,mid+1,l);
}

int convertRomanString(int *arr,int number, int n){
	
	int pivot_index= pivotIndex(arr,0,n-1);
	if (pivot_index == -1)
		return binarySearch(arr,number, 0 , n-1);
	
	if(arr[pivot_index] == number)
		return number;
	if(arr[pivot_index] > number)
		return binarySearch(arr,number, 0 , pivot_index-1);
	else
		return binarySearch(arr,number,pivot_index+1,n-1);
}

int main(){
	int  arr[] = {4,5,6,7,8,9,1,2,3};
	cout<<convertRomanString(arr,6, sizeof(arr)/sizeof(int));
}
