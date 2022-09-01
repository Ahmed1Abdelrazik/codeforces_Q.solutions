 
#include <bits/stdc++.h>
#include <algorithm>
using namespace std;
 
int main(){
 
#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w",stdout);
#endif
	int n,q; cin>>n>>q;
 
	int a[n];
	for(int i=0;i<n;i++) cin>>a[i];
	sort(a,a+n);
	reverse(a,a+n);
	long long int sum[n+1];
	sum[0]=a[0];
	for(int j =1 ; j<n;j++) sum[j]=sum[j-1]+a[j];
 	while(q--){
 		int x,y; cin>>x>>y;
	 		if(x!=y) cout<<sum[x-1]-sum[x-y-1]<<endl;
	 		else cout<<sum[x-1]<<endl;
 	}
 
 
 
 
 
}