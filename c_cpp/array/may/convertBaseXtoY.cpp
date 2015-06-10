/*
    author vikas kumar

*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <limits.h> 
using namespace std;

vector<int> reverse(vector<int> v){
    vector<int> temp;
    for(int i =v.size()-1;i>=0;i--)
        temp.push_back(v.at(i));
    return temp;
}    
vector<int> toDigits(long n , int base){
    vector<int> v;
    while(n>0){
        v.push_back(n%base);
        n=n/base;
    }
    return reverse(v);
}

long fromDigits(vector<int> v, int base){
    long n=0;
    for(int i=0;i<v.size(); i++){
        n = n*base+v.at(i);
    }
    return n;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    int *arr;
    vector<int> v;
    v.push_back(2);
    v.push_back(3);
    v.push_back(5);
    
    vector<int> out  =  toDigits(fromDigits(v,5),11);
    for (int i = 0; i < out.size(); ++i){
        cout<<out.at(i);
    }
return 0;
}
