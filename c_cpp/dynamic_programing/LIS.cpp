#include<iostream>
#include<stdlib.h>
#include<limits.h>
using namespace std;

int maximum(int a ,int b){
	if(a>b) return a;return b;
}

//dinamic programming o(n*n) approach
int LIS(int arr[], int n){
	int lis[n];
	for(int i=0;i<n;i++) lis[i]=0;
	lis[n-1]=1;
	for(int i=n-2;i>=0;i--){
		for(int j=i+1;j<n;j++){
			if(arr[i] < arr[j])
				lis[i]=maximum(lis[i],lis[j]);
		}
		lis[i]+=1;
	}
	for(int i=1;i<n;i++)
		lis[0]=maximum(lis[0],lis[i]);

	return lis[0];
}

int main(){
	int  arr[] = {5,6,7,-4,-1,0,3,9,-5,11};
	cout<<"maximum sum subarray : "<<LIS(arr,sizeof(arr)/sizeof(int))<<endl;
	return 0;
}
