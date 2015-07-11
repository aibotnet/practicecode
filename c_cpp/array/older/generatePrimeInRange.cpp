#include<iostream>
#include<stdlib.h>
#include<string.h>

using namespace std;

void generatePrimeNumber(long x , long y){
	if(x< 2 && x > y) return;
	bool *arr = new bool[y+1];
	memset(arr,0,sizeof(bool)*(y+1));

	if(x==2) cout<<2<<endl;

	for(int i=3;i<=y;i+=2){
		if(arr[i] || (arr[i]%2==0)) continue;

		if(i>=x) if(arr[i]==0) cout<<i<<endl;
		
		for(int j=i;j<=y;j+=i){arr[j]=1;}
	}
}

int main(){
	long n,x,y;
	cin>>n;
	while(n>0){
		cin>>x;cin>>y;
		generatePrimeNumber(x,y);
		n--;	
	}
	return 0;
}
