#include <iostream>
#include <stdlib.h>
#include <limits.h>
#include <algorithm>
#include <string>
#include <stack>
#include <limits.h>

using namespace std;

int mergeArray(int number[],int temprory[],int start,int mid,int end){
	int i,j,inversions=0,k=start;
	i=start;j=mid+1;
	while(i<=mid && j<=end){
		if(number[i]<=number[j]){
			temprory[k++]=number[i];i++;
		}else{
			temprory[k++]=number[j];j++;
			inversions+=(mid-i+1);
		}
	}
	while(i<=mid) temprory[k++]=number[i++]; 
	while(j<=end) temprory[k++]=number[j++]; 
	for(int i=start; i<=end;i++) number[i]=temprory[i];
	return inversions;
}

int _countInversionMergeSort(int number[],int tempArr[],int start, int end){
	int a,b,mid;
	if(start < end){
		mid=start+(end-start)/2;
		a = _countInversionMergeSort(number,tempArr,start,mid);
		b = _countInversionMergeSort(number,tempArr,mid+1,end);
		return a+b+mergeArray(number,tempArr,start,mid,end);
	}
	return 0;
}

int  countInversion(int number[],int n){
	int tempArr[n];
	return _countInversionMergeSort(number,tempArr,0,n-1);
}


int main(){
	int n,a,b,max=INT_MIN;
	cin>>n;
	stack<int> s1,s2;
	while(n>0){
		cin>>a;cin>>b;
		if(a>max) max=a;
		if(b>max) max=b;
		s1.push(a);
		s2.push(b);
		n--;
	}

	int *mergeArray = new int[max];
	
	for(int i=0;i<max;i++){
		mergeArray[i]=i;
	}

	while(!s1.empty()){
		int temp=mergeArray[s1.top()-1];
		mergeArray[s1.top()-1]=mergeArray[s2.top()-1];
		mergeArray[s2.top()-1]=temp;
		s1.pop();s2.pop();
	}
	cout<<countInversion(mergeArray,max);
return 0;
}

