#include <queue> // functional,iostream,ctime,cstdlib
using namespace std;


int main(int argc, char* argv[])
{
    srand(time(0));
    priority_queue<int,vector<int>,greater<int> > q;
    for( int i = 0; i != 10; ++i ) q.push(rand()%10);
    cout << "Min-heap, popped one by one: ";
    while( ! q.empty() ) {
        cout << q.top() << ' ';  // 0 3 3 3 4 5 5 6 8 9
        q.pop();
    }
    cout << endl;
    return 0;
}