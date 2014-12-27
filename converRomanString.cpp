#include<iostream>
#include<stdlib.h>
using namespace std;

char * convertRomanString(char *buf,int number){
	int i=0;
	if(number < 0)
		return NULL;	
	while(number>=1000){number-=1000;buf[i++]='M';}
	if(number>=900){number-=900;buf[i++]='C';buf[i++]='M';}
	if(number>=500){number-=500;buf[i++]='D';}
	if(number>=400){number-=400;buf[i++]='C';buf[i++]='D';}
	while(number>=100){number-=100;buf[i++]='C';}
	if(number>=90){number-=90;buf[i++]='X';buf[i++]='C';}
	if(number>=50){number-=50;buf[i++]='L';}
	if(number>=40){number-=40;buf[i++]='X';buf[i++]='L';}
	while(number>=10){number-=10;buf[i++]='X';}
	if(number>=9){number-=9;buf[i++]='I';buf[i++]='X';}
	if(number>=5){number-=5;buf[i++]='V';}
	if(number>=4){number-=4;buf[i++]='I';buf[i++]='V';}
	while(number){number-=1;buf[i++]='I';}
	
	buf[i]='\0';
}
int main(){
	char buf[20];
	convertRomanString(buf,1494);
	cout<<buf<<endl;
}
