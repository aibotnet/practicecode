#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <limits.h>

using namespace std;


//Dp solution o(n) without using extra memory
int stealMaxMoneyFromHouse2(int arr[], int n){
	if(n==1) return arr[0];
	else if(n==2) return max(arr[0],arr[1]);
	int p,pp,temp; pp=arr[0];p= max(arr[0],arr[1]);
	for(int i=2;i<n;i++){
		temp = max(arr[i]+pp , p);
		pp=p;p=temp;
	}
	return temp;
}


//time complexity O(2^n)
// T(n) = max( a[i]+T(n-2) , T(n-1))
int stealMaxMoneyFromHouse1(int arr[],int f, int l){
	if(f>l) return 0;
	if(f==l) return arr[f];

	return max(arr[f]+stealMaxMoneyFromHouse1(arr,f+2,l)
		, stealMaxMoneyFromHouse1(arr,f+1,l));
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int arr[] = {11,2,3,12,15,10};
    cout<<stealMaxMoneyFromHouse1(arr,0,(sizeof(arr)/sizeof(int) -1))<<endl;
		cout<<stealMaxMoneyFromHouse2(arr,(sizeof(arr)/sizeof(int)))<<endl;
return 0;
}
