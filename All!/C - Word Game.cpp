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
 
const int M = 1e5 +9;
 
 
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
		string A[3][n];
		string B[3][n];
 
		for(int j =0 ; j<3; j++){
			for(int i = 0 ; i< n; i++){
				cin>>A[j][i];
				B[j][i]=A[j][i];
			}
		}
 
		int a=0;
		int b=0; 
		int c=0;
 
		map<string,int> L;
 
 
		for(int i = 0 ; i<3; i++){
			for(int j = 0 ; j<n ; j++){
				L[A[i][j]]++;
				
			}
 
		}
		// cout<<L["abc"];
 
		for(int i = 0 ; i<3; i++){
			for(int j = 0 ; j<n ; j++){
				if(i==0){
					if(L[A[i][j]]==2) a+=1;
					if(L[A[i][j]]==1) a+=3;
				}
 
				if(i==1){
					if(L[A[i][j]]==2) b+=1;
					if(L[A[i][j]]==1) b+=3;
 
				}
				if(i==2){
					if(L[A[i][j]]==2) c+=1;
					if(L[A[i][j]]==1) c+=3;
 
			}
				
			}
		}
 
		cout<<a<<" "<<b<<" "<<c<<"\n";
 
	}
}