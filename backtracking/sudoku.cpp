#include <stdio.h>
#define UNASSIGNED 0 
#define N 9
 
 
/* Takes a partially filled-in grid and attempts to assign values to
  all unassigned locations in such a way to meet the requirements
  for Sudoku solution (non-duplication across rows, columns, and boxes) */


bool FindUnassignedLocation(int grid[N][N], int &row, int &col){
    for (row = 0; row < N; row++)
        for (col = 0; col < N; col++)
            if (grid[row][col] == UNASSIGNED)
                return true;
    return false;
}
 
bool UsedInRow(int grid[N][N], int row, int num){
    for (int col = 0; col < N; col++)
        if (grid[row][col] == num)
            return true;
    return false;
}
 
bool UsedInCol(int grid[N][N], int col, int num){
    for (int row = 0; row < N; row++)
        if (grid[row][col] == num)
            return true;
    return false;
}
 
/* Returns a boolean which indicates whether any assigned entry
   within the specified 3x3 box matches the given number. */
bool UsedInBox(int grid[N][N], int boxStartRow, int boxStartCol, int num){
    for (int row = 0; row < 3; row++)
        for (int col = 0; col < 3; col++)
            if (grid[row+boxStartRow][col+boxStartCol] == num)
                return true;
    return false;
}
 

bool isSafe(int grid[N][N], int row, int col, int num){
    /* Check if 'num' is not already placed in current row,
       current column and current 3x3 box */
    return !UsedInRow(grid, row, num) &&
           !UsedInCol(grid, col, num) &&
           !UsedInBox(grid, row - row%3 , col - col%3, num);
}
 
void printGrid(int grid[N][N]){
    for (int row = 0; row < N; row++){
       for (int col = 0; col < N; col++)
             printf("%2d", grid[row][col]);
        printf("\n");
    }
}

bool SolveSudoku(int grid[N][N]){
    int row, col;
 
    if (!FindUnassignedLocation(grid, row, col)) // If there is no unassigned location, we are done
       return true; // success!
 
    for (int num = 1; num <= 9; num++){
        if (isSafe(grid, row, col, num)){
            grid[row][col] = num; // make tentative assignment
 
            if (SolveSudoku(grid)) return true; // return, if success, yay!
 
            grid[row][col] = UNASSIGNED;  // failure, unmake & try again
        }
    }
    return false; // this triggers backtracking
}
 
/* Driver Program to test above functions */
int main(){
    // 0 means unassigned cells
    int grid[N][N] = {{3, 0, 6, 5, 0, 8, 4, 0, 0},
                      {5, 2, 0, 0, 0, 0, 0, 0, 0},
                      {0, 8, 7, 0, 0, 0, 0, 3, 1},
                      {0, 0, 3, 0, 1, 0, 0, 8, 0},
                      {9, 0, 0, 8, 6, 3, 0, 0, 5},
                      {0, 5, 0, 0, 9, 0, 6, 0, 0},
                      {1, 3, 0, 0, 0, 0, 2, 5, 0},
                      {0, 0, 0, 0, 0, 0, 0, 7, 4},
                      {0, 0, 5, 2, 0, 6, 3, 0, 0}};
    if (SolveSudoku(grid) == true)
          printGrid(grid);
    else
         printf("No solution exists");
 
    return 0;
}