/*
 Given a String and a pattern find all anagrams of the pattern in the original
 string. You need to print all the index of the location where 
 the match was found

 Ex – INPUT – ABDACDBACA   ABCD
 	  OUTPUT – 1 3 4 5 (at index 1 BDAC , at index 3 ACDB and so on )
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <limits.h> 
using namespace std;

bool check(int *h1,int *h2){
    for(int i=0;i<256;i++)
        if(h1[i]!=h2[i]){
            //cout<<i<<" "<<h1[i]<<" "<<h2[i]<<endl;
            return false;

        }
    return true;        
}


void findAnagram(string s1, string s2){
    int h1[256]={0},h2[256]={0};
    for(int i=0;i<s2.length();i++) h1[s2[i]]+=1;
    for(int i=0;i<s2.length();i++) h2[s1[i]]+=1;
    
    if(check(h1,h2)) cout<<0;

    for(int i=s2.length();i<s1.length();i++){
        h2[s1[i-s2.length()]]-=1;
        h2[s1[i]]+=1;
        if(check(h1,h2)) cout<<i-s2.length()+1;
    } 
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    string s1,s2;
    cin>>s1>>s2;
    findAnagram(s1,s2);
return 0;
}
