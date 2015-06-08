#include <iostream>
#include <stdlib.h>
#include <limits.h>
#include <algorithm>

using namespace std;

void nextSmallerNumberWithSameSetOfDigit(int number[],int n){
	int i;
	for(i=n-1;i>0;i--)
		if(number[i-1]>number[i])
			break;
	if(i==0){cout<<"Not Possible !!!"<<endl;return;}

	//find smallest digit in right side
	int largest_index=i;
	for(int j=i+1;j<n;j++){
		if(number[j] > number[largest_index])
			largest_index=j;
	}
	cout<<largest_index<<endl;
	int temp = number[i-1];number[i-1]=number[largest_index];number[largest_index]=temp;
	sort(number+i,number+n,greater<int>());

	for(int i=0;i<n;i++) cout<<number[i]<<" ";
}

int main(){
	int  number[] = {1,2,3,4,5,6,7};
	nextSmallerNumberWithSameSetOfDigit(number,sizeof(number)/sizeof(int));
return 0;
}
