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
 	  
 	int tt ; cin>>tt;
 	while(tt--){
 		int n; cin>>n;
 		ll a[n];
 		for(int i = 0 ; i< n ; ++i) cin>>a[i];
 
		vi L;
 
		ll maax =-2e9;
		int i = 0;
		while(i<n){
				if(i<n && a[i]>0){
					while( i<n && a[i]>0 ){
						if(a[i]>maax) maax = a[i];
						i++;
					}
 
						L.append(maax);
						maax=-2e9;
					}
				
				if(i<n && a[i]<0){
					while(i<n && a[i]<0  ){
						if(a[i]>maax) maax = a[i];
						i++;
					}
 
						L.append(maax);
						maax=-2e9;
					}
		}
 
			
		ll sum = 0;
		for(int i =0 ; i<L.size(); i++) sum+= L[i];
 
		cout<<sum<<"\n";
	}
 
}