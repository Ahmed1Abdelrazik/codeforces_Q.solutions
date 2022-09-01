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
const int N = 1e5 + 2;
 
int main(){
 	
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif
 	ios::sync_with_stdio(false);
  	cin.tie(0);
	//code starts here
 
  	int n;cin>>n;
 
	ll C[N]={0};
 
  	for(int r =1 ; r<=n; r++){
  		int k;
  		cin>>k;
  		C[k]+=k;
 
  	}
 
  	ll dp[n+1];
 
  	dp[0]=0;
  	dp[1] = C[1];
 
  	for(int i = 2 ; i < N ; i++){
  		dp[i] = max(dp[i-1], dp[i-2] +  C[i] );
  	}
 
  	cout<<dp[N-1];
}