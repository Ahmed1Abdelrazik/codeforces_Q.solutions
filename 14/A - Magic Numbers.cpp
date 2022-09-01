 
#include <bits/stdc++.h>
using namespace std;
#include <cmath>
// #include <cctype>
int main(){
 
#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w",stdout);
#endif
 
	string n;
	cin>>n;
	bool f = true;
	for(int i =0; i <n.length(); i++){
		if(n[i]!='1'&&n[i]!='4'){
			cout<<"NO"; f =false; break;}
		else if(n[0]=='4'){cout<<"NO"; f=false; break;}
		else if(n[i]=='4'&&n[i+1] =='4'&&n[i+2] =='4'){cout<<"NO"; f=false;break;}
		
		}
	if (f == true ){cout<<"YES";}
	return 0;
}