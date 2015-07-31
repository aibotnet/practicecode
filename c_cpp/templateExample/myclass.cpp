#include <limits.h>
#include <stdlib.h> //also contains qsort
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

class A{
public:
	int a;
};

void f(A &bb){
	bb.a=12;
}
int main() {
    
    A aa;
    aa.a=10;
    f(aa);
    cout<<aa.a;

return 0;
}
