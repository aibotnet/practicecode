#include<iostream>
#include<string.h>
#include<stdbool.h>
using namespace std;

void justSmallerPalindromeUtil(int *numArr,int n){
	bool leftGreater=false;
	int mid=n/2,i=mid-1,j;
	if(n%2==1)j=mid+1;else j=mid;
	while(i>=0 && numArr[i]==numArr[j]){i--;j++;}
	
	//number is already palindrome 
	//or left side of number is smaller than it's right side for each i
	if(i<0 || numArr[i] > numArr[j]) leftGreater=true;
	while(i>=0){
		numArr[j]=numArr[i];
		i--;j++; //copying left side to right side
	}
	
	if(leftGreater){
		int carry=-1;i=mid-1;
		if(n%2==1){
			numArr[mid]+=carry;
			if (numArr[mid] <0){carry=-1;numArr[mid]=9;}else carry=0;	
		    j=mid+1;
		}else j=mid;
		
		while(i>=0){
			numArr[i]+=carry;
			if (numArr[i] <0){
				carry=-1;numArr[i]=9;
			}else carry=0;
			numArr[j]=numArr[i];
			i--;j++;
		}
	}	
	
	for (int k=0;k<n;k++)
		cout<<numArr[k]<<" ";
}
void justSmallerPalindrome(int *numArr,int n){
	//check for all 100,1000 like pattern
	for(int i=0;i<n;i++){
		if(i==0){
			if(numArr[i]!=1)
				break;
		}else{
			if(numArr[i]!=0)
				break;
		}
	}
	justSmallerPalindromeUtil(numArr,n);
}

int main(){
	int numArr[]={9,9,9,9};
	justSmallerPalindrome(numArr,4);
	return 0;
}
