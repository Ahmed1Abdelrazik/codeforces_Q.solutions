#include <bits/stdc++.h>
using namespace std;
#include <algorithm>
#include <string>
#include <chrono>
using namespace std::chrono;
// #include <cctype>
#define long long int;
int main(){
 
#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w",stdout);
#endif
 	 int n; cin>>n;
 	 int a[n+1];
 
 	 for(int i=0; i<=n; i++) a[i]=1;
	 a[0]=0; a[1]=0;
 
	 for(int i=2; i*i<=n; i++){
	 	if(a[i]==1){
	 		for(int j=2; i*j<=n; j++){
	 			a[i*j]=0;
	 		}
	 	}
	 }
 
	 if(a[n-2])cout<<2<<" "<<n-2;
	 else cout<<-1;
	 
 
 
 
}