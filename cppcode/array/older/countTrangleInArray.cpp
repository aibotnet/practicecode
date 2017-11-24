// Program to count number of triangles that can be formed from given array
#include <stdio.h>
#include <stdlib.h>
 

int comp(const void* a, const void* b)
{  return *(int*)a > *(int*)b ; }
 
// Function to count all possible triangles with arr[] elements

int findNumberOfTriangles(int arr[], int n){
    qsort(arr, n, sizeof( arr[0] ), comp);
    int count = 0;
 
    // Fix the first element.  We need to run till n-3 as the other two elements are
    // selected from arr[i+1...n-1]
    for (int i = 0; i < n-2; ++i){
        // Initialize index of the rightmost third element
        int k = i+2;
 
        for (int j = i+1; j < n; ++j){
            while (k < n && arr[i] + arr[j] > arr[k])
               ++k;
            count += k - j - 1;
        }
    }
    return count;
}
 
// Driver program to test above functionarr[j+1]
int main(){
    int arr[] =   {10, 21, 22, 100, 101, 200, 300};
    int size = sizeof( arr ) / sizeof( arr[0] );
 
    printf("Total number of triangles possible is %d ",
           findNumberOfTriangles( arr, size ) );
 
    return 0;
}