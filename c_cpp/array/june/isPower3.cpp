#include<iostream>
#include<math.h>

bool IsPowerOfThree(unsigned int n)
{
  // Optimizing lines to handle the most common cases extremely quickly
  if(n%3 != 0) return n==1;
  if(n%9 != 0) return n==3;

  // General algorithm - works for any uint
  unsigned int r;
  n = n/59049;r=n%59049; if(n!=0 && r!=0) return false;
  n = (n+r)/243;r=n%243; if(n!=0 && r!=0) return false;
  n = (n+r)/27;r=n%27;   if(n!=0 && r!=0) return false;
  n += r;
  return n==1 || n==3 || n==9;
}

int main(){

}

/*
* 59040 == 3^10
* 243   == 243
*/
