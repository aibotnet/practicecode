#include<iostream>
#include<stdlib.h>
#include<limits.h>
using namespace std;
int min(int a , int b){
	if(a<b)
		return a;
	return b;
}

int minimumcoinRequired(int *coin,int n , int amount){
	int *C =(int *)malloc(4*(n+1));
	for(int i=1;i<=amount;i++)
		C[i]=INT_MAX;
	C[0]=0;
	for(int i=1;i<=amount;i++){
		for(int j=0;j<n;j++){
			if (coin[j]>i)continue;
			C[i] = min(C[i],C[i-coin[j]])+1;
		}
	}
	for(int i=0;i<=amount;i++)
		cout<<C[i]<<" ";
	return C[amount];	
}

int main(){
	int  coin[] = {1,5,7};
	cout<<"Minimum No of coin : "<<minimumcoinRequired(coin,sizeof(coin)/sizeof(int) , 4);
	return 0;
}
