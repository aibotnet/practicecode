#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    long double a,b,n,temp;
    int i=3;
    cin>>a>>b>>n;
    while(i<=n){
        temp=b*b+a;
        a=b;b=temp;
        i+=1;
    }
    cout<<fixed<<b;
    return 0;
}
