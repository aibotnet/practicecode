#include<iostream>
#include<stdlib.h>
#include<string.h>
#include<stack>
using namespace std;

bool isOperend(char ch){
	if(ch=='&' || ch=='|' || ch=='!' || ch=='(' || ch == ')')
		return false;
	return true;
}

bool VerifierString(char propstat[], int n){
	cout<<propstat<<endl;
	stack<int> val;//value stack
	stack<char> op;//operator stack
	int v1,v2;
	//assuming given propositional  statement is syntactically correct.
	int i=0;
	while(i<n){
		if(isOperend(propstat[i])){val.push(int(propstat[i]));i++;}
		else{
			if(propstat[i]==')'){
				while(op.top()!='('){
					char opr = op.top();op.pop();
					if(op.empty() || op.top()!='!'){
						if(opr=='&'){
							v1=val.top()-48;val.pop();
							v2=val.top()-48;val.pop();
							val.push(v1&&v2);
						}
						else if (opr=='|'){
							v2=val.top()-48;val.pop();
							v1=val.top()-48;val.pop();
							val.push(v1||v2);
						}
						else{
							v1=val.top()-48;val.pop();
							val.push(!v1);
						}
					}
					else{ //handle case (!a&b)
						if(opr=='&'){
							v1=val.top()-48;val.pop();
							v2=val.top()-48;val.pop();
							val.push(v1&&!v2);
						}
						else{
							v2=val.top()-48;val.pop();
							v1=val.top()-48;val.pop();
							val.push(v1||!v2);
						}
						op.pop();
					}
				}
				//ignoring opening parenthesis
				op.pop();
				i++;
			}
			else{
				op.push(propstat[i]);i++;
			}
		}
	}

	while(!op.empty()){
		char opr = op.top();op.pop();
		if(op.empty() || op.top()!='!'){
			if(opr=='&'){
				v1=val.top()-48;val.pop();
				v2=val.top()-48;val.pop();
				val.push(v1&&v2);
			}
			else if (opr=='|'){
				v2=val.top()-48;val.pop();
				v1=val.top()-48;val.pop();
				val.push(v1||v2);
			}
			else{
				v1=val.top()-48;val.pop();
				val.push(!v1);
			}
		}
		else{ //handle case (!a&b)
			if(opr=='&'){
				v1=val.top()-48;val.pop();
				v2=val.top()-48;val.pop();
				val.push(v1&&!v2);
			}
			else{
				v2=val.top()-48;val.pop();
				v1=val.top()-48;val.pop();
				val.push(v1||!v2);
			}
			op.pop();
		}
	}
	cout<<val.top()<<endl;
	return val.top();
}
//Generate all possible expression of given length
bool tautologyVerifier(char propstat[],int start, int n){
	if(start==n){
		//now we reasc at the end of string now calculate
		//result of string and verify it.
		return VerifierString(propstat,n);
	}
	if(isOperend(propstat[start])){
		propstat[start]='0';
		bool res = tautologyVerifier(propstat,start+1,n);
		propstat[start]='1';
		return res && tautologyVerifier(propstat,start+1,n);
	}
	return 	tautologyVerifier(propstat,start+1,n);
}

//(a&(!b|b))|(!a&(!b|b))
int main(){
	//read integer untill [space] or [newline].
	char propstat[50];
	cout<<"Enter tautology String : \n";
	cin>>propstat;
	cout<<"Processing given string ....\n";
	if(tautologyVerifier(propstat,0, strlen(propstat)))
		cout<<"Tautology\n";
	else
		cout<<"Sorry not a Tautology\n";
}