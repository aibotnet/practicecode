#include<stdio.h>
/*
void show_mem_rep(char *start, int n) {
    int i;
    for (i = 0; i < n; i++)
         printf(" %.2x", start[i]);
    printf("\n");
}
 
//Main function to call above function for 0x01234567
int main(){
   int i = 0x01234567;
   show_mem_rep((char *)&i, sizeof(i));
   return 0;
}
*/

//short function

int main() {
   unsigned int i = 1;
   char *c = (char*)&i;
   if (*c)    
       printf("Little endian");
   else
       printf("Big endian");
   return 0;
}
