#include <iostream>
#define M 100001
#define S 100000
using namespace std;

bool p[M];
bool seg[S];

// 0 - non prime, 1 - prime
void generate(){
    for(long int i=3; i<M; i++) p[i] = i%2;
    p[0] = p[1] = 0; p[2] = 1;
    long int j=3;
    while(j*j <= M){
        for(long int t=j*j; t<=M; t+=j)
            p[t] = 0;
        j+=2;
    }
}

void print(int m, int n){
    while(m < M && m<=n){
        if(p[m]) cout << m << "\n";
        m++;
    }
    
    for(int i=0; i<S; i++) seg[i] = (i+m)%2;
    
    for(int np=3; np<M; np+=2){
        if(!p[np]) continue;
        int in=0;
        if(m%np) in = np - m%np;
        while(m+in <= n){
            seg[in] = 0;
            in+=np;
        }
    }
    
    for(int i=0; i<S && m+i<=n; i++){
        if(seg[i])
            cout << i+m << "\n";
    }
    
}

int main(){
    int t;cin >> t;
    generate();
    while(t--){
        long int m,n;
        cin >>m >> n;
        print(m,n);
        cout << "\n";
    }
}