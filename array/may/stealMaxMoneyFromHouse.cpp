#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <limits.h>

using namespace std;

int compare(int a, int b){if(a>b) return a;return b;}
//time complexity O(nlogn) using sorting
int stealMaxMoneyFromHouse2(int arr[],int n){
	int amount = 0 ;
	sort(arr,arr+n,compare);
	for(int i=n-1;i>=0;i-=2) amount+=arr[i];
	return amount;		
}


//time complexity O(2^n)
int stealMaxMoneyFromHouse1(int arr[],int f, int l){
	if(f>l) return 0;
	if(f==l) return arr[f];

	return max(arr[f]+stealMaxMoneyFromHouse1(arr,f+2,l) 
		, arr[f+1]+stealMaxMoneyFromHouse1(arr,f+3,l));
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int arr[] = {1,2,3,4,15,6};
    cout<<stealMaxMoneyFromHouse1(arr,0,(sizeof(arr)/sizeof(int) -1))<<endl;
    cout<<stealMaxMoneyFromHouse2(arr,sizeof(arr)/sizeof(int))<<endl;
return 0;
}
