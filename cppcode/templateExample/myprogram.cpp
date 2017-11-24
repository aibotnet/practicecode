#include <limits.h>
#include <stdlib.h> //also contains qsort
#include <math.h>       /* log10,log2 */
#include <string.h>
#include <iostream>
#include <fstream>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <string> 
#include <algorithm>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>

using namespace std;

int strtoi(string s){
	int num = 0;
	for(int i=0;i<s.size();i++){num=num*10+(s[i]-48);}
	return num;
}
string itostr(int i){
	string s="",ss="";
	while(i){s+=(i%10)+48;i/=10;}
	for(int i=s.size()-1;i>=0;i--) ss+=s[i];return ss;
}

int main() {
    
    int N,K;
    
return 0;
}
