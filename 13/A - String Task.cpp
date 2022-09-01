#include <bits/stdc++.h>
using namespace std;
#include <cctype>
int main(){
 
#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w",stdout);
#endif
 
	string word,out;
    cin>>word;
 
    for(int r=0; r<word.length(); r++)
    	{
    		char letter=tolower(word[r]);
    		if(letter=='o'||letter=='u'||letter=='a'||letter=='i'||letter=='y'||letter=='e') continue;
    		else out= out +'.'+letter;
    	}
    	cout<<out;
	return 0;
}