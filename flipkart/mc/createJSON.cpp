#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>
#include <cctype>
#include <stdlib.h>

using namespace std;

struct trieNode{
	bool flag;
	vector<int> v;
	trieNode *arr[26];
};

trieNode * createNode(){
	trieNode * t = new trieNode;
	t->flag = true;
	for(int i=0;i<26;i++)
		t->arr[i]=NULL;
	return t;
}


class JsonBuilder{
	public:
		trieNode *root;
		char ch;
	
		JsonBuilder(){
			root = createNode();
		}

		bool isValid(string s){
			return true;
		}
		void insertNode(string s){
			trieNode *temp = root;
			for(int i=0;i<s.length();i++){
				if(isdigit(s[i])) continue;
				if(s[i]=='>') continue;
				ch = s[i];
				
				if(ch == '='){
					temp->flag=false;
					temp->v.push_back(s[i+1]);
					cout<<"=";
				}
				else{
					if(temp->arr[ch-90]==NULL){
					 	temp->arr[ch-90]= createNode();
					}
					temp  = temp->arr[ch-90];
				}
			}
		}
		void createGraph(string arr[], int n){
			for(int i=0; i<n;i++){
				if(isValid(arr[i]))
					insertNode(arr[i]);
			}
		}
		string toString(trieNode *root){
			string s="";
			char ch ;
			if(root){
				for(int i=0;i<26;i++){
					if(root->arr[i]){
						ch = i+90;
						if(root->flag == false){
							s = "\t"+s+ch+" : [";
							for(int i=0;i<root->v.size();i++){
								ch = root->v[i]+90;
								s+=ch;
							}
							s+="]\n";		
						}else{
							s = "\t"+s+ch+" : ";
							s+= toString(root->arr[i])+"\n";
						}
					}
				}
			}
			return "{\n"+s+"\n}";
		}
};


int main(){
	string arr[]={"a>b=5","a>c=6"};
	JsonBuilder jb;
	jb.createGraph(arr,2);
	cout<<jb.toString(jb.root);
}