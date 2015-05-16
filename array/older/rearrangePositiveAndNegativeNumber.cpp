#include<limits.h>
#include<iostream>
using namespace std;


void rearrange(int a[], int n){
    int min = INT_MAX, max = INT_MIN;
    for(int i=0; i<n; i++){
        if(a[i] > max) max = a[i];
        if(a[i] < min) min = a[i];
    }
    //Change all values to Positive
    for(int i=0; i<n; i++)  a[i]-= min;
    int newMax = max-min+1, cuNegativeIndex = 0;
    //Save original negative values into new positions
    for(int i=0; i<n; i++)
        if(a[i]%newMax < (-min))
            a[cuNegativeIndex++] += (a[i]%newMax)*newMax;

    //Save original positive values into new positions
    int cuPositiveIndex = cuNegativeIndex;
    for(int i=0; i<n; i++)
        if(a[i]%newMax > (-min))
            a[cuPositiveIndex++] += (a[i]%newMax)*newMax;
    //Recover to original value 
    for(int i=0; i<n; i++) a[i] = a[i]/newMax + min; 
}

int main(){
    int  number[] = {5,4,-3,-9,-8,-7,-6,5,4,-1,4,6,7};
    rearrange(number,sizeof(number)/sizeof(int));

    for(int i=0;i<(sizeof(number)/sizeof(int));i++)
        cout<<number[i]<<" ";
    cout<<endl;
return 0;
}
