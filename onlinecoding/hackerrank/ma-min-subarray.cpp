#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int getMax(int arr[], int n){
    int temp=0;
    for(int i=0;i<n;i++){
        if(arr[i]<0)
            continue;
        temp+=arr[i];
    }
    return temp;
}

int getMaxC(int arr[], int n){
    int max=0,temp=0;
    for(int i=0;i<n;i++){
        temp+=arr[i];
        if(temp <0) temp=0;
        if(temp>max) max=temp;
    }
    return max;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n,m;
    int *arr;
    cin>>n;
    while(n){
        cin>>m;
        arr = new int[m];
        for(int i=0;i<m;i++){
            cin>>arr[i];
        }
        cout<<getMaxC(arr,m)<<" "<<getMax(arr,m)<<endl;
        n-=1;
    }

}
