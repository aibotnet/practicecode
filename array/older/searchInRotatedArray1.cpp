#include<iostream>
#include<stdlib.h>
using namespace std;

//Searching element without finding pivot index
//time compexity increase to O(3logn) -> O(logn)
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

int searchElementInRotatedAndPivotedArray(int *arr,int number, int n){

}

int main(){
	int  arr[] = {4,5,6,7,8,9,1,2,3};
	cout<<searchElementInRotatedAndPivotedArray(arr,6, sizeof(arr)/sizeof(int));
}
