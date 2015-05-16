#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

//o(n) approach
void findMissingInAp2(int arr[],int f, int l){
	cout<<f<<" "<<l<<endl;
	int mid,d1,d2;
	if( (f==l)  || (f+1==l)) return;
	d1 = arr[f+1]-arr[f];
	d2 = arr[f+2]-arr[f+1];
	if((f+2==l) || (d1!=d2)){
		if(d1 > d2) {cout<<arr[f]+d2;return;}
		else {cout<<arr[f+1]+d1;return;}
	}
	mid = f + (l-f)/2;
	int val = arr[f] + d1 * ((l-f)/2); 
	if (arr[mid] == val)
		return findMissingInAp2(arr,mid+1,l);
	else
		return findMissingInAp2(arr,f,mid-1);
}

//o(n) approach
void findMissingInAp1(int arr[],int n){
	int i,d1,d2;
	if(n<=2) return;
	d1 = arr[1]-arr[0]; 
	for(i=2;i<n;i++){
		d2=arr[i]-arr[i-1];
		if(d1==d2) continue;

		if(i > 3){cout<<arr[i-1]+d1;return;}
		if(d1 > d2) {cout<<arr[i-1]-d2;return;}
		else {cout<<arr[i-1]+d1;return;}
	}
return;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int arr[] = {1,3,5,7,9,11,13,15,17,19,23,25,27,29};
    //findMissingInAp1(arr,sizeof(arr)/4);
    findMissingInAp2(arr,0,(sizeof(arr)/4)-1);
return 0;
}
