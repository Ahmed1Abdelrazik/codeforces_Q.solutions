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
 	ll p,y ; cin>>p>>y;
 	bool ok = false;
 	for(int i = y ; i>p ; --i){
 		ok=true;
 		for(int j = 2 ; j*j<=y ; j++){
 			if(j>p) break;
 			if(i%j == 0){
 				ok=false;
 				break;
 			}
 
		}
		if(ok){
		cout<<i;
		break;
 		}
 	}
 
 if(ok == false) cout<<-1;
 
}