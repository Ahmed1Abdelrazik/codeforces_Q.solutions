 
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
 
	 int n;cin>>n;
	 bool f = false;
	 for(int i =1; i<=n ; i++){
	 	bool check = true;
	 	for(int j =0; j<to_string(i).length();j++){
	 			if(to_string(i)[j]!='4' && to_string(i)[j]!='7'){
	 				check=false;
	 				break;
	 			}
 		}
	 	if(check && n%i ==0){
	 		f = true;
	 		// cout<<i<<" ";
	 	}
	 }
	 if(f == true){cout<<"YES";}
	 else{cout<<"NO";}
 
}