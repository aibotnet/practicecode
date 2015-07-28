#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

# define MAX 100 // assuming we need first 100 rows
long long triangle[MAX + 1][MAX + 1];


int foo(int n,int r){//can cause integer overflow
     if(n==r) return 1;
     if(r==1) return n;
     return foo(n-1,r) + foo(n-1,r-1);
}

long long C(int n, int r) {   //can cause integer overflow
    if(r > n / 2) r = n - r; // because C(n, r) == C(n, n - r)
    long long ans = 1;
    int i;

    for(i = 1; i <= r; i++) {
        ans *= n - r + i;
        ans /= i;
    }
    return ans;
}



void makeTriangle() {
    int i, j;

    // initialize the first row
    triangle[0][0] = 1; // C(0, 0) = 1

    for(i = 1; i < MAX; i++) {
        triangle[i][0] = 1; // C(i, 0) = 1
        for(j = 1; j <= i; j++) {
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
        }
    }
}

long long C1(int n, int r) {
	makeTriangle();
    return triangle[n][r];
}

int main() {
	cout<<foo(10,3)<<endl;
	cout<<C(10,3)<<endl;
	cout<<C1(10,3)<<endl;
return 0;
}
