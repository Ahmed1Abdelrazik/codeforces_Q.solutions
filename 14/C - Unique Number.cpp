 
#include <bits/stdc++.h>
using namespace std;
#include <algorithm>
#include <string>
// #include <cctype>
#define long long int;
int main(){
 
#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w",stdout);
#endif
 
	 int t;cin>>t;
	
	while(t--){
		 int n; cin>>n;
		 int d =9;
		 string out = "";
		 bool flag =true;
		 if(n>45)cout<<-1<<endl;
 
		 else{
			 while(n>0){
			 	if(n<d) break;
			 	out += to_string(d);
			 	n-=d;
			 	d--;
 
			 }
			 if(n>0) out+=to_string(n);
		 reverse(out.begin(), out.end());
		 cout<<out<<endl;
		 }
 
 	}
 
 
}