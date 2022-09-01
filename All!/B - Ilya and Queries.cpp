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
	//start here
 
 	string S;cin>>S;
 	int l = S.length();
	int A[l]={0};
 
	for(int i =0 ; i<l-1 ; i++){
		if(S[i]==S[i+1]) A[i+1]++;
 
	}
	for(int i=0 ; i<l-1 ; i++){
		A[i+1]+=A[i];
 
	}
 	int q; cin>>q;
 	while(q--){
 
 		int a,b; cin>>a>>b;
 		cout<<A[b-1]-A[a-1]<<"\n";
 
 	}
 
}