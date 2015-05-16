#include<iostream>
#include<stdlib.h>
#include<stdbool>
using namespace std;

bool searchElementInBitonicArrayUtil(int arr[],int start,int end, int el){
	int mid= start+(end-start)/2;
	if(start>end) return false;
	if(arr[mid]==el) return true;	
}

bool searchElementInBitonicArray(int arr[],int n, int el){
	return searchElementInBitonicArrayUtil(arr,0,n-1, el);
}

int main(){
	int arr = [1,2,3,4,5,6,11,14,24,20,17,6,5];
	searchElementInBitonicArray(arr,sizeof(arr)/sizeof(int),2);
}
