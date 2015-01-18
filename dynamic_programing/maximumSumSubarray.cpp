#include<iostream>
#include<stdlib.h>
#include<limits.h>
using namespace std;


//kadensAlgorithm
int maximumSumSubarray(int *arr,int n){
	int max_sum=0,temp_sum=0;
	for(int i=0;i<n;i++){
		temp_sum+=arr[i];
		if(temp_sum<0) temp_sum=0;
		if(temp_sum>max_sum) max_sum=temp_sum;
	}
	return max_sum;
}

int maximum(int a ,int b){
	if(a>b) return a;return b;
}


//maximum sum subarray
int maximumSumSubarrayDP(int *arr,int n){
	int temp[n];
	int maxel=INT_MIN;
	temp[0]=arr[0];
	for(int i=1;i<n;i++)
		temp[i]=maximum(temp[i-1]+arr[i],arr[i]);
	
	for(int i=0;i<n;i++)
		maxel=maximum(maxel,temp[i]);
		
	return maxel;
}

int main(){
	int  arr[] = {-5,-2,6,-4,-1,7,3,-5,6};
	cout<<"maximum sum subarray : "<<maximumSumSubarrayDP(arr,sizeof(arr)/sizeof(int))<<endl;
	return 0;
}
