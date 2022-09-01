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
 
		int res=0;
 
		string a[n];
		string b[n];
		for(int i = 0 ; i <n ; i++){
			cin>>a[i];
			b[i]=a[i];
 
 
		}
 
 
		for(int i =0 ; i<n ; i++){
			for(int j = 0 ; j<n ; j++){
				int zero = 0;
				if(a[i][j] == '0')        zero++;
				if(a[j][n-i-1] =='0')     zero++; 
				if(a[n-i-1][n-j-1] =='0') zero++;
				if(a[n-j-1][i] =='0')     zero++;
 
				if(zero>=2){
					a[i][j] = '0';     
					a[j][n-i-1] ='0';   
					a[n-i-1][n-j-1] ='0';
					a[n-j-1][i] ='0';
 
				}
				else{
					a[i][j] = '1';     
					a[j][n-i-1] ='1';   
					a[n-i-1][n-j-1] ='1';
					a[n-j-1][i] ='1';
 
				}
 
 
			}
		}
		
 
 
 
 
		for(int i =0 ; i<n ; i++){
			for(int j = 0 ; j<n ; j++){
				if(b[i][j]!=a[i][j])res++;
			}
		}
 
 
		cout<<res<<"\n";
 
	}
}