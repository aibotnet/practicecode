#include<iostream>
using namespace std;

void findQutientAndReminder(int nu,int de){
	int quot =0,temp =1;
	
	while(de<=nu){
		de<<=1;temp<<=1;
	}
	
	while(temp >1){
		de>>=1;temp>>=1;
		if(nu >= de){
			nu-=de;quot+=temp;
		}
	}
	cout<<quot<<" "<<nu;
}

int main(){
	findQutientAndReminder(24,3);
	
	return 0;
}
