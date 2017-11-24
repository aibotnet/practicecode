
#include<iostream>
#include<string.h>
#include<stdbool.h>
using namespace std;

void nextgreaterPalindromeUtil(int *numArr,int n){
	bool leftSmaller=false;
	int mid=n/2,i=mid-1,j;
	if(n%2==1)j=mid+1;
	else j=mid;
	
	while(i>=0 && numArr[i]==numArr[j]){
		i--;j++;
	}
	//number is already palindrome 
	//or left side of number is smaller than it's right side for each i
	if(i<0 || numArr[i] < numArr[j])
		leftSmaller=true;
	while(i>=0){
		numArr[j]=numArr[i];
		i--;j++; //copying left side to right side
	}
	if(leftSmaller){
		int carry=1;i=mid-1;
		if(n%2==1){
			numArr[mid]+=carry;
			carry=numArr[mid]/10;
			numArr[mid]%=10;
			j=mid+1;
		}
		else j=mid;
		while(i>=0){
			numArr[i]+=carry;
			carry=numArr[i]/10;numArr[i]%=10;
			numArr[j]=numArr[i];i--;j++;
		}
	}	
	
	for (int k=0;k<n;k++)
		cout<<numArr[k]<<" ";
}
void nextgreaterPalindrome(int *numArr,int n){
	//check for all 9
	for(int i=0;i<n;i++)
		if(numArr[i]!=9)
			break;
	//if(i==n){
	//handle for all 9
	//}
	nextgreaterPalindromeUtil(numArr,n);
}

int main(){
	int numArr[]={1,0,0,0};
	nextgreaterPalindrome(numArr,4);
	return 0;
}
