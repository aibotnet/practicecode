#include <queue> // functional,iostream,ctime,cstdlib
#include <iostream>
using namespace std;


int main(int argc, char* argv[])
{
    
    priority_queue<int,vector<int>,greater<int> > q;
    int t;
    for( int i = 0; i != 3; ++i ){
        cin>>t;
        q.push(t);
    }

    cout << "Min-heap, popped one by one: ";
    while( ! q.empty() ) {
        cout << q.top() << ' ';  // 0 3 3 3 4 5 5 6 8 9
        q.pop();
    }
    cout << endl;
    return 0;
}