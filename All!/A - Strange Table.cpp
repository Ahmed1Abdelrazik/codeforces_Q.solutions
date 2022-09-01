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
 		ll n,m,x ; cin>>n>>m>>x;
 		ll Qu = x/n;
 		ll Rem = x%n;
 		if(Rem==0) Rem=n;
 		else Qu++;
 		// cout<<Rem<<" "<<Qu<<endl;
 		cout<<m*(Rem-1) + Qu<<"\n";
 		
 
 		
 
 
 	}
 		
}
 
 