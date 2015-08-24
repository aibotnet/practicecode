#include<iostream>
using namespace std;

//O(2logn) approach
int searchElementInBitonicArrayUtil(int arr[],int start,int end, int el){
	int mid= start+(end-start)/2;
	if(start>end) return 0;
	if(arr[mid]==el) return 1;
	// else if(arr[mid] < el){return searchElementInBitonicArrayUtil(arr,mid+1,end,el);}
	// else{
	// 	return searchElementInBitonicArrayUtil(arr,start,mid-1,el)
	// 			||searchElementInBitonicArrayUtil(arr,mid+1,end,el);
	// }	
}

int searchElementInBitonicArray(int arr[],int n, int el){
	return searchElementInBitonicArrayUtil(arr,0,n-1, el);
}

int main(){
	int arr[] = {1,2,3,4,5,6,11,14,24,20,17,6,5};
	cout<<searchElementInBitonicArray(arr,sizeof(arr)/sizeof(int),2)<<endl;
}
