#include<stdio.h>
#define N 4 
 
void printSolution(int sol[N][N]){
    for (int i = 0; i < N; i++){
        for (int j = 0; j < N; j++)
            printf(" %d ", sol[i][j]);
        printf("\n");
    }
}
bool isSafe(int maze[N][N], int x, int y){
    if(x >= 0 && x < N && y >= 0 && y < N && maze[x][y] == 1)
        return true;
    return false;
}
 
/* A recursive utility function to solve Maze problem */
bool solveMazeUtil(int maze[N][N], int x, int y, int sol[N][N]){
    if(x == N-1 && y == N-1){
        sol[x][y] = 1;return true;
    }

    if(isSafe(maze, x, y) == true){// Check if maze[x][y] is valid
        sol[x][y] = 1;// mark x,y as part of solution path
        if (solveMazeUtil(maze, x+1, y, sol) == true) //right move
            return true;
        if (solveMazeUtil(maze, x, y+1, sol) == true) //down move
            return true;
        sol[x][y] = 0; //backtracking
        return false;
    }   
    return false;
}

bool solveMaze(int maze[N][N]){
    int sol[N][N] = {0};
    if(solveMazeUtil(maze, 0, 0, sol) == false){
        printf("Solution doesn't exist");
        return false;
    }
    printSolution(sol);
    return true;
}
 
int main(){
    int maze[N][N]  =  { {1, 0, 0, 0},
                         {1, 1, 0, 1},
                         {0, 1, 0, 0},
                         {1, 1, 1, 1}
                    };
    solveMaze(maze);
    return 0;
}