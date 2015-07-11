#include <iostream>
#include <iomanip>
#include <algorithm>
#include <iterator>

using namespace std;

void FindLongestSubset(int* s, int n, int* subs, int& slen){
    sort(s, s + n);
    copy(s, s + n, ostream_iterator<int>(cout, "  "));
    cout << endl;
    int* p(s);
    int* start(NULL);
    int l(0);   // length
    int maxLen(0);
    int *maxStart(NULL);
    int *pSubs(subs);

    while(p < s + n){
        if(start == NULL){
            start = p ++;l ++;
        }
        else{
            if(*p - *(p-1) == 1){
                l ++;
            }
            else{
                l = 0;start = NULL;
            }

            p ++;
            while(p < s + n && *p == *(p - 1)){
                p ++;
            }
        }

        if(l > maxLen){
            maxLen = l;
            maxStart = start;
        }
    }

    // Copy elements to the subset
    l = 0;
    while(l < maxLen){
        *pSubs ++ = *maxStart ++;
        while(maxStart < s + n && *maxStart == *(maxStart - 1)){
            maxStart ++;
        }
        l ++;
    }
    
    slen = maxLen;
}

int main(int argc, char* argv[]){
    int testCase[] = { 5, 1, 9, 3, 8, 20, 4, 10, 2, 11, 3, 12, 13, 14, 12, 12, 11};
    int len(sizeof(testCase)/sizeof(testCase[0]));
    cout << "Then test case is " << endl;
    copy(testCase, testCase + len, ostream_iterator<int>(cout, "  "));
    cout << endl;
    int *subs = new int[len];
    int sLen(0);
    FindLongestSubset(testCase, len, subs, sLen);
    cout << "The longest subset with consecutive numbers is" << endl;
    copy(subs, subs + sLen, ostream_iterator<int>(cout, "  "));
    cout << endl;
    delete[] subs;

    return 0;
}