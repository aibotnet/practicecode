#include <iostream>
#include <set>

using namespace std;

int main (){
  int myints[] = {75,23,65,42,13};
  set<int> myset (myints,myints+5);

  cout << "myset (int) contains:";
  myset.insert(23);
  set<int>::iterator it;
  for (it=myset.begin(); it!=myset.end(); ++it)
  	cout << ' ' << *it;
  cout << '\n';



  string sarr[] = {"a","hgg","vikas","hello","hi"};
  set<string> myset1 (sarr,sarr+5);
  
  myset1.insert("geeksforgeeks");

  cout << "myset (string) contains:";
  set<string>::iterator it1;
  for (it1=myset1.begin(); it1!=myset1.end(); ++it1)
  	cout << ' ' << *it1;
  cout << '\n';





  it1 = myset1.find("hello");
  cout<<"\nresult : "<<*it1<<endl;
  
  it1 = myset1.find("hello HI");
  if(it1!=myset1.end())
  	cout<<"\nresult : "<<*it1<<endl;
  else
  	cout<<"Not Found\n";

  myset1.erase("hgg");
  myset1.erase("f sdbhfou");
  for (it1=myset1.begin(); it1!=myset1.end(); ++it1)
  	cout << ' ' << *it1;
  cout << '\n';
  
  return 0;
}