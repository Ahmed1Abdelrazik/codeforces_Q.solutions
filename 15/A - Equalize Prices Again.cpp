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
 		int n; cin>>n;
 		int a[n];
 		ll sum = 0;
 		for(int i =0 ; i<n ; i++){
 			cin>>a[i];
 			sum+=a[i];
 		}
 		if(sum % n !=0) cout<<(sum/n) +1<<"\n";
 		else cout<<sum/n<<"\n";
 
 		
 
 
 	}
 		
}