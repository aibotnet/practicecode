#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int getMaxArea(int hist[], int n){
    stack<int> s;
    int max_area = 0; 
    int tp;
    int area_with_top;
 
    int i = 0;
    while (i < n){
        if (s.empty() || hist[s.top()] <= hist[i])
            s.push(i++);
        else{
            tp = s.top(); 
            s.pop(); 
            area_with_top = hist[tp] * (s.empty() ? i : i - s.top() - 1);
            if (max_area < area_with_top)
                max_area = area_with_top;
        }
    }

    while (s.empty() == false){
        tp = s.top();
        s.pop();
        area_with_top = hist[tp] * (s.empty() ? i : i - s.top() - 1);
 
        if (max_area < area_with_top)
            max_area = area_with_top;
    }
    
    return max_area;
}


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
    int n;
    int *arr;
    cin>>n;
    arr = new int[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }    
    cout<<largestRectangle(arr,n);
}
