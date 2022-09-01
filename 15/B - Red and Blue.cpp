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
 
 	int t; cin>>t;
 	while(t--){
 		int n; cin>>n;
 		int Q[n]={0};
 		for(int i =0 ; i<n ; i++){
 			cin>>Q[i];
 		}
 		int m ; cin>>m;
 		int M[m];
 		for(int i =0 ; i<m ; i++){
 			cin>>M[i];
 		}
 
 
 		int dp1[n]={0};
 		int dp2[m]={0};
 
 		dp1[0] = Q[0];
 		dp2[0] = M[0];
 
 		int mmax1 =max(0,dp1[0]);
 		int mmax2 =max(0,dp2[0]);
 
		for(int i =1 ; i<n ; i++){
 			dp1[i]= Q[i]+dp1[i-1];
 			if(dp1[i]>mmax1)mmax1=dp1[i];
 		}
 		for(int i =1 ; i<m ; i++){
 			dp2[i]= M[i]+dp2[i-1];
 			if(dp2[i]>mmax2)mmax2=dp2[i];
 		}
 		 		
 		cout<<mmax1+mmax2<<"\n";
 
 
 	}
 
 
}
 