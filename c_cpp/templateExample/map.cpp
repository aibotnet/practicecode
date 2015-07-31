#include <iostream>
#include <map>

int main (){
  std::map<char,int> mymap;

  mymap['b'] = 100;
  mymap['a'] = 200;
  mymap['c'] = 300;

  mymap['c'] = -300;
  char ch = 'a';
  mymap[ch] = -200;

  std::map<char,int>::iterator it;
  
  mymap.insert ( std::pair<char,int>('z',2000) );

  for (it=mymap.begin(); it!=mymap.end(); ++it)
    std::cout << it->first << " => " << it->second << '\n';
  

  mymap.erase ('c');

  it = mymap.find('a');
  if (it != mymap.end())
    mymap.erase (it);
  
  for (it=mymap.begin(); it!=mymap.end(); ++it)
    std::cout << it->first << " ===> " << it->second << '\n';

  return 0;
}