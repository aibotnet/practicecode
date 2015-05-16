#include <iostream>
#include <stdlib.h>
#include <limits.h>
#include <algorithm>

using namespace std;

void nextGreaterNumberWithSameSetOfDigit(int number[],int n){
	int i;
	for(i=n-1;i>0;i--)
		if(number[i-1]<number[i])
			break;
	if(i==0){cout<<"Not Possible"<<endl;return;}

	//find smallest digit in right side
	int smallest_index=i;
	for(int j=i+1;j<n;j++){
		if(number[j] < number[smallest_index])
			smallest_index=j;
	}
	cout<<smallest_index<<endl;
	int temp = number[i-1];number[i-1]=number[smallest_index];number[smallest_index]=temp;
	sort(number+i,number+n);

	for(int i=0;i<n;i++) cout<<number[i]<<" ";
}

int main(){
	int  number[] = {5,4,3,9,8,7,6,5};
	nextGreaterNumberWithSameSetOfDigit(number,sizeof(number)/sizeof(int));
return 0;
}
