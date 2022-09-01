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
		string a[n];
		set<string> col;
		for(int i = 0 ; i< n ; i++) {
			cin>>a[i];
			col.insert(a[i]);
		}
 
 
		
		bool b[n]={0};
		for(int i = 0 ; i< n ; i++){
			for(int j = 0 ; j<a[i].length()-1; j++){
				string L = a[i].substr(0,j+1);
				int B = a[i].length() - j;
 
				string M = a[i].substr(j+1,B);
				// cout<<L<<" "<<M<<"\n";
				if(col.count(L) && col.count(M)) b[i]=1;
 
 
			}
			// cout<<"---\n";
 
		}
 
 
		for(int r =0; r<n; r++) cout<<b[r];
		cout<<"\n";
 
	}
}