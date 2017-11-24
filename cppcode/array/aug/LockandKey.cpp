#include<iostream>
#include<math.h>

using namespace std;

void mswap(int arr[],int i, int j){
  int temp = arr[i];
  arr[i]=arr[j];
  arr[j]=temp;
}
int  partition(int arr[],int f,int l,int key){
  int i=f-1,j=f;
  while(j<l){
      if(arr[j]<key){
        i++;mswap(arr,i,j);
      }else if(arr[j]==key){
        mswap(arr,j,l);j--;
      }
      j++;
  }
  mswap(arr,i+1,l);return i+1;
}

void matchPairs(int nuts[],int bolts[] ,int f, int l){
  if(f>l) return;
  int pi = partition(nuts ,f,l,bolts[l]);
  partition(bolts,f,l,nuts[pi]);
  matchPairs(nuts,bolts,f,pi-1);
  matchPairs(nuts,bolts,pi+1,l);
}

int main(){
  int arr1[] = {1,3,-1,0,5,-6};
  int arr2[] = {5,-6,-1,3,1,0};
  int n = sizeof(arr2)/sizeof(arr2[0]);
  matchPairs(arr1,arr2,0,n-1);
  for(int i=0;i<n;i++)
    cout<<arr1[i]<<"\t"<<arr2[i]<<endl;
}
