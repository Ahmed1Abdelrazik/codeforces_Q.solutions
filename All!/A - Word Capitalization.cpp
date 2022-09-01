#include <bits/stdc++.h>
using namespace std;
#include <cctype>
int main(){
 
#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w",stdout);
#endif
 
	string word;
    cin>>word;
    word[0] = toupper(word[0]);
	cout<<word;
	return 0;
}