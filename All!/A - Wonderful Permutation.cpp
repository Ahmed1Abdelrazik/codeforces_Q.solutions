/*Ahmed Abdelrazik*/
 
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pi;
#define append push_back
#define pair make_pair
#define search(vec,a) binary_search(vec.begin(), vec.end(), a)
 
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
 
  	int t ; cin>>t;
	  	while(t--){
	  		int n,k; cin>>n>>k;
	  		int c = k;
	  		int a[n];
	  		for(int i=0;i<n;i++)cin>>a[i];
 
  			for(int i=0; i<k ; i++){
  				if(a[i]<=k){c--;}
  			}
  			cout<<c<<"\n";
	  	}
  		
}
 
 
 