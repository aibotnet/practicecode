#include<iostream>
#include<stdlib.h>
using namespace std;

int convertRomanStringToInteger(char *buf , int n){
	int i=0, number= 0;
	if(n==0)
		return 0;
	while(i < n && buf[i]=='M'){number+=1000;i++;}
	if(i+1 < n && (buf[i]=='C' && buf[i+1]=='M')){number+=900;i+=2;}
	if(i < n && buf[i]=='D'){number+=500;i++;}
	if(i+1 < n && (buf[i]=='C' && buf[i+1]=='D')){number+=400;i+=2;}
	
	while(i < n && buf[i]=='C'){number+=100;i++;}
	if(i+1 < n && (buf[i]=='X' && buf[i+1]=='C')){number+=90;i+=2;}
	if(i < n && buf[i]=='L'){number+=50;i++;}
	if(i+1 < n && (buf[i]=='X' && buf[i+1]=='L')){number+=40;i+=2;}
	
	while(i < n && buf[i]=='X'){number+=10;i++;}
	if(i+1 < n && (buf[i]=='I' && buf[i+1]=='X')){number+=9;i+=2;}
	if(i < n && buf[i]=='V'){number+=5;i++;}
	if(i+1 < n && (buf[i]=='I' && buf[i+1]=='V')){number+=4;i+=2;}
	while(i < n && buf[i]=='I'){number+=1;i++;}
	
	return number;
}


int main(){
	char *buf="MCCCLXXXVI";
	cout << convertRomanStringToInteger(buf,10);
}
