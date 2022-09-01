 #include <bits/stdc++.h>
using namespace std;
 
int main(){
 
#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt", "w",stdout);
#endif
 
	int n,m,k;
    cin>>n>>m>>k;
    int a[n];
 
    int res = 0;
    for(int i = 0 ; i<n;i++){
     cin>>a[i];
     if(a[i]==1){
     	m-=1;
     }
     else{
     	if(k>0) k-=1;
 		else m-=1;
     }
 
}
	if(m<0 && k<0)
	cout<<abs(m+k);
 	else if(m<0)
 		cout<<abs(m);
 	else cout<<0;
	return 0;
}
