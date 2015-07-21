// range heap example
#include <iostream>     // std::cout
#include <algorithm>    // std::make_heap, std::pop_heap, std::push_heap, std::sort_heap
#include <vector>       // std::vector

using namespace std;

bool mycompare(int a, int b){
   if(a<b) return true;
   else return false; 
}

int main () {
  
  /* Sorting a vector
  int myints[] = {10,20,30,5,15};
  vector<int> v(myints,myints+5);
  sort(v.begin(),v.end(),mycompare);
  for(int i=0;i<v.size();i++)
    cout<<v[i]<<" ";
  */

  // sorting an ordinary array 

  int myints1[] = {10,20,30,5,15};
  sort(myints1, myints1+5);
  for(int i=0;i<5;i++)
    cout<<myints1[i]<<" ";
  return 0;
}