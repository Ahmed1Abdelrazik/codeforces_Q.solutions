/*Ahmed Abdelrazik*/
 
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
#define append push_back
#define pair make_pair
#define search(vec,a) binary_search(vec.begin(), vec.end(), a)
const ll INF = 0x3f3f3f3f3f3f3f3f;
// #define for(i,n) for(int i = 0; i<n ; i++) 
// #define For(i,a,n) for(int i = a; i<n ; i++) 
 
bool is_prime(int n){
	for(int e =2 ; e*e<=n ; e++){
 		if(n%e == 0) return false;
 	}
	return true;
 
}
 
const int M = 1e5 +9;
 
 
int main(){
 	
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif
 	ios::sync_with_stdio(false);
  	cin.tie(0);
	//code starts here
 
	int t; cin>>t;
 
	while(t--){
		int n; cin>>n;
		int a[n];
		int b[n+1]={0};
		for(int i = 0 ; i<n ; i++){
			cin>>a[i];
			b[a[i]]++;
		}
 
		for(int i = n-1  ; i>=1 ; i--){
			if(a[i-1] > a[i] ) a[i-1]=0;
		}
 
		int c[n+1] = {0};
		for(int i = 0  ; i<n ; i++){
			if(a[i]!=0)c[a[i]]++;
		}
 
		for(int i = n-1  ; i>=0 ; i--){
			if(c[a[i]]<b[a[i]]) a[i]=0;
		}
 
 
 
		for(int i = n-1  ; i>=1 ; i--){
			if(a[i-1] > a[i] ) a[i-1]=0;
		}
		int d[n+1] = {0};
		for(int i = 0  ; i<n ; i++){
			if(a[i]!=0)d[a[i]]++;
		}
 
 
		// for(int i = 0; i<n+1; i++)cout<<b[i]<<" ";
		// 	cout<<"\n";
		// for(int i = 0; i<n+1; i++)cout<<d[i]<<" ";
 
		// 	cout<<"\n";
 
 
		int sum =0;
 
 
		for(int i = 0  ; i<n+1 ; i++){
			if(d[i]==0 && b[i]>0 ) sum++;
		}
 
		cout<<sum<<"\n";
	}
}
