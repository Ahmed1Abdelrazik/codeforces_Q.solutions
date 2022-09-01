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
 
	 	string a;cin>>a;
	 	int zero = a.length();
	 	int one = 0;
	 	for(int r =0 ; r<a.length() ; r++){
	 		if(a[r]=='1') {one++; zero--;}
	 			
	 	}
 
	 	if(zero != one)
	 	cout<<min(zero,one)<<"\n";
	 	else
	 		cout<<one-1<<"\n";
 	}
 		
}