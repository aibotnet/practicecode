#include<iostream>
#include<stdlib.h>
#include<stack>
#include<stdbool.h>
using namespace std;

int isOpening(char ch){
	if (ch == '(' || ch == '{' || ch == '[')
		return 1;
	return 0;
}

int isClosing(char ch){
	if (ch == ')' || ch == '}' || ch == ']')
		return 1;
	return 0;
}

int isMatching(char ch1 , char ch2){
	if (ch1=='(' && ch2 == ')')
		return 1;
	if (ch1=='{' && ch2 == '}')
		return 1;
	if (ch1=='[' && ch2 == ']')
		return 1;
	return 0;
}

int checkForParenthesis(char *arr, int n){
	int i;
	stack<char> s;
	for(i=0;i<n;i++){
		if (isOpening(arr[i]))
			s.push(arr[i]);
		else if (isClosing(arr[i])){
			char top = s.top();
			s.pop();
			if (!isMatching(top,arr[i]))
				return 0;		
		}
	}
	if (!s.empty())
		return 0;
	return 1;
}
int main(){	
	char *s = "{()()[][]}";
	cout << checkForParenthesis(s,10);	
	return 0;
}
