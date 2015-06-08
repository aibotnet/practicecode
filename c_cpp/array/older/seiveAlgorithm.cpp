#include<iostream>
#include<stdlib.h>
using namespace std;

void markMultiples(int temp[],int start,int n){
	for(int i=start+start;i<=n;i+=start){
		temp[i]=1;//marking index so it wont be prime number.
	}
}

//seive algorithm Implementation
void generatePrime1toN(int n){
	int *temp =  new int[n+1];
	for (int i=0;i<=n;i++){temp[i]=0;}
	for(int i=2;i<=n;i++){
		if(temp[i]==0){
			cout<<"Prime No Is : "<<i<<endl;
			markMultiples(temp,i,n);
		}
	}
}

int main(){
	generatePrime1toN(100);
}
