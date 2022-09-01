#include <bits/stdc++.h>
using namespace std;
#include <cmath>
// #include <cctype>
 
int main(){
 
#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w",stdout);
#endif
 
	long long int t;cin>>t;
	
	while(t--){
		long long int n; cin>>n;
		long long int count=0;
		long long int a[n];
		for(int i=0; i <n;i++) cin>>a[i];
			if(a[0]!=0) count++;
		for(int j =1; j<n;j++){
			if((a[j]!=0 && a[j-1] ==0)){count ++;}
		}
 
		if(count>=2) cout<<2<<endl;
		else if(count==1) cout<<1<<endl;
		else cout<<0<<endl;
	}
 
 
}