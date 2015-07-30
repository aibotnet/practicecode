#include<stdio.h>

int row[] = {0, 0, -1, 0, 1};
int col[] = {0, -1, 0, 1, 0};

int getCount(char keypad[][3], int n){ // this is table filling approach
    if(keypad == NULL || n <= 0) return 0;
    if(n == 1) return 10;
    
    // taking n+1 for simplicity - count[i][j] will store
    // number count starting with digit i and length j
    int count[10][n+1];
    
    int i=0, j=0, k=0, move=0, ro=0, co=0, num = 0;
    int nextNum=0, totalCount = 0;
 
    for (i=0; i<=9; i++){count[i][0] = 0;count[i][1] = 1;}
 
    // Bottom up - Get number count of length 2, 3, 4, ... , n
    for (k=2; k<=n; k++){
        for (i=0; i<4; i++){  // Loop on keypad row
            for (j=0; j<3; j++){   // Loop on keypad column
                // Process for 0 to 9 digits
                if (keypad[i][j] != '*' && keypad[i][j] != '#'){
                    num = keypad[i][j] - '0';
                    count[num][k] = 0;
                    for (move=0; move<5; move++){
                        ro = i + row[move];
                        co = j + col[move];
                        if (ro >= 0 && ro <= 3 && co >=0 && co <= 2 &&
                           keypad[ro][co] != '*' && keypad[ro][co] != '#'){
                            nextNum = keypad[ro][co] - '0';
                            count[num][k] += count[nextNum][k-1];
                        }
                    }
                }
            }
        }
    }
 
    totalCount = 0;
    for (i=0; i<=9; i++)
        totalCount += count[i][n];
    return totalCount;
}


int main(int argc, char *argv[]){
   char keypad[4][3] = {{'1','2','3'},
                        {'4','5','6'},
                        {'7','8','9'},
                        {'*','0','#'}};
   printf("Count for numbers of length %d: %d\n", 1, getCount(keypad, 1));
   printf("Count for numbers of length %d: %d\n", 2, getCount(keypad, 2));
   printf("Count for numbers of length %d: %d\n", 3, getCount(keypad, 3));
   printf("Count for numbers of length %d: %d\n", 4, getCount(keypad, 4));
   printf("Count for numbers of length %d: %d\n", 5, getCount(keypad, 5)); 
   return 0;
}