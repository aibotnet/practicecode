#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;
long long mod = 1000000007;

long long getmod(long long temp){
	if(temp>0) temp %= mod;
   	else temp=temp+mod;	
    return temp;	
}

void getSeeds(int N,int K,int s[],int c[]){
    long long *dp= new long long[K+1];
    long long temp;

    //cout<<mod<<" \n";
    for(int i=0;i<N;i++) dp[i]=s[i]; 
    
    for(int i=N;i<=K;i++){
    	temp=0;
    	for(int j=1;j<N;j++){
    		temp+=dp[i-N+j]*c[j-1];
    		cout<<temp<<endl;
    	}
    	dp[i]=getmod(dp[i-N]-temp);
    	dp[i]=dp[i]/c[N-1];
    	dp[i]=getmod(dp[i]);
    	//dp[i]=dp[i]%mod;    
    }
    for(int i=N-1;i>=0;i--) cout<<dp[K-i]<<" ";
    //for(int i=0;i<=K;i++) cout<<dp[i]<<" ";	
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int N,K;
    cin>>N;cin>>K;
    int *seeds= new int[N];
    int *coefs= new int[N];
    for(int i=0;i<N;i++) cin>>seeds[i];
    for(int i=0;i<N;i++) cin>>coefs[i];
    getSeeds(N,K,seeds,coefs);
    return 0;
}
