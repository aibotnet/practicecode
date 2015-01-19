/*
 * count total no of inversion in array.(merge sort approach)
 */
#include <iostream>
#include <stdlib.h>
#include <limits.h>
#include <algorithm>

using namespace std;

int mergeArray(int number[],int temprory[],int start,int mid,int end){
	int i,j,inversions=0,k=start;
	i=start;j=mid+1;
	while(i<=mid && j<=end){
		if(number[i]<=number[j]){//there is no inversion if elements are same.
			temprory[k++]=number[i];i++;
		}else{
			temprory[k++]=number[j];j++;
			inversions+=(mid-i+1);
		}
	}
	while(i<=mid) temprory[k++]=number[i++]; //  element left in left side of array
	while(j<=end) temprory[k++]=number[j++]; //  element left in right side of array
	for(int i=start; i<=end;i++) number[i]=temprory[i];//copying sorted part to original array.
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
	int tempArr[n];//used for temprory storage during merge sort
	return _countInversionMergeSort(number,tempArr,0,n-1);
}

int main(){
	int  number[] = {5,4,3,9,8,7,6,5};
	cout<<"Total Inversion in this array : "<<countInversion(number,sizeof(number)/sizeof(int))<<endl;

	for(int i=0;i<(sizeof(number)/sizeof(int));i++)
		cout<<number[i]<<" ";
return 0;
}
