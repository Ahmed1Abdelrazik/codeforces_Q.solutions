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
 
#define for(i,n) for(int i = 0; i<n ; i++) 
#define For(i,a,n) for(int i = a; i<n ; i++) 
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
  		bool flag1 = false , flag2 = false;
  		int n,m; cin>>n>>m;
  		string a,b;
  		cin>>a>>b;
 
  		if(b.substr(1,m-1)==a.substr(n-m+1,m-1)){
  			flag1 =true;
  		}
 
  		for(i,n-m+1){
  			if(a[i]==b[0]){
  				flag2=true;
  				break;
  			}
  		}
  		if(flag1 && flag2){
  			cout<<"Yes\n";
  		}
  		else{
  			cout<<"No\n";
  		}
 
 
  	}
 
 
 
 
  	return 0;
 
}