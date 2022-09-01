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
 
  	
  	int t; cin>>t;
 
 
  	while(t--){
  		int n,m; cin>>n>>m;
  		int a[n],b[m];
  		bool f = false;
  		for(int i =0 ; i<n ; i++) cin>>a[i];
  		for(int j =0 ; j<m ; j++) cin>>b[j];
 
		for(int i =0 ; i<n ; i++){
			for(int j =0 ; j<m ; j++){
				if (a[i] == b[j] && f == false){
					f = true;
					cout<<"Yes\n";
					cout<<"1 "<<a[i]<<"\n";
					break;
				}
			}
			if(f == true) break;			
		}
		if(f == false){
			cout<<"No\n";
		}
 
  	}
 
 
  	return 0;
 
}