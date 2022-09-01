/*Ahmed Abdelrazik*/
 
/*	vector<int>::iterator itr = find(v.begin(), v.end(), key);
	int index = distance(v.begin(), itr);
*/
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
  		bool flag = true;
  		int n; cin>>n;
  		int a[n+1],pref[n+1],suff[n+1];
  		
  		for(int i = 1 ; i <= n; i++){
  			cin>>a[i];
  		}
  		pref[1] = a[1];
  		suff[n] = a[n];
  		for(int i = 2 ; i <= n; i++){
  			pref[i]= max(a[i],pref[i-1]);
  			
  		}
 		for(int i = n-1 ; i >= 1; i--){
  			suff[i]= max(a[i],suff[i+1]);
  		}
 
  		for(int i = 2 ; i <= n-1; i++){
  			if(a[i]< pref[i-1] && a[i]< suff[i+1]){
  				flag = false;
  			}
  		}
 
  		cout<<(flag? "Yes\n": "No\n");
 
  	}
}
 
 
 