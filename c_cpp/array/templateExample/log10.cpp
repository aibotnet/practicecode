#include <stdio.h>      /* printf */
#include <math.h>       /* log10 */

int f(double n){
	double d1;
	if(n==1) return true;

	for(int i=1;i<=n/2;i++){
			d1=log10(n)/log10(i);
		  if((d1-floor(d1))==0)
		  	  return true;
		}

	return false;	  	
}

int main ()
{
  double param, result;
  param = 1000.0;
  result = log10 (param);
  printf ("%d\n", f(8));

  return 0;
}