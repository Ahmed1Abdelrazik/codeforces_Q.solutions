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
 
 
int main(){
 	
	#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
	#endif
 	ios::sync_with_stdio(false);
  	cin.tie(0);
	//code starts here
	int  n; cin>>n;
	
  	vi B;
  	for(int i =0 ; i<n; i++) {
  		int a; cin>>a;
  		B.append(a);
  	}
 	sort(B.begin(),B.end());
 	
 
 	int  m; cin>>m;
	vi G;
  	for(int i =0 ; i<m; i++) {
  		int a; cin>>a;
  		G.append(a);
  	}
 	sort(G.begin(),G.end());
 
 	int result = 0;
  	if(n<m){
  		for(int i = 0 ; i<n ; i++){
  			int j = 0;
  			while(j<G.size()){
  				if(abs(B[i]-G[j])<=1){
  					result++;
  					G.erase(G.begin()+j);
  					break;
  				}
  				j++;
  			}
  		}
 
  	}
 
  	else{
  		for(int i = 0 ; i<m ; i++){
  			int j = 0;
  			while(j<B.size()){
  				if(abs(G[i]-B[j])<=1){
  					result++;
  					B.erase(B.begin()+j);
  					break;
  				}
  				j++;
  			}
  		}
 
  	}
  	cout<<result;
 
}