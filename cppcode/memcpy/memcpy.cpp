#include<stdio.h>
#include<string.h>
 
// A function to copy block of 'n' bytes from source
// address 'src' to destination address 'dest'.
void myMemCpy(void *dest, void *src, size_t n){
   // Typecast src and dest addresses to (char *)
   char *csrc = (char *)src;
   char *cdest = (char *)dest;
 
   // Create a temporary array to hold data of src
   char *temp = new char[n];
 
   // Copy data from csrc[] to temp[]
   for (int i=0; i<n; i++)
       temp[i] = csrc[i];
 
   // Copy data from temp[] to cdest[]
   for (int i=0; i<n; i++)
       cdest[i] = temp[i];
}
 
// Driver program
int main(){
   char csrc[] = "GeeksforGeeks";
   char cdest[100];
   myMemCpy(cdest, csrc, strlen(csrc)+1);
   printf("Copied string is %s", cdest);
 
   int isrc[] = {10, 20, 30, 40, 50};
   int n = sizeof(isrc)/sizeof(isrc[0]);
   int idest[n], i;
   myMemCpy(idest, isrc,  sizeof(isrc));
   printf("\nCopied array is ");
   for (i=0; i<n; i++)
     printf("%d ", idest[i]);
   return 0;
}
