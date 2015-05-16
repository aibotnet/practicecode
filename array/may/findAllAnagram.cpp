#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

void findAnagram(string s1, string s2){
    char h1[256]={0},h2[256]={0};
    for(int i=0;i<s2.length();i++) h1[s2[i]]+=1;
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    string s1,s2;
    cin>>s1>>s2;
    findAnagram(s1,s2);
return 0;
}
