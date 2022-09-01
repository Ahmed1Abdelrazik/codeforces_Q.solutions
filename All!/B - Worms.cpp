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
const int N = 1e5 + 9;
 
int main(){
 	
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif
 	ios::sync_with_stdio(false);
  	cin.tie(0);
	//code starts here
	int n; cin>>n;
	int a[n];
	for(int i =0; i<n ; i++) cin>>a[i];
	int m; cin>>m;
	int b[m];
	for(int i =0; i<m ; i++) cin>>b[i];
 
 
	ll sum[n+1];
	sum[0]=0;
	sum[1] = a[0];
 
	for(int i =2; i<=n ; i++) sum[i]=sum[i-1]+a[i-1] ;
	
		// for(int i =0; i<=n ; i++) cout<<sum[i]<<" ";
		// 	cout<<"\n";
 
	for(int i =0 ; i<m ; i++){
		auto k = lower_bound(sum,sum+n+1,b[i])-sum;
		cout<<k<<"\n";
	}
 
}