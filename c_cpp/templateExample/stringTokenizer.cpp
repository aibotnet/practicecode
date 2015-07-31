/* strtok example */
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <cstring>

using namespace std;

int main (){

  std::string data = "abc:def:ghi:jkl";
  StringTokenizer strtok(data,":");

  return 0;
}