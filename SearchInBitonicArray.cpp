#include<iostream>
#include<stdlib.h>
#include<stdbool>
using namespace std;

bool searchElementInBitonicArrayUtil(int arr[],int start,int end){
		
}

bool searchElementInBitonicArray(int arr[],int n){
	return searchElementInBitonicArrayUtil(arr,0,n-1);
}

int main(){
	int arr = [1,2,3,4,5,6,11,14,24,20,17,6,5];
	searchElementInBitonicArray(arr,sizeof(arr)/sizeof(int));
}
