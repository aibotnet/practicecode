#include<iostream>
#include<stdlib.h>
#include<limits.h>
using namespace std;

int findCeilIndex(int arr[], int l , int r, int key){

}

int maximum(int a ,int b){
	if(a>b) return a;return b;
}
//dinamic programming o(n*n) approach
int LIS_NLOGN(int arr[], int n){
	int lis[n];
}

int main(){
	int  arr[] = {5,6,7,-4,-1,0,3,9,-5,11};
	cout<<"maximum sum subarray : "<<LIS_NLOGN(arr,sizeof(arr)/sizeof(int))<<endl;
	return 0;
}
