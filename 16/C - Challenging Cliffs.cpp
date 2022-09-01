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
	int t; cin>>t;
 
	while(t--){
		int n; cin>>n;
		int a[n];
		for(int i= 0 ; i<n ; ++i){
			cin>>a[i];
		}
		sort(a,a+n);
		bool flag = false;
		int i = 0;
		int min = abs(a[0]-a[1]);
		for(int r = 1 ; r<n; r++){
			if(abs(a[r]-a[r-1]) < min){
				i=r-1;
				min = abs(a[r]-a[r-1]);
			}
		}
		
		cout<<a[i]<<" ";
		for(int k =i+2 ; k<n; k++){
			cout<<a[k]<<" ";
		}
		for(int k =0 ; k<i; k++){
			cout<<a[k]<<" ";
		}
		cout<<a[i+1]<<"\n";	
 
 
 
	}
}