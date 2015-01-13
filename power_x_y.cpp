#include<iostream>
using namespace std;

double findPow(double x,double N){
	//cout<<x<<" "<<N<<endl;
	if (N==0.0){
		cout<<x<<" "<<N<<endl;
		return 1.0;
	}	
	double half = N/2.0;
	//cout<<half<<endl;
	double res = findPow(x,half);
	//cout<<res<<endl;
	if ((int)N%2==0)
		return res*res;
	else{
		//to work for negative number
		if (N > 0)
			return x*res*res;
		else
			return (res*res)/x;
	}
	//return res*res;
}

int main(){
	cout<<-3/2<<endl;
	cout<<(double)findPow(16.0/9.0,1.0/2.0)<<endl;
	return 0;
}
