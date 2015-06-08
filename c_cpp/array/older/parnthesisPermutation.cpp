#include<iostream>
using namespace std;

void printPermutation(int pos,int n,int open,int close){
	static char buf[20];
	if (close == n){
		buf[pos]='\0';
		cout << buf <<endl;
		return;
	}
	
	if(open > close){
		buf[pos]= ')';
		printPermutation(pos+1,n,open,close+1);	
	}
	
	if (open < n){
		buf[pos]= '(';
		printPermutation(pos+1,n,open+1,close);
	}
}

int main(){
	printPermutation(0,3,0,0);
}

