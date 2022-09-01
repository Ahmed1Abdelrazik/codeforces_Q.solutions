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
	int t; cin>>t;
	while(t--){
		int n,m,x,y,d;
		cin>>n>>m>>x>>y>>d;
		if( y-d <=1 && x-d<=1 )cout<<-1<<"\n";
		else if( y+d>=m  && x+d>=n )cout<<-1<<"\n";
		else if( x+d >=n && x-d-1<=0 )cout<<-1<<"\n";
		else if( d+y>=m  && y-d-1<=0 )cout<<-1<<"\n";
 
		else cout<<n+m-2<<"\n";
	}
 
}