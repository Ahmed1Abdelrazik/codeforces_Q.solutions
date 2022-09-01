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
 
  	// for(int i = 1 ; i < 10 ; i++){
  	// 	cout<<i<<" "<<i*(i+1) /2<<"\n";
  	// }
 
	int t; cin>>t;
 
	while(t--){
		ll n; cin>>n;
		string S; cin>>S;
 
		ll res = n*(n+1) / 2;
		for(int  i=  1 ; i< n ; i++){
			if(S[i]==S[i-1]) res-=i;
		}
 
		cout<<res<<"\n";
	}
}