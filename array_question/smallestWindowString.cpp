#include<iostream>
#include<string.h>
#include<limits.h>
using namespace std;

void findSmallestWindowInString(char input[],char chars[], int N, int M){
	cout<<"Length of strings"<<endl;
	cout<<N<<" "<<M<<endl;
	int shouldFind[256]={0};int hasFound[256]={0};
	int minWindow = INT_MAX;
	
	for(int i=0;i<M;i++) //processing of "tist"
		shouldFind[chars[i]]++;
	
	int start=0,finish=N-1,j=0,count=0;
	for(int i=0;i<N;i++){
		//first find M charecter in input
		if(!shouldFind[input[i]])
			continue;
		hasFound[input[i]]++;
		if (shouldFind[input[i]] >= hasFound[input[i]])
			count++;
		//if count is equal to M
		if(count==M){
			//cout<<i<<endl;
			while(!shouldFind[input[j]] || (hasFound[input[j]] > shouldFind[input[j]])){
				if(hasFound[input[j]] > shouldFind[input[j]])
					hasFound[input[j]]--;
				j++;
				cout<<i<<endl;
			}
			//update minWindow		
			if(minWindow > (i-j+1)){
				minWindow=i-j+1;
				start=j;finish=i;
			}			
		} 
	}	
	cout<<start<<" "<<finish<<endl;
}



int main(){
	char *str1="this is a test string";
	char *str2="tist";
	findSmallestWindowInString(str1,str2, strlen(str1), strlen(str2));
}
