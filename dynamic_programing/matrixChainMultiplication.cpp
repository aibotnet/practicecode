#include <iostream>
#include <stdlib.h>
#include <limits.h>
#include <algorithm>

using namespace std;

//dinamic programming approach
//cost of multiplication of matrix A[p,q] X B[q,r] ==> pqr
//mat[i][j] --> stores cost of multiplication of matrix (0,i) to (i+1, n)
void matrixChainMultiplication(int dimension[],int n){
	int mat[n+1][n+1];
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){

		}
	}
}

int main(){
	//dimension of matrix.
	int  dimension[] = {5,4,3,9,8,7,6,5};
	matrixChainMultiplication(dimension,sizeof(dimension)/sizeof(int));
return 0;
}
