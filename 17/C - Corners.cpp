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
	
	int t = 0; cin>>t;
 
	while(t--){
		int n, m ; cin>>n>>m;
		int ones = 0;
		int zero = 0;
		string a[n];
 
 
		bool flag = false;
		for(int i = 0 ; i<n ; i++){
			string A; cin>>A;
			a[i]=A;
			for(int j = 0 ; j<m; j++){
				if(A[j]=='1')ones++;
				else zero++;
			}
			for(int j = 1 ; j<m; j++){
				if(A[j]=='0' && A[j-1] == '0'){flag =true; break;}
			}
		}
 
 
 
		for(int  j = 0  ; j<m ; j++){
			if(flag)break;
			for(int i =1 ; i<n; i++ ){
				if( a[i-1][j] == '0' && a[i][j] =='0' ) {flag = true; break;}
 
				if(a[i+1][j-1] == '0' && a[i][j] =='0') {flag = true; break;}
				if(a[i-1][j+1] == '0' && a[i][j] =='0') {flag = true; break;}
				if(a[i+1][j+1] == '0' && a[i][j] =='0') {flag = true; break;}
				if(a[i-1][j-1] == '0' && a[i][j] =='0') {flag = true; break;}
				
 
 
 
 
			}
 
		}
		// cout<<flag<<endl;
 
		if(flag)cout<<ones<<"\n";
		else {
			if(zero>0)cout<<ones-1<<"\n";
			else cout<<ones-2<<"\n";
		}
 
	}
}