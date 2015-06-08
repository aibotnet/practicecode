#include<iostream>
#include<stdlib.h>
#include<limits.h>
using namespace std;


int minimum(int a ,int b){if(a<b) return a;return b;}

/*
	//second approach
	for(int i=1;i<n;i++){
		for(int j=0;j<i;j++){
			if(arr[j]>=(i-j)){
				if( (minStep[j]+1) < minStep[i] )
					minStep[i]=minStep[j]+1;
			}
		}
	}
*/

//dinamic programming o(n*n) approach
int minJumDP(int arr[], int n){
	int minStep[n];
	if (n==0 || arr[0]==0)
		return INT_MAX;

	for(int i=0;i<n;i++) minStep[i]=INT_MAX;
	minStep[n-1]=1;
	for(int i=n-2;i>=0;i--){
		for(int j=1;j<=arr[i];j++){
			if((i+j) >= n) break;
			minStep[i]=minimum(minStep[i], minStep[i+j]);
		}
		minStep[i]+=1;
	}

	return minStep[0];
}

int main(){
	int  arr[] = {5,6,7,4,1,4,3,9,5};
	cout<<"minimum no of jump required : "<<minJumDP(arr,sizeof(arr)/sizeof(int))<<endl;
	return 0;
}
