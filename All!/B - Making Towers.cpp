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
		vi b[n+1];
	
		int a[n];
		for(int  i = 0 ; i<n ; i++){
			cin>>a[i];
			b[a[i]].append(i+1);
 
		}
 
		// for(int i =1 ; i< n+1 ; i++){
		// 	for(int j = 0 ; j< b[i].size() ; j++) {
		// 		cout<<b[i][j]<<" ";
		// 	}
		// 	cout<<"\n";
 
		// }
 
		int c[n+1]={0};
		for(int i = 0 ; i<n ; i++){
			c[a[i]]=1;
		}
 
 
		for(int i =1 ; i< n+1 ; i++){
			for(int j = 1 ; j< b[i].size() ; j++) {
				if( (b[i][j] - b[i][j-1]) % 2 == 1) {
					c[i]++;
 
				}
			}
 
		}
		for(int i = 1 ; i<n+1 ; i++) {
			cout<<c[i]<<" ";
		}
 
		cout<<"\n";
 
	}
}