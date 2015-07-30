// range heap example
#include <iostream>     // std::cout
#include <algorithm>    // std::make_heap, std::pop_heap, std::push_heap, std::sort_heap
#include <vector>       // std::vector

using namespace std;

struct s{
  int a;
  int b;
};
bool mycompare(s aa, s bb){
   if(aa.a > bb.a) return true;
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

  s *arr = new s[5];
  arr[0].a=-1;
  arr[0].b=9;
  arr[1].a=-1;
  arr[1].b=9;
  arr[2].a=-1;
  arr[2].b=9;
  arr[3].a=-1;
  arr[3].b=9;
  arr[4].a=-5;
  arr[4].b=9;

  sort(arr,arr+5,mycompare);

  for(int i=0;i<5;i++)
    cout<<arr[i].a<<" ";
  return 0;
}