#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;
long long mod = 1000000007;

int getSetDiff(int N,std::vector<int> v){
    sort(v.begin(),v.end());
    int gdiff=0,diff,p,c;
    p=pow(2,N-2); 
    for(int i=N-1;i>0;i--){
       c=p; 
       for(int j=0;j<i;j++){
         diff=v[i]-v[j];
         gdiff+=diff*c;
         gdiff%=mod;
         c/=2;
       }
       p/=2;
    }
    return gdiff;    
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int N,K;
    cin>>N;
    while(N){
        cin>>K;
        vector<int> intVec(K);
        for(int i=0; i<K; i++)    
            cin>>intVec.at(i);
    cout<<getSetDiff(K,intVec)<<endl;
    N--;
    }
    return 0;
}
