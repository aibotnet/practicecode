#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;
vector<int> mxh;
priority_queue<int,vector<int>,greater<int> > mnh;
int size=0;
void insert_in_max(int el){
    mxh.push_back(el);
    push_heap(mxh.begin(),mxh.end());
}

int extract_from_max(){
    int temp = mxh.front();
    pop_heap (mxh.begin(),mxh.end());
    mxh.pop_back();return temp;
}
void insert_in_min(int el){mnh.push(el);}

int extract_from_min(){
    int temp = mnh.top();
    mnh.pop();return temp;
}

void getBalance(int num){
    int min,max;
    if(size%2==0){
        insert_in_max(num);size++;
        if(mnh.size()==0) return;
        if(mxh.front() > mnh.top()){
            insert_in_min(extract_from_max());
            insert_in_max(extract_from_min());
        }
    }else{
        insert_in_max(num);size++;
        insert_in_min(extract_from_max());
    }
} 
double getMedian(){
    if(size%2==0)
        return (mxh.front()+mnh.top())/2.0;  
    else
        return mxh.front(); 
}
int main() {
    int num;
    while(true){
        cin>>num;getBalance(num);
        cout<<"Median is now : "<<getMedian()<<endl;
    }
return 0;
}
