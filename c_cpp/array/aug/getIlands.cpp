#include<iostream>
#include<math.h>

#define R 6
#define C 7

using namespace std;

int row[]={-1,-1,-1,0,0,1,1,1};
int col[]={-1,0,1,-1,1,-1,0,1};

void mark(int m[][7],int v[][7],int r,int c){
  int rowi,coli;v[r][c]=1;
  for(int i=0;i<8;i++)
    for(int j=0;j<8;j++){
      rowi = r + row[i];
      coli = c + col[j];
      if(rowi < 0 || rowi>=R || coli<0 || coli>=C) continue;
      if(v[rowi][coli] || ! m[rowi][coli]) continue;
      mark(m,v,rowi,coli);
    }
}

int getIlands(int m[][C]){
  int count = 0;
  int v[R][C];
  for(int i=0;i<R;i++)
    for(int j=0;j<C;j++)
      v[i][j]=0;
  for(int i=0;i<R;i++){
    for(int j=0;j<C;j++){
      if(!m[i][j] || v[i][j]) continue;
      cout<<i<<" "<<j<<"\n";
      count++;mark(m,v,i,j);
    }
  }
  return count;
}

int main(){
  int m[6][7]={
    {1,0,0,1,0,0,1},
    {1,1,0,1,0,1,0},
    {0,0,1,0,0,0,0},
    {0,0,0,0,0,0,0},
    {0,1,0,1,0,1,0},
    {1,0,1,0,1,0,1}
  };
  cout<<getIlands(m);
}
