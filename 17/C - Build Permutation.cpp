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
const int N = 317+ 1;
const int M = 1e5 +9;
ll square[N];
 
int main(){
 	
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif
 	ios::sync_with_stdio(false);
  	cin.tie(0);
	//code starts here
 
  	for(int i = 1 ; i<318 ; i++){
  		square[i]=i*i;
  	}
 
 
	// for(auto x:square) cout<<x<<" ";
	int t; cin>>t;
 
	while(t--){
		int dp[M]={0};
		bool f = true;
		vi out;
 
		int n; cin>>n;
		int a = 1;
		auto M = lower_bound(square,square+N,n-a)-square;
		for(int i = n-1 ; i>= 0 ; i--){
			if(f== false)break;
			while(dp[square[M]-i] == 1 || (square[M]-i) >=n ){
				a++;
				M = lower_bound(square,square+N,n-a)-square;
				if( (square[M]-i)<0){break; f = false;}
 
			}
		
			dp[square[M]-i] =1;
			out.append(square[M]-i);
 
		
		}
 
		if(f==true){
			for(int j = out.size()-1 ; j>=0  ; j-- ) {cout<<out[j]<<" ";}
			cout<<"\n";
		}
		else cout<<"-1\n";
 
	}
}